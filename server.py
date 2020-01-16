import requests, socket, threading, sys

def handle(client):
    # return
    message = ""
    with client:
        message = ""
        # data = client.recv(1024).decode()
        # while data != "end":
        #     message += data
        #     print(data)
        #     data = client.recv(1024).decode()
        client.sendall(message.encode())

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('localhost',8001))
        sock.listen(5)
        for i in range(5):
            client, address = sock.accept()
            print(client, address)
            thread = threading.Thread(target=handle, args=(client,))
            thread.run()

if __name__=="__main__":
    main()
