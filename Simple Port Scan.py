import socket

def port_scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except socket.gaierror:
        print(f"Could not resolve hostname")
    except socket.error:
        print(f"Could not connect to server")

# Define the target IP address
target_ip = "X.X.X.X"

# Scan the first 1024 ports
for port in range(1, 1024):
        port_scan(target_ip, port)
        if result > 0:
            open_ports.append(port)

if len(open_ports) > 0:
        print(f"The following ports are open: {open_ports}")
else:
    print("No open ports found")
