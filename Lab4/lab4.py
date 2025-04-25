# author: Greg Pappas

from sys import argv
from socket import *
from urllib.parse import urlparse


flag = argv[1]
port = int(argv[2])
domain = argv[3]
parsedInput = urlparse(domain)
netloc = parsedInput.netloc  # example.com
path = parsedInput.path  # /hello/ from example.com/hello
getRequest = f"GET {path} HTTP/1.1\r\nHost: {netloc}\r\nConnection: close\r\n\r\n"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((netloc, port))
clientSocket.send(getRequest.encode())

res = b""
while True:
    data = clientSocket.recv(1024)
    if not data:
        break
    res += data

# split the header from the body.
if b"\r\n\r\n" in res:
    h, b = res.split(b"\r\n\r\n", 1)

# print or save depending on flag
if flag == "-p":
    # print output
    print(b.decode())
elif flag == "-f":
    # save to file
    with open("http_output.txt", "w") as file:
        file.write(b.decode() + "\n")

clientSocket.close()
