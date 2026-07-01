import re
from urllib.parse import urlparse
def check_ip_address(url):

    domain = urlparse(url).netloc

    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

    if re.match(ip_pattern, domain):

        return {
            "ip_address": True,
            "reason": "URL uses an IP address instead of a domain."
        }

    return {
        "ip_address": False,
        "reason": "No IP address detected."
    }
if __name__ == "__main__":

    print(check_ip_address("http://192.168.1.10/login"))

    print(check_ip_address("https://google.com"))