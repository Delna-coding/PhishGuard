def check_https(url):
    if url.startswith("https://"):
        return {
            "https": True,
            "reason": "Uses HTTPS."
        }

    return {
        "https": False,
        "reason": "Website does not use HTTPS."
    }