# Lab 7

### Completed by Greg Pappas

## Setup

Users will need to install [scapy](https://scapy.net/) in order to use the program.

## Usage:

#### sudo is required to run this program.

- `sudo python3 lab7.py <domain> <hops>`

### domain

Must type domain without prepending `https://` to the domain and without an ending `/`.
`example.com` will work while `https://example.com/` will not work.

- Example: `sudo python3 lab7.py https://google.com/ 30` will _not_ work.
- However, `sudo python3 lab7.py google.com 30` _will_ work

## Examples:

- `sudo python3 lab7.py google.com 20`
- `sudo python3 lab7.py example.com 30`
- `sudo python3 lab7.py npr.org 15`

## Program description

This program works similarly to `traceroute`, but sends tcp syn packets by default. It also tracks the AS numbers provided by each resolvable hop.

## Questions

1. Besides TCP, what other protocols can be used for a traceroute tool?

- ICMP, GRE, SCTP, UDP are all possible to be used.

2. When traversing to a website, does the path remain constant every time?

- No, it can change based on dynamic routing, CDNs, hardware failures, and ISP traffic.

3. If a packet dies before reaching the target website, what type of packet is
   returned?

- A type 11: time exceeded ICMP message.

4. Can the whois command be used to discover the owner of an AS number?

- Yes. by running the following example `whois AS10594`
