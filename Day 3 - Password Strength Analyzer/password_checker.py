import re
import getpass

# ==============================
#   ASCII Banner
# ==============================

banner = r"""
====================================================
   ____                                    _ 
  |  _ \ __ _ ___ _____      _____  _ __ __| |
  | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
  |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
  |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|

   ____  _                        _   _     
  / ___|| |_ _ __ ___ _ __   __ _| |_| |__  
  \___ \| __| '__/ _ \ '_ \ / _` | __| '_ \ 
   ___) | |_| | |  __/ | | | (_| | |_| | | |
  |____/ \__|_|  \___|_| |_|\__, |\__|_| |_|
                             |___/           

        Password Strength Analyzer
====================================================
"""

print(banner)

# Hide password input while typing
password = getpass.getpass("Enter Password: ")

strength = 0

print("\n[+] Running Security Checks...\n")

# Minimum Length Check
if len(password) >= 8:
    strength += 1
    print("[+] Minimum length verified")
else:
    print("[-] Password too short")

# Uppercase Check
if re.search(r"[A-Z]", password):
    strength += 1
    print("[+] Uppercase letter detected")
else:
    print("[-] No uppercase letter found")

# Lowercase Check
if re.search(r"[a-z]", password):
    strength += 1
    print("[+] Lowercase letter detected")
else:
    print("[-] No lowercase letter found")

# Number Check
if re.search(r"[0-9]", password):
    strength += 1
    print("[+] Number detected")
else:
    print("[-] No number found")

# Special Character Check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1
    print("[+] Special character detected")
else:
    print("[-] No special character found")

# Strength Result
print("\n====================================")
print(" Password Strength:", end=" ")

if strength == 5:
    print("STRONG 💪")
elif strength >= 3:
    print("MEDIUM ⚠️")
else:
    print("WEAK ❌")

print("====================================")