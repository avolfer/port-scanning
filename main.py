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

x = input("Type IP: ")

# Example usage
scan_ports(x, 1, 1024)
