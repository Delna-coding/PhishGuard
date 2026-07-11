import whois
from datetime import datetime, timezone
from urllib.parse import urlparse


def check_domain_age(url):
    try:
        domain = urlparse(url).netloc.replace("www.", "")

        info = whois.whois(domain)

        creation = info.creation_date

        if isinstance(creation, list):
            creation = creation[0]

        if creation:

            now = datetime.now(timezone.utc)

            if creation.tzinfo is None:
              creation = creation.replace(tzinfo=timezone.utc)

            age = (now - creation).days

            if age < 180:
                return {
                    "new_domain": True,
                    "age_days": age,
                    "reason": f"Domain registered only {age} days ago."
                }

            return {
                "new_domain": False,
                "age_days": age,
                "reason": f"Domain is {age} days old."
            }

        return {
            "new_domain": None,
            "reason": "Creation date unavailable."
        }

    except Exception as e:
        return {
            "new_domain": None,
            "reason": str(e)
        }


if __name__ == "__main__":

    print(check_domain_age("https://google.com"))