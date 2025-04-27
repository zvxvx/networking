# author: Greg Pappas

from sys import argv
from socket import *
from urllib.parse import urlparse


flag = argv[1]

try:
    port = int(argv[2])
except ValueError:
    print("Invalid port entry. Must be an integer.")
    exit()

domain = argv[3]
# both of these are important to include for proper functionality. Without the / being appended, a bad request may be returned.
if not domain.startswith("http://"):
    print("Domain must have http:// prepended to it.")
    exit()
if not domain.endswith("/"):
    print("Domain must have / appended to it.")
    exit()
if port == 443:
    print("HTTPS is not supported, nor any port running the HTTPS protocol.")
    exit()

parsedInput = urlparse(domain)
netloc = parsedInput.netloc  # example.com
path = parsedInput.path  # /hello/ from example.com/hello
getRequest = f"GET {path} HTTP/1.1\r\nHost: {netloc}\r\nConnection: close\r\n\r\n"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((netloc, port))
clientSocket.send(getRequest.encode())

# ensure all of the request is saved to res.
res = b""
while True:
    data = clientSocket.recv(1024)
    if not data:
        break
    res += data

# split the header from the body.
if b"\r\n\r\n" in res:
    h, b = res.split(b"\r\n\r\n", 1)
else:
    b = res

# print or save depending on flag
if flag == "-p":
    print("Printing output...")
    print()
    print(b.decode())
elif flag == "-f":
    with open("http_output.txt", "w") as file:
        file.write(b.decode() + "\n")
    print("Results saved to http_output.txt")
else:
    print("Invalid flag. Use -p to print results or -f to save to http_output.txt.")

clientSocket.close()
