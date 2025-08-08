# Network Health & Security Checker (Basic Toolkit)

A simple Python toolkit that combines essential network and security checks into one easy-to-use script.  
Perfect for quickly assessing the health and security basics of a target device or domain.

---

## Features

- **Ping Test:** Checks if the target IP/domain is reachable and measures latency.  
- **Port Scanner:** Scans common TCP ports to identify which are open.  
- **SSL Certificate Checker:** Verifies if the target web server has a valid SSL/TLS certificate, its expiry date, and issuer.  
- **Password Strength Checker (optional):** Allows you to input a password and get a strength score with feedback.  
- **Report Generation:** Generates a clear, human-readable text report summarizing all findings, and saves it to a file.

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
