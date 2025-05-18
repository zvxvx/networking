# Lab 6
# Author: Greg Pappas
from urllib.parse import urlparse
from scapy.all import *
from socket import gethostbyname
from sys import argv

domain = argv[1]

if not domain.startswith("http://"):
    print("Domain must have http:// prepended to it.")
    exit()
if not domain.endswith("/"):
    print("Domain must have / appended to it.")
    exit()

parsedInput = urlparse(domain)
netloc = parsedInput.netloc  # example.com
path = parsedInput.path  # /hello/ from example.com/hello
getRequest = f"GET {path} HTTP/1.1\r\nHost: {netloc}\r\nConnection: close\r\n\r\n"

tcp_packet=TCP()
ip_packet=IP()

ip_packet.dst=gethostbyname(netloc)

tcp_packet.dport=80
tcp_packet.sport=12345
tcp_packet.flags="S"
tcp_packet.seq=4

synack = sr1(ip_packet/tcp_packet)

tcp_packet.flags="A"
tcp_packet.seq = synack.ack
tcp_packet.ack = synack.seq + 1
send(ip_packet/tcp_packet)

tcp_packet.flags="PA"
send(ip_packet/tcp_packet/getRequest)
