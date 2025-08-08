# report_generator.py

def generate_text_report(target, ping_result, open_ports, ssl_info, password_info=None):
    lines = []
    lines.append(f"Network Health & Security Report for {target}")
    lines.append("=" * 40)

    reachable, latency = ping_result
    lines.append(f"Ping Test: {'Reachable' if reachable else 'Not reachable'}")
    if reachable:
        lines.append(f"Latency: {latency} ms")

    if open_ports:
        lines.append(f"Open Ports: {', '.join(str(p) for p in open_ports)}")
    else:
        lines.append("No common ports are open.")

    if ssl_info["valid"]:
        lines.append(f"SSL Certificate valid, expires on {ssl_info['expiry_date'].strftime('%Y-%m-%d')} ({ssl_info['days_left']} days left)")
        lines.append(f"Issuer: {ssl_info['issuer']}")
    else:
        lines.append(f"SSL Check failed: {ssl_info.get('error')}")

    if password_info:
        score, errors = password_info
        lines.append(f"Password strength score: {score}/5")
        if score < 5:
            lines.append("Password issues:")
            for k, v in errors.items():
                if v:
                    lines.append(f" - {k.replace('_', ' ').capitalize()}")
        else:
            lines.append("Password is strong.")

    return "\n".join(lines)
