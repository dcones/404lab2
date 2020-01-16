import socket

def main():
    buffer_size = 4096
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start, socket.socket(socket.AF_INET, socket.SOCK_STREAM) as end:
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Accept local connections
        local_host = "localhost"
        local_port = 8001
        start.bind((local_host,local_port))
        start.listen(1)

        # Accept client connection
        client, address = start.accept()

        # Connect to google
        end_host = "www.google.com"
        end_port = 80
        end.connect((end_host,end_port))

        # Get request from client
        client_data = client.recv(buffer_size)

        # Send client's request to google
        end.sendall(client_data)

        # Inform google we are done writing
        end.shutdown(socket.SHUT_WR)

        # Get google's response
        message = b""
        response = end.recv(buffer_size)
        while response:
            message += response
            response = end.recv(buffer_size)

        # Send google's response to client
        client.sendall(message)

if __name__=="__main__":
    main()
