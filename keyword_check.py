def check_keywords(url):
    keywords = [
        "login",
        "verify",
        "password",
        "bank",
        "account",
        "update",
        "secure"
    ]

    url_lower = url.lower()
    found = [k for k in keywords if k in url_lower]

    if found:
        return {
            "suspicious": True,
            "reason": "Suspicious keywords found: " + ", ".join(found)
        }

    return {
        "suspicious": False,
        "reason": "No suspicious keywords found."
    }


if __name__ == "__main__":
    print(check_keywords("http://paypal-login.xyz"))
    print(check_keywords("https://google.com"))