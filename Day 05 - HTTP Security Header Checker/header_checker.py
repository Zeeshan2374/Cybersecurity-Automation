import requests
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Red ASCII Banner
banner = r"""
 _   _ _____ _____ ____    ____                      _ _         
| | | |_   _|_   _|  _ \  / ___|  ___  ___ _   _ _ __(_) |_ _   _
| |_| | | |   | | | |_) | \___ \ / _ \/ __| | | | '__| | __| | | |
|  _  | | |   | | |  __/   ___) |  __/ (__| |_| | |  | | |_| |_| |
|_| |_| |_|   |_| |_|     |____/ \___|\___|\__,_|_|  |_|\__|\__, |
                                                             |___/

 _   _                _           
| | | | ___  __ _  __| | ___ _ __ 
| |_| |/ _ \/ _` |/ _` |/ _ \ '__|
|  _  |  __/ (_| | (_| |  __/ |   
|_| |_|\___|\__,_|\__,_|\___|_|   

Checker
"""

print(Fore.RED + banner)
print(Fore.CYAN + "=" * 65)
print(Fore.YELLOW + "HTTP Security Header Checker")
print(Fore.CYAN + "=" * 65)

# Get URL
url = input("\nEnter URL: ").strip()

# Auto-add HTTPS if missing
if not url.startswith(("http://", "https://")):
    url = "https://" + url

# Security headers to check
headers_to_check = {
    "Strict-Transport-Security":
        "Enforces HTTPS connections.",
    "Content-Security-Policy":
        "Helps prevent Cross-Site Scripting (XSS).",
    "X-Frame-Options":
        "Protects against clickjacking attacks.",
    "X-Content-Type-Options":
        "Prevents MIME-type sniffing.",
    "Permissions-Policy":
        "Controls browser features and APIs.",
    "Referrer-Policy":
        "Controls referrer information leakage.",
    "Cross-Origin-Opener-Policy":
        "Provides isolation against cross-origin attacks.",
    "Cross-Origin-Resource-Policy":
        "Restricts resource sharing across origins.",
    "Cross-Origin-Embedder-Policy":
        "Protects embedded resources."
}

try:
    print(Fore.CYAN + "\n[+] Connecting to target...\n")

    response = requests.get(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            )
        },
        timeout=10
    )

    print(Fore.CYAN + f"Status Code: {response.status_code}")

    if response.status_code != 200:
        print(
            Fore.YELLOW +
            f"Warning: Website returned status code "
            f"{response.status_code}"
        )

    print(Fore.CYAN + "\nChecking Security Headers...\n")

    found = 0
    missing_headers = []

    for header, recommendation in headers_to_check.items():

        if header in response.headers:
            found += 1

            print(
                Fore.GREEN +
                f"[+] {header} Found"
            )

            print(
                Fore.WHITE +
                f"    Value: {response.headers[header]}"
            )

        else:
            missing_headers.append(header)

            print(
                Fore.RED +
                f"[-] {header} Missing"
            )

    # Security Score
    total = len(headers_to_check)
    score = (found / total) * 100

    print(Fore.CYAN + "\n" + "=" * 65)
    print(Fore.YELLOW + f"Security Score: {score:.0f}%")
    print(Fore.CYAN + "=" * 65)

    # Score Rating
    if score >= 80:
        print(Fore.GREEN + "Security Rating: Excellent")
    elif score >= 60:
        print(Fore.YELLOW + "Security Rating: Good")
    elif score >= 40:
        print(Fore.YELLOW + "Security Rating: Average")
    else:
        print(Fore.RED + "Security Rating: Poor")

    # Recommendations
    if missing_headers:
        print(Fore.CYAN + "\nRecommendations:\n")

        for header in missing_headers:
            print(
                Fore.RED +
                f"[-] {header}"
            )
            print(
                Fore.WHITE +
                f"    Recommendation: "
                f"{headers_to_check[header]}"
            )

    # HTTPS Warning
    if url.startswith("http://"):
        print(
            Fore.RED +
            "\nWarning: Target website uses HTTP instead of HTTPS."
        )

except requests.exceptions.ConnectionError:
    print(
        Fore.RED +
        "\n[!] Connection Error: Unable to reach the website."
    )

except requests.exceptions.Timeout:
    print(
        Fore.RED +
        "\n[!] Timeout Error: Website took too long to respond."
    )

except requests.exceptions.RequestException as e:
    print(
        Fore.RED +
        f"\n[!] Request Error: {e}"
    )

except KeyboardInterrupt:
    print(
        Fore.RED +
        "\n\n[!] Scan cancelled by user."
    )