from port_scanner import scan_ports
from ping_test import ping_host
from ssl_checker import check_ssl_expiry
from password_checker import check_password_strength
from report_generator import generate_text_report

def main():
    target = input("Enter target IP/domain: ").strip()

    print("\n[+] Pinging target...")
    reachable, latency = ping_host(target)
    if reachable:
        print(f"✅ {target} is reachable. Latency: {latency} ms")
    else:
        print(f"❌ {target} is not reachable.")

    print("\n[+] Scanning common ports...")
    open_ports = scan_ports(target)
    if open_ports:
        print(f"✅ Open ports on {target}: {open_ports}")
    else:
        print("❌ No common ports are open.")
        
    print("\n[+] Checking SSL certificate (if applicable)...")
    ssl_info = check_ssl_expiry(target)
    if ssl_info["valid"]:
        print(f"✅ SSL Certificate valid, expires on {ssl_info['expiry_date'].strftime('%Y-%m-%d')}, days left: {ssl_info['days_left']}")
        print(f"Issuer: {ssl_info['issuer']}")
    else:
        print(f"❌ SSL Check failed: {ssl_info.get('error')}")

    print("\n[+] Password Strength Checker (optional)")
    password = input("Enter a password to check (or press Enter to skip): ")
    if password:
        score, errors = check_password_strength(password)
        print(f"Password strength score: {score}/5")
        if score < 5:
            print("Issues found:")
            for k, v in errors.items():
                if v:
                    print(f" - {k.replace('_', ' ').capitalize()}")
        else:
            print("Strong password!")
        password_info = (score, errors)
    else:
        password_info = None

    # Generate report
    report = generate_text_report(target, (reachable, latency), open_ports, ssl_info, password_info)
    print("\n--- REPORT ---\n")
    print(report)

    # Optionally save report to file
    with open(f"{target}_report.txt", "w") as f:
        f.write(report)


if __name__ == "__main__":
    main()
