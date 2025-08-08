# ssl_checker.py
import socket
import ssl
from datetime import datetime

def check_ssl_expiry(hostname, port=443):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expiry_date_str = cert['notAfter']
                expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
                days_left = (expiry_date - datetime.utcnow()).days
                return {
                    "valid": True,
                    "expiry_date": expiry_date,
                    "days_left": days_left,
                    "issuer": dict(x[0] for x in cert['issuer'])['commonName']
                }
    except Exception as e:
        return {"valid": False, "error": str(e)}
