Day 07 - Network Device Discovery Tool
A simple Python-based tool that discovers active devices on a local network and displays their IP addresses and hostnames.

Features
Discover active devices on a network
Resolve hostnames
Simple network visibility
Beginner-friendly implementation
Lightweight and fast
Technologies Used
Python
Socket
Subprocess
Installation
git clone https://github.com/viehgroup/cybersecurity-automation.git
cd Day-07-Network-Device-Discovery-Tool
Usage
python network_discovery.py
Enter a subnet prefix when prompted.

Example:

192.168.1
Example Output
Enter Network Prefix: 192.168.1

Scanning Network...

[+] Device Found
IP Address: 192.168.1.1
Hostname: router.local

[+] Device Found
IP Address: 192.168.1.10
Hostname: laptop.local
What You Will Learn
Network discovery concepts
Host identification
Python automation
Basic network enumeration
Challenge Task
Try improving this project by adding:

MAC address detection
Vendor identification
Multi-threaded scanning
Export results to CSV
Disclaimer
This project is intended for educational and authorized security testing purposes only.

30 Days of Cybersecurity Automation
Building practical cybersecurity tools