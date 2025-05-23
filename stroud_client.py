import socket

def boot_echo_client(host_ip = '127.0.0.1', port_num = 6000):
    # uses with statement to enure proper socket closure
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect((host_ip, port_num))
        print(f"connected to server at {host_ip}:{port_num}")

        while True:
            message = input("\nEnter message (type 'end' to exit): ")

            server.sendall(message.encode())
            print(f"\nSent: {message}")

            # receives server data and decodes into a message
            recv_message = server.recv(1024).decode()

            # prints server return message
            print(f"Received: {recv_message}")
            # breaks connection with server on receiving 'dne'
            if recv_message.lower() == 'dne':
                break

if __name__ == "__main__":
    boot_echo_client()