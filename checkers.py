from domain_age import check_domain_age
from brand_spoof import check_brand_spoof
from keyword_check import check_keywords
from ip_address import check_ip_address
from https_check import check_https


def run_all_checks(url):
    results = {}

    results["domain_age"] = check_domain_age(url)
    results["brand_spoof"] = check_brand_spoof(url)
    results["keywords"] = check_keywords(url)
    results["ip_address"] = check_ip_address(url)
    results["https"] = check_https(url)

    return results