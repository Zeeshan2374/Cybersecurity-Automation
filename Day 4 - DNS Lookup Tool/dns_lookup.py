import dns.resolver

# ==================================
#           ASCII BANNER
# ==================================

banner = r"""
==================================================
  ____  _   _ ____    _                _                
 |  _ \| \ | / ___|  | |    ___   ___ | | ___   _ _ __  
 | | | |  \| \___ \  | |   / _ \ / _ \| |/ / | | | '_ \ 
 | |_| | |\  |___) | | |__| (_) | (_) |   <| |_| | |_) |
 |____/|_| \_|____/  |_____\___/ \___/|_|\_\\__,_| .__/ 
                                                  |_|    

                DNS Lookup Tool
==================================================
"""

print(banner)

# Take user input
domain = input("Enter Domain: ").strip()

# DNS Record Types
record_types = ["A", "MX", "NS"]

# Lookup Loop
for record in record_types:

    print(f"\n[ {record} Records ]")

    try:
        answers = dns.resolver.resolve(domain, record)

        for data in answers:
            print(f"[+] {data}")

    except dns.resolver.NoAnswer:
        print(f"[-] No {record} record found")

    except dns.resolver.NXDOMAIN:
        print("[-] Domain does not exist")
        break

    except dns.resolver.Timeout:
        print("[-] Request timed out")

    except Exception as e:
        print(f"[-] Error fetching {record} records: {e}")

print("\n===================================")
print(" DNS Lookup Completed Successfully ")
print("===================================")