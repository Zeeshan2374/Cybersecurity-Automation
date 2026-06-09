import ssl
import socket
from datetime import datetime, timezone

# ASCII Banner
print(r"""
  ____           _     _____          _
 / ___|___ _ __ | |_  |_   _|__   ___| |___
| |   / _ \ '_ \| __|   | |/ _ \ / _ \ / __|
| |__|  __/ | | | |_    | | (_) |  __/ \__ \
 \____\___|_| |_|\__|   |_|\___/ \___|_|___/

        SSL Certificate Checker
""")

domain = input("Enter Domain (e.g. google.com): ").strip()

try:
    # Create SSL Context
    context = ssl.create_default_context()

    # Connect to the server
    with socket.create_connection((domain, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:

            cert = ssock.getpeercert()

            # Extract Issuer Information
            issuer = {}
            for item in cert.get('issuer', []):
                issuer.update(dict(item))

            valid_from = cert.get('notBefore', 'N/A')
            valid_until = cert.get('notAfter', 'N/A')

            # Convert expiry date
            expiry_date = datetime.strptime(
                valid_until,
                "%b %d %H:%M:%S %Y %Z"
            ).replace(tzinfo=timezone.utc)

            current_time = datetime.now(timezone.utc)

            days_remaining = (expiry_date - current_time).days

            print("\n" + "=" * 50)
            print("      SSL CERTIFICATE INFORMATION")
            print("=" * 50)

            print(f"Domain          : {domain}")
            print(f"Issuer          : {issuer.get('organizationName', 'Unknown')}")
            print(f"Valid From      : {valid_from}")
            print(f"Valid Until     : {valid_until}")
            print(f"Days Remaining  : {days_remaining}")

            if days_remaining < 0:
                print("Status          : EXPIRED")
            elif days_remaining <= 30:
                print("Status          : Expiring Soon")
            else:
                print("Status          : Valid")

            print("=" * 50)

except socket.gaierror:
    print("[!] Invalid domain or DNS resolution failed.")

except ssl.SSLError as e:
    print(f"[!] SSL Error: {e}")

except Exception as e:
    print(f"[!] Error: {e}")