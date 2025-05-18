# Lab 6

### Completed by Greg Pappas

## Setup

Users will need to install (https://scapy.net/)[scapy] in order to use the program. To capture the traffic sent by the program, the user will also need to install tcpdump and either use tcpdump to read the .pcap file or wireshark. To capture the data appropriately, iptables will also need to be installed and used.

## Usage:

#### sudo is required to run this program.

- `sudo python3 lab6.py <domain>`

#### Be sure to run tcpdump in another terminal window to capture the packets for analysis.
`sudo tcpdump -i any -w test.pcap port 80`

#### To successfully send packets without the transmission being interrupted with reset packets, the user will need to use iptables in the structure shown below.
```sh
sudo iptables -I OUTPUT -p tcp --tcp-flags ALL RST -j DROP
sudo python3 lab6.py http://example.com/
sudo iptables -D OUTPUT -p tcp --tcp-flags ALL RST -j DROP
```
It is better to write this out in a script that handles the commands for you, so feel free to use the included test.sh file.

### domain

Must have http:// prepended to the actual domain and have / appended to the end of the domain. If not added, the program will tell you to add them.

- Example: `sudo python3 lab6.py httpforever.com` will _not_ work.
- However, `sudo python3 lab6.py http://httpforever.com/` _will_ work

## Examples:

- `sudo python3 lab6.py http://httpforever.com/`
- `sudo python3 lab6.py http://http-password.badssl.com/`
- `sudo python3 lab6.py http://example.com/`

## Program description

This program manually creates a three-way handshake with syn->syn-ack->ack packets crafted with scapy. It then makes a push-ack packet that sends a get request to a domain. This can be recorded with tcpdump and traced back with wireshark to verify results of a successful three-way handshake and get request.

## Questions

1. In lab 4 you sent a GET request using the sockets library. What did the
sockets library do for you?
- The sockets library handled the three-way handshake syn->syn-ack->ack packets and push packet of the get request for us so we didn't have to make the packets ourselves.

2. Before you submit this lab, you should check that your pcap contains the
correct traffic. What program should you use to analyze your pcap? In
your pcap, did the server send you the complete HTML for the website or
just a portion of the HTML? (Does the response end with a </html> tag?)
- You can use tcpdump or wireshark to analyze the pcap, but wireshark has a GUI to make it easy to reassemble the packets by following the TCP stream.
- In most cases, the server only sends us a portion of the site as it doesn't end with a closing html tag (e.g. httpforever.com). However, if the site is simple and barebones, it is possible to get an entire webpage to be sent by the server. (e.g. http://example.com)

3. Is your program guaranteed to receive a complete HTML response from
the website? Why or why not.
- Since mechanisms are not put in place to ensure complete HTML response, we are limited by how robust the site is. If it has a lot of content, we are not going to get a complete HTML response; however, if the site is plain with little text, it is possible to get a complete HTML response.

4. Can you merge the final ACK of the three-way handshake with the GET
request? That is, can you merge the two packets into one? If yes, explain
how such an option might be beneficial.
- Yes, you can. Instead of having a packet with the flag of "A", you can merge that packet by using "PA" and append the getRequest to the send request of that packet. That way you don't need packet flags of "A" _and_ "PA".
- By merging, it is one less packet to be sent, which is one less packet to be processed. On a large scale, this saves a lot of network/processing usage and will be gentler on the bandwidth.

5. Can scapy be used to send other types of packets? If yes, give an example.
- Yes, such as an ICMP packet by assigning a variable to ICMP() and then accessing its methods with dot notation to modify the values accordingly.
