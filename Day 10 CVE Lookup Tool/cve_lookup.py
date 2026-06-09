import requests

# ASCII Banner
print(r"""
 ██████╗██╗   ██╗███████╗
██╔════╝██║   ██║██╔════╝
██║     ██║   ██║█████╗
██║     ╚██╗ ██╔╝██╔══╝
╚██████╗ ╚████╔╝ ███████╗
 ╚═════╝  ╚═══╝  ╚══════╝

  CVE VULNERABILITY LOOKUP TOOL
""")

cve_id = input("Enter CVE ID (e.g. CVE-2021-44228): ").upper().strip()

url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    vulnerabilities = data.get("vulnerabilities", [])

    if not vulnerabilities:
        print("\n[!] CVE not found.")
        exit()

    cve = vulnerabilities[0]["cve"]

    # Description
    descriptions = cve.get("descriptions", [])
    description = descriptions[0]["value"] if descriptions else "No description available."

    # CVSS Score
    metrics = cve.get("metrics", {})
    cvss_score = "N/A"

    if "cvssMetricV31" in metrics:
        cvss_score = metrics["cvssMetricV31"][0]["cvssData"]["baseScore"]

    elif "cvssMetricV30" in metrics:
        cvss_score = metrics["cvssMetricV30"][0]["cvssData"]["baseScore"]

    elif "cvssMetricV2" in metrics:
        cvss_score = metrics["cvssMetricV2"][0]["cvssData"]["baseScore"]

    # Severity Rating
    severity = "Unknown"

    if isinstance(cvss_score, (int, float)):
        if cvss_score >= 9.0:
            severity = "Critical"
        elif cvss_score >= 7.0:
            severity = "High"
        elif cvss_score >= 4.0:
            severity = "Medium"
        else:
            severity = "Low"

    print("\n" + "=" * 60)
    print("CVE VULNERABILITY REPORT")
    print("=" * 60)

    print(f"CVE ID      : {cve_id}")
    print(f"CVSS Score  : {cvss_score}")
    print(f"Severity    : {severity}")

    print("\nDescription:")
    print(description)

    print("=" * 60)

except requests.exceptions.Timeout:
    print("\n[!] Request timed out.")

except requests.exceptions.ConnectionError:
    print("\n[!] Network connection error.")

except requests.exceptions.HTTPError as e:
    print(f"\n[!] HTTP Error: {e}")

except Exception as e:
    print(f"\n[!] Error: {e}")