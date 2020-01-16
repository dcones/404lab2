import requests, socket, pdb

def main():
    # pdb.set_trace()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('localhost',8001))
        data = input()
        while data:
            sock.sendall(data.encode())
            data = input()
        sock.sendall(b"end")

        return_message = sock.recv(1024).decode()
        print(return_message)

def main():
    import urllib
    page = urllib.request.urlopen("http://www.google.com")
    contents = page.read()
    print(contents)

def main():
    # pdb.set_trace()
    host = "www.google.com"
    buffer_size = 4096
    port = 80
    payload = 'GET / HTTP/1.0\r\nHost: '+host+'\r\n\r\n'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        remote_ip = socket.gethostbyname(host)
        sock.connect((remote_ip,port))
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
