import socket

def main():
    host = "www.google.com"
    port = 80
    buffer_size = 4096
    payload = 'GET / HTTP/1.0\r\nHost: '+host+'\r\n\r\n'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        sock.sendall(payload.encode())
        sock.shutdown(socket.SHUT_WR)
        message = b""
        data = sock.recv(buffer_size)
        while data:
            message += data
            data = sock.recv(buffer_size)
        print(message.decode('ISO-8859-1'))

if __name__=="__main__":
    main()
