#! /usr/bin/bash

echo "TEST 1: python3 lab4.py -p 80 http://httpforever.com/"
python3 lab4.py -p 80 http://httpforever.com/
echo
echo "TEST 2: python3 lab4.py -f 80 http://httpforever.com/"
python3 lab4.py -f 80 http://httpforever.com/
echo 
echo "TEST 3: python3 lab4.py -p 80 http://httpforever.com/login/"
python3 lab4.py -p 80 http://httpforever.com/login/
