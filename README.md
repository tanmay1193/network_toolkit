# Network Health & Security Checker (Basic Toolkit)

A simple Python toolkit that combines essential network and security checks into one easy-to-use script.  
Perfect for quickly assessing the health and security basics of a target device or domain.

---

## Features

- **Ping Test:** Checks if the target IP/domain is reachable and measures latency.  
- **Port Scanner:** Scans common TCP ports to identify which are open.  
- **SSL Certificate Checker:** Verifies if the target web server has a valid SSL/TLS certificate, its expiry date, and issuer.  
- **Password Strength Checker (optional):** Allows you to input a password and get a strength score with feedback.  
- **Report Generation:** Generates a clear, human-readable text report summarizing all findings and saves it to a file.

---

## Why This Project?

- Combines multiple small but useful network and security utilities into one script.  
- Helps users and admins quickly check network health and basic security posture.  
- Great learning project for Python networking (sockets, SSL, subprocess), regex, and report generation.  
- Easily extendable with new checks and features.  
- Useful demo and portfolio project for cybersecurity and Python programming roles.

---

## Tech Stack / Libraries Used

- `socket` (built-in) — for port scanning and SSL connection.  
- `ping3` — for ICMP ping tests.  
- `ssl` and `datetime` — to inspect SSL certificates.  
- `re` — regex-based password strength checking.  
- Basic file handling for report saving.

---

## Getting Started

### Prerequisites

- Python 3.x installed (recommend Python 3.8+).  
- `ping3` library installed:
  ```bash
  pip install ping3

### 1. Clone the repository:
 ```bash
git clone https://github.com/yourusername/network_health_security_checker.git
cd network_health_security_checker
```
### 2. (Optional) Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
### 4. Run the main script:
```bash
python3 main.py
```
### 5. Follow the prompts to enter a target IP/domain and optionally test a password.

## Sample Outupt
```bash
Enter target IP/domain: 0xtechietanmay.vercel.app

[+] Pinging target...
✅ 0xtechietanmay.vercel.app is reachable. Latency: 20.9 ms

[+] Scanning common ports...
✅ Open ports on 0xtechietanmay.vercel.app: [80, 443]

[+] Checking SSL certificate (if applicable)...
✅ SSL Certificate valid, expires on 2025-09-22, days left: 45
Issuer: R11

[+] Password Strength Checker (optional)
Enter a password to check (or press Enter to skip): Cc@7699481!
Password strength score: 5/5
Strong password!

--- REPORT ---

Network Health & Security Report for 0xtechietanmay.vercel.app
========================================
Ping Test: Reachable
Latency: 20.9 ms
Open Ports: 80, 443
SSL Certificate valid, expires on 2025-09-22 (45 days left)
Issuer: R11
Password strength score: 5/5
Password is strong.
```
## Project Structure
```bash
network_health_security_checker/
│
├── main.py               # Main script to run the toolkit
├── port_scanner.py       # Port scanning functionality
├── ping_test.py          # Ping functionality
├── ssl_checker.py        # SSL certificate checking
├── password_checker.py   # Password strength checker
├── report_generator.py   # Report generation logic
├── requirements.txt      # Python dependencies
└── README.md             # This file
```
## Future Enhancements
  - Add CLI arguments for automated runs.
  - Implement multi-threaded scanning for faster results.
  - Integrate WHOIS, DNS lookups, and GeoIP location info.
  - Generate HTML or JSON formatted reports.
  - Add vulnerability scanning modules (e.g., nmap integration).
