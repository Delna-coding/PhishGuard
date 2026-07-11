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

    # Official domain
    if domain in trusted_domains.values():
        return {
            "spoof": False,
            "reason": "Official domain"
        }

    # Brand name appears inside domain
    for brand, official in trusted_domains.items():

        if brand in domain:
            return {
                "spoof": True,
                "reason": f"Contains trusted brand name '{brand}'"
            }

    # Typo detection
    for brand, official in trusted_domains.items():

        score = similarity(domain, official)

        if score > 0.70:
            return {
                "spoof": True,
                "reason": f"Looks similar to {official}",
                "similarity": round(score, 2)
            }

    return {
        "spoof": False,
        "reason": "No spoof detected"
    }