# Author: Greg Pappas

from scapy.all import *  # type: ignore
from socket import gethostbyname
from sys import argv
from subprocess import getstatusoutput

domain = argv[1]
max_hops = int(argv[2])
as_nums = []
as_str = ""

ip = IP()  # type: ignore

tcp = TCP()  # type: ignore
tcp.flags = "S"

try:
    ip_add = gethostbyname(domain)
    ip.dst = ip_add
except:
    print(f"{domain} could not be resolved. try another domain.")
    exit(1)

route = f"route to {domain} ({ip_add}), {max_hops} hops max"
print(route)


for i in range(1, max_hops + 1):
    ip.ttl = i
    packet = ip / tcp
    response = sr1(packet, verbose=0, timeout=3)

    if response is None:
        print(f"{i} - * * *")
    else:
        print(f"{i} - {response.src}")
        status, str = getstatusoutput(
            f"whois -h whois.cymru.com '-v {response.src}' | awk '{{print $1}}'"
        )
        try:
            as_num = int(str.splitlines()[2])
        except:
            continue

        if as_nums.count(as_num) == 0:
            as_nums.append(as_num)

        if response.src == ip_add:
            break

for i in range(len(as_nums)):
    as_str += f"AS{as_nums[i]} -> "

if len(as_nums) > 0:
    print(f"Traversed AS numbers: {as_str[:-4]}")
