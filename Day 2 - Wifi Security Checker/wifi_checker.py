import subprocess
import platform
import re
import sys


def banner():
    print(r"""
██╗    ██╗██╗███████╗██╗
██║    ██║██║██╔════╝██║
██║ █╗ ██║██║█████╗  ██║
██║███╗██║██║██╔══╝  ██║
╚███╔███╔╝██║██║     ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝

      WIFI Security Checker
""")
    print("=" * 70)


def get_windows_wifi():
    try:
        output = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True,
            text=True,
            encoding="utf-8"
        )

        ssid = re.search(r"^\s*SSID\s*:\s(.+)$", output, re.MULTILINE)
        signal = re.search(r"^\s*Signal\s*:\s(.+)$", output, re.MULTILINE)
        auth = re.search(r"^\s*Authentication\s*:\s(.+)$", output, re.MULTILINE)

        if not ssid:
            return None

        return {
            "ssid": ssid.group(1).strip(),
            "signal": signal.group(1).strip() if signal else "Unknown",
            "auth": auth.group(1).strip() if auth else "Unknown"
        }

    except Exception:
        return None


def get_linux_wifi():
    try:
        result = subprocess.run(
            ["nmcli", "-t", "-f", "active,ssid,security,signal", "dev", "wifi"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return None

        wifi_lines = result.stdout.splitlines()

        active_network = next(
            (line for line in wifi_lines if line.startswith("yes")),
            None
        )

        if not active_network:
            return None

        parts = active_network.split(":")

        if len(parts) < 4:
            return None

        return {
            "ssid": parts[1],
            "signal": parts[3] + "%",
            "auth": parts[2]
        }

    except FileNotFoundError:
        return None


def check_security(auth):
    auth_upper = auth.upper()

    print("\n[ SECURITY STATUS ]")

    if "WPA3" in auth_upper:
        print("[+] WPA3 detected (Strong Security)")
    elif "WPA2" in auth_upper:
        print("[+] WPA2 detected (Good Security)")
    elif "WPA" in auth_upper:
        print("[!] WPA detected (Older Security)")
    elif "OPEN" in auth_upper or "--" in auth_upper or auth_upper == "":
        print("[!] Open Network (No Encryption)")
    else:
        print("[?] Unknown Security Type")


def main():
    banner()

    os_name = platform.system()

    if os_name == "Windows":
        wifi = get_windows_wifi()
    elif os_name == "Linux":
        wifi = get_linux_wifi()
    else:
        print(f"[ERROR] Unsupported OS: {os_name}")
        sys.exit()

    if not wifi:
        print("[INFO] No active Wi-Fi connection detected OR required tools missing.")
        print("Linux requires: nmcli")
        sys.exit()

    print(f"\nOperating System  : {os_name}")
    print(f"Connected Wi-Fi   : {wifi['ssid']}")
    print(f"Signal Strength   : {wifi['signal']}")
    print(f"Encryption Type   : {wifi['auth']}")

    check_security(wifi["auth"])

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()