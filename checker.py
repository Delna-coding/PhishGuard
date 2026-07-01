from urllib.parse import urlparse
from difflib import SequenceMatcher


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def check_brand_spoof(url):
    trusted_domains = {
        "amazon": "amazon.com",
        "google": "google.com",
        "paypal": "paypal.com",
        "apple": "apple.com",
        "microsoft": "microsoft.com"
    }

    domain = urlparse(url).netloc.lower().replace("www.", "")

    # If it's an official domain, it's not a spoof
    if domain in trusted_domains.values():
        return {
            "spoof": False,
            "reason": "Official domain"
        }

    # Compare against trusted domains
    for brand, official in trusted_domains.items():

        score = similarity(domain, official)

        if score > 0.75:
            return {
                "spoof": True,
                "reason": f"Looks similar to {official}",
                "similarity": round(score, 2)
            }

    return {
        "spoof": False,
        "reason": "No spoof detected"
    }


def analyze_url(url):

    score = 0
    reasons = []

    url_lower = url.lower()

    # HTTPS Check
    if not url_lower.startswith("https"):
        score += 20
        reasons.append("Website is not using HTTPS.")

    # Suspicious Keywords
    keywords = [
        "login",
        "verify",
        "password",
        "bank",
        "account",
        "update",
        "secure"
    ]

    found = [k for k in keywords if k in url_lower]

    if found:
        score += 20
        reasons.append(
            "Suspicious keywords: " + ", ".join(found)
        )

    # Long URL
    if len(url) > 75:
        score += 10
        reasons.append("Very long URL.")

    # Brand Spoof
    spoof = check_brand_spoof(url)

    if spoof["spoof"]:
        score += 30
        reasons.append(spoof["reason"])

    # Final Verdict
    if score < 30:
        verdict = "SAFE 🟢"
    elif score < 60:
        verdict = "SUSPICIOUS 🟡"
    else:
        verdict = "DANGEROUS 🔴"

    return {
        "url": url,
        "score": min(score, 100),
        "verdict": verdict,
        "reasons": reasons
    }


if __name__ == "__main__":

    test_urls = [

        "https://google.com",

        "http://paypal-login.xyz",

        "https://amaz0n.com",

        "http://verify-bank-account-login.xyz"

    ]

    for url in test_urls:

        print("=" * 50)

        result = analyze_url(url)

        print(result)