import math
from collections import Counter

SUSPICIOUS_TLDS = [".xyz", ".tk", ".ml", ".ga", ".top", ".click"]

KNOWN_BRANDS = ["paypal", "google", "apple", "microsoft", "amazon", "netflix"]


def calculate_entropy(url):
    counts = Counter(url)
    total = len(url)
    entropy = -sum((c/total) * math.log2(c/total) for c in counts.values())
    return round(entropy, 2)


def has_suspicious_tld(url):
    for tld in SUSPICIOUS_TLDS:
        if tld in url.lower():
            return True
    return False


def has_misleading_brand(url):
    domain = url.split("//")[-1].split("/")[0].lower()
    for brand in KNOWN_BRANDS:
        if brand in url.lower() and brand not in domain:
            return True
    return False


def calculate_risk_score(entropy, suspicious_tld, misleading_brand):
    score = 0
    if entropy > 3.5:
        score += 3
    if suspicious_tld:
        score += 4
    if misleading_brand:
        score += 5
    return min(score, 10)


def generate_explanation(score, suspicious_tld, misleading_brand, entropy):
    if score == 0:
        return "This URL looks safe. No suspicious signals were detected."
    
    reasons = []
    if misleading_brand:
        reasons.append("it appears to impersonate a well known brand")
    if suspicious_tld:
        reasons.append("it uses a domain extension commonly associated with phishing")
    if entropy > 3.5:
        reasons.append("the URL contains unusual random-looking characters")

    reason_text = " and ".join(reasons)
    
    if score <= 3:
        level = "low"
    elif score <= 6:
        level = "moderate"
    else:
        level = "high"

    return f"This URL has a {level} risk score of {score}/10 because {reason_text}. Exercise caution before clicking."


async def analyze_url(url):
    entropy = calculate_entropy(url)
    suspicious_tld = has_suspicious_tld(url)
    misleading_brand = has_misleading_brand(url)
    score = calculate_risk_score(entropy, suspicious_tld, misleading_brand)
    explanation = generate_explanation(score, suspicious_tld, misleading_brand, entropy)

    return {
        "url": url,
        "risk_score": score,
        "entropy": entropy,
        "suspicious_tld": suspicious_tld,
        "misleading_brand": misleading_brand,
        "explanation": explanation
    }