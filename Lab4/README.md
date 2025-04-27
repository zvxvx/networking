# lab4

### Completed by Greg Pappas

## Setup

None needed. Should work as intended as long as python 3 is installed.

## Usage:

- `python3 lab4.py <flag> <port> http://<domain>/`

### flags

- `-p` sends results to stdout.
- `-f` sends results to the file http_output.txt

### port

- Must be an integer value. This program works specifically for the HTTP\1.1 protocol, so any port running the HTTP protocol can be used. Any HTTPS protocol port used is likely to have the connection reset by peer.

### domain

Must have http:// prepended to the actual domain and have / appended to the end of the domain. If not added, the program will tell you to add them.

- Example: `python3 lab4.py -p 80 httpforever.com` will _not_ work.
- However, `python3 lab4.py -p 80 http://httpforever.com/` _will_ work

## Examples:

#### Run the following in the terminal.

- `python3 lab4.py -p 80 http://httpforever.com/`
- `python3 lab4.py -f 80 http://httpforever.com/`
- `python3 lab4.py -p 80 http://httpforever.com/login/`

## Program description

This program performs similarly to curl and wget. Running the program will print out or save the contents of the webpage to a file of the selected domain running on HTTP.

## Questions

1. Why did you have to encode() your request and decode() the response(s)?
   What do these functions do?

- Encoding and decoding is necessary with raw sockets for data transmission because it deals with raw bytes, and this is because of the low level nature of working with raw sockets.
- Encoding allows us to use convert the message to bytes with utf-8, unless otherwise specified.
- Decoding allows us to convert the bytes back into a string. Without these two functions, we'd have a _very_ hard time making use of the data sent and received.

2. What changes would you have to make to create a UDP socket?

- `clientSocket = socket(AF_INET, SOCK_STREAM)` would need to be changed to `clientSocket = socket(AF_INET, SOCK_DGRAM)`
- `clientSocket.connect((netloc, port))` and `clientSocket.send(getRequest.encode())` would be replaced with `clientSocket.sendto(getRequest.encode(), (netloc, port))`
- `clientSocket.recv(1024)` would be replaced with `clientSocket.recvfrom(1024)`

3. If you wanted to create a TCP server, what would you have to change?

- If it was previously UDP, do the reverse of above.

4. Can your TCP client create or process HTTPS traffic? What happens if
   you send a request to port 443?

- This program does not support the processing of HTTPS traffic. It is programmed to handle HTTP\1.1 requests. The connection will be reset by peer if attempted. In this program 443 specifically will be rejected.
