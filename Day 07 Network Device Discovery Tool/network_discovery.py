import subprocess
import socket
import platform

# ASCII Banner
print(r"""
 _   _      _                      _
| \ | | ___| |___      _____  _ __| | __
|  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
| |\  |  __/ |_ \ V  V / (_) | |  |   <
|_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\

      Network Device Discovery Scanner
""")

network = input(
    "Enter Network Prefix (e.g. 192.168.1): "
).strip()

active_hosts = []

# Detect Operating System
param = "-n" if platform.system().lower() == "windows" else "-c"

print("\nScanning Network...\n")

for i in range(1, 255):
    ip = f"{network}.{i}"

    try:
        result = subprocess.run(
            ["ping", param, "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=2
        )

        if result.returncode == 0:

            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "Unknown"

            active_hosts.append((ip, hostname))

            print("[+] Device Found")
            print(f"IP Address : {ip}")
            print(f"Hostname   : {hostname}")
            print("-" * 40)

    except subprocess.TimeoutExpired:
        continue

    except Exception:
        continue

# Summary Report
print("\n" + "=" * 50)
print("SCAN COMPLETED")
print("=" * 50)

print(f"Total Active Devices Found: {len(active_hosts)}")

if active_hosts:
    print("\nDiscovered Hosts:")
    for ip, hostname in active_hosts:
        print(f"{ip:<16} {hostname}")

print("=" * 50)