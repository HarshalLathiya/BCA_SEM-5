import socket

def create_socket():
    try:
        # Create a socket object (IPv4, TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created ✅")

        # Example: resolve localhost
        host = socket.gethostname()
        port = 12345

        # Bind the socket to host and port
        s.bind((host, port))
        print(f"Socket binded to {host}:{port}")

        # Put the socket into listening mode
        s.listen(5)
        print("Socket is now listening... 🔊")

        # Accept a connection (blocking call)
        conn, addr = s.accept()
        print("Got connection from", addr)

        conn.send(b"Hello! You are connected to the server.")
        conn.close()

    except socket.error as err:
        print("Socket creation failed with error:", err)

if __name__ == "__main__":
    create_socket()
