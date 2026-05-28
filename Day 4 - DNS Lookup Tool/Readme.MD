Day 04 - DNS Lookup Tool
A simple Python-based DNS lookup tool that retrieves important DNS records for a target domain.
Features
•	Fetch A records
•	Retrieve MX records
•	Get NS records
•	Beginner-friendly implementation
•	Simple command-line interface
Technologies Used
•	Python
•	dnspython
📂 Installation
Clone the repository and navigate to the project directory:
git clone https://github.com/<url>
cd filename
Install dependencies:
pip install dnspython
▶️ Usage
Run the script using Python:
python dns_lookup.py
Enter a domain name when prompted.
Example:
example.com
Example Output
Enter Domain: amazon.com

[ A Records ]
[+] 98.82.161.185
[+] 98.87.170.71
[+] 98.87.170.74

[ MX Records ]
[+] 5 amazon-smtp.amazon.com.

[ NS Records ]
[+] ns-264.awsdns-33.com.
[+] ns-521.awsdns-01.net.
[+] ns-1447.awsdns-52.org.
[+] ns-1707.awsdns-21.co.uk.

===================================
 DNS Lookup Completed Successfully 
===================================
What You Will Learn
•	DNS fundamentals
•	DNS record enumeration
•	Python automation
•	Domain intelligence gathering
Challenge Task
Try improving this project by adding:
•	TXT record lookup
•	Subdomain discovery
•	Reverse DNS lookup
•	Export results to a file
•	Whois integration
•	ASN information lookup
⚠️ Disclaimer
This project is intended for educational and authorized security testing purposes only.
30 Days of Cybersecurity Automation 
Building practical cybersecurity tools, one day at a time.

