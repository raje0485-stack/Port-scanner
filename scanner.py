# 1. Import libraries FIRST
import socket
from concurrent.futures import ThreadPoolExecutor

# 2. Define function SECOND
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            if port == 22:
                print(f"Port {port} is OPEN — Risk: Remote access possible!")
            elif port == 80:
                print(f"Port {port} is OPEN — Risk: Web server exposed!")
            elif port == 445:
                print(f"Port {port} is OPEN — Risk: File sharing exposed! Ransomware risk!")
            else:
                print(f"Port {port} is OPEN")
    except:
        pass

# 3. Get target THIRD
target = input("Enter target IP or domain: ")
ports = range(1, 1025)
print(f"\nScanning target: {target}\n")

# 4. Run scanner LAST
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, ports)

print("\nScan Completed!")
