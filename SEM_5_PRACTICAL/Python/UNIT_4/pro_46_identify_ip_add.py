import socket

# Get the hostname of the system
hostname = socket.gethostname()

# Get the IP address of the hostname
ip_address = socket.gethostbyname(hostname)

print("Host Name:", hostname)
print("IP Address:", ip_address)
