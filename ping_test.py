# ping_test.py
from ping3 import ping

def ping_host(host):
    response = ping(host)
    if response is None:
        return False, None
    return True, round(response * 1000, 2)  # milliseconds
