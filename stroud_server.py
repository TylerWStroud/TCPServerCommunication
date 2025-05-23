import socket

# using local ip with small port number
def boot_echo_server(host_ip = '127.0.0.1', port_num = 6000):
    # declaring TCP server
    # uses with statement to enure proper socket closure
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # binding server to the ip and port
        server.bind((host_ip, port_num))
        # waits for connection (one client at a time)
        server.listen()
        # client connects to server
        connection, address = server.accept()

        with connection:
            # displays/confirms connection
            print(f"Connected by {address}")
            while True:
                data = connection.recv(1024)
                if not data:
                    break


                reverse_recv_message = data.decode()[::-1]
                print(f"\nReceived: {data.decode()}")
                connection.sendall(reverse_recv_message.encode())
                print(f"Echoed: {reverse_recv_message}")

if __name__ == "__main__":
    boot_echo_server()
