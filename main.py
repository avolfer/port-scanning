import socket

def scan_ports(host, start_port, end_port):
    """Scan ports on a given host."""
    for port in range(start_port, end_port+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((host, port))
            print(f"Port {port} is open.")
        except socket.error:
            pass
        s.close()

# Example usage
scan_ports("127.0.0.1", 1, 1024)
