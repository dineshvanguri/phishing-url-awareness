
from urllib.parse import urlparse
import ipaddress


def check_url(url):
    warnings = []

    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    if "@" in url:
        warnings.append("URL contains @ symbol")

    if len(url) > 100:
        warnings.append("URL is longer than 100 characters")

    try:
        ipaddress.ip_address(hostname)
        warnings.append("URL uses an IP address instead of a domain")
    except ValueError:
        pass

    if len(hostname.split(".")) >= 5:
        warnings.append("URL has many hostname segments")

    if "xn--" in hostname:
        warnings.append("URL contains punycode")

    if parsed.scheme == "http":
        warnings.append("URL uses HTTP instead of HTTPS")

    return warnings


def main():
    print("=== Phishing URL Awareness Checker ===")
    print("This tool checks URL text for warning signs.")
    print("It does not visit websites or prove whether a URL is safe.")

    while True:
        url = input("\nEnter a URL (or type 'quit' to exit): ").strip()

        if url.lower() == "quit":
            print("Goodbye!")
            break

        if not url:
            print("Please enter a URL.")
            continue

        warnings = check_url(url)

        if warnings:
            print("\nWarning signs found:")
            for warning in warnings:
                print("-", warning)
        else:
            print("\nNo listed warning signs found.")
            print("This does NOT mean the URL is safe.")


if __name__ == "__main__":
    main()
