# author: Greg Pappas

from sys import argv
from socket import *
from urllib.parse import urlparse


flag = argv[1]
port = int(argv[2])
domain = argv[3]
parsedInput = urlparse(f"http://{domain}/")
scheme = parsedInput.scheme  # http
netloc = parsedInput.netloc  # example.com
path = parsedInput.path  # /hello/ from example.com/hello
print(scheme, netloc, path)
getRequest = f"GET {path} HTTP/1.1\r\nHost: {netloc}\r\nConnection: close\r\n\r\n"
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((netloc, port))
clientSocket.send(getRequest.encode())
res = clientSocket.recv(1024)

if flag == "-p":
    # print output
    print("From server: ", res.decode())
elif flag == "-f":
    # save to file
    with open("http_output.txt", "w") as file:
        file.write(res.decode())
clientSocket.close()
