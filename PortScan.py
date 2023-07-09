import socket

target = input("Enter the target IP address: ")
min_port = int(input("Enter the minimum port number: "))
max_port = int(input("Enter the maximum port number: "))

print(f"\nScanning ports {min_port} to {max_port} on {target}...\n")

for port in range(min_port, max_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: Open")
    sock.close()

print("\nPort scanning complete.")
