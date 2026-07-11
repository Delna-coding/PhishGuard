def calculate_score(results):
    score = 0
    reasons = []

    # Domain Age
    domain = results["domain_age"]

    if domain["new_domain"]:
        score += 25
        reasons.append(domain["reason"])

    # Brand Spoof
    spoof = results["brand_spoof"]

    if spoof["spoof"]:
        score += 30
        reasons.append(spoof["reason"])

    # Keyword Check
    keyword = results["keywords"]

    if keyword["suspicious"]:
        score += 20
        reasons.append(keyword["reason"])

    # IP Address
    ip = results["ip_address"]

    if ip["ip_address"]:
        score += 25
        reasons.append(ip["reason"])

    # HTTPS Check
    https = results["https"]

    if not https["https"]:
        score += 20
        reasons.append(https["reason"])

    # Final Verdict
    if score < 10:
        verdict = "🟢 SAFE"
    elif score <= 30:
        verdict = "🟡 SUSPICIOUS AND POTENTIAL RISK" 
    elif score < 60:
        verdict = "🟡 SUSPICIOUS"
    else:
        verdict = "🔴 DANGEROUS"

    return {
        "score": min(score, 100),
        "verdict": verdict,
        "reasons": reasons
    }