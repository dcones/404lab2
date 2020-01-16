import requests, socket, threading, sys

def handle(client):
    with client:
        data = client.recv(1024)
        print(data.decode())
        client.sendall(data)

def main():
    host = ""
    port = 8001
    num_connections = 5
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host,port))
        sock.listen(num_connections)
        for i in range(num_connections):
            client, address = sock.accept()
            # print(client, address)
            print("Connected by ", address)
            thread = threading.Thread(target=handle, args=(client,))
            thread.run()

if __name__=="__main__":
    main()
