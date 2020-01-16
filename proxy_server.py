import socket, threading

end_host = "www.google.com"
end_port = 80
buffer_size = 4096

def handle(client):
    with client, socket.socket(socket.AF_INET, socket.SOCK_STREAM) as end:
        # Connect to google
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

def main():
    local_host = "localhost"
    local_port = 8001
    num_connections = 5
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start:
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Accept local connections
        start.bind((local_host,local_port))
        start.listen(num_connections)
        for i in range(num_connections):
            # Accept client connection
            client, address = start.accept()
            print("Connected by ", address)

            # Start thread to handle client
            thread = threading.Thread(target=handle, args=(client,))
            thread.run()

if __name__=="__main__":
    main()
