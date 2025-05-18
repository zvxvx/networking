#!/bin/bash
sudo iptables -I OUTPUT -p tcp --tcp-flags ALL RST -j DROP
sudo python3 lab6.py http://httpforever.com/
sudo python3 lab6.py http://http-password.badssl.com/
sudo python3 lab6.py http://example.com/
sudo iptables -D OUTPUT -p tcp --tcp-flags ALL RST -j DROP
