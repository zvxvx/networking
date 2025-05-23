# Author: Greg Pappas

from scapy.all import *
from socket import gethostbyname
from sys import argv
from subprocess import getstatusoutput

domain = argv[1]
max_hops = int(argv[2]);
ip_add = gethostbyname(domain)

# if not domain.startswith("http://"):
#     print("Domain must have http:// prepended to it.")
#     exit()
# if not domain.endswith("/"):
#     print("Domain must have / appended to it.")
#     exit()

tcp_packet=TCP() # type: ignore
ip_packet=IP(ttl=1) # type: ignore
ip_packet.dst=ip_add

route = f"route to {domain} ({ip_add}), {max_hops} hops max"
print(route)
for i in range(max_hops):
    i = i + 1
    ip_packet.ttl= i
    print(i)

# synack = sr1(ip_packet/tcp_packet, verbose=0, timeout=3)

# send(ip_packet/tcp_packet)