# port_scanner.py
import socket

def scan_ports(target, ports=[22, 80, 443, 8080]):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # 1 second timeout
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass
    return open_ports
