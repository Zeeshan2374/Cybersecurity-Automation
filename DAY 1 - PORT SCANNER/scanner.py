import socket
import os
from colorama import Fore, init

init(autoreset=True)

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# PORT SCANNER Banner
banner = f"""
{Fore.RED}
██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝   ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║
██║     ╚██████╔╝██║  ██║   ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝

███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
{Fore.YELLOW}
==============================================================
"""

print(banner)

target = input(Fore.WHITE + "Enter Target IP/Domain: ")
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print(Fore.CYAN + f"\nScanning Target: {target}")
print(Fore.YELLOW + "-" * 50)

for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print(Fore.GREEN + f"[+] Port {port} is OPEN")

        s.close()

    except KeyboardInterrupt:
        print(Fore.RED + "\nScan stopped by user.")
        exit()

    except socket.gaierror:
        print(Fore.RED + "Hostname could not be resolved.")
        exit()

    except socket.error:
        print(Fore.RED + "Could not connect to server.")
        exit()

print(Fore.CYAN + "\nScan Completed.")