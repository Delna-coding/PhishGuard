import requests

# Replace this with your own Google Safe Browsing API key
API_KEY = "YOUR_API_KEY"

API_URL = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"


def check_safe_browsing(url):
    payload = {
        "client": {
            "clientId": "phishguard",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": [
                "MALWARE",
                "SOCIAL_ENGINEERING",
                "UNWANTED_SOFTWARE"
            ],
            "platformTypes": [
                "ANY_PLATFORM"
            ],
            "threatEntryTypes": [
                "URL"
            ],
            "threatEntries": [
                {
                    "url": url
                }
            ]
        }
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code != 200:
            return {
                "unsafe": None,
                "reason": f"API Error ({response.status_code})"
            }

        data = response.json()

        if "matches" in data:
            return {
                "unsafe": True,
                "reason": "URL found in Google Safe Browsing database."
            }

        return {
            "unsafe": False,
            "reason": "URL not found in Google Safe Browsing database."
        }

    except Exception as e:
        return {
            "unsafe": None,
            "reason": str(e)
        }


if __name__ == "__main__":
    print(check_safe_browsing("https://google.com"))
    