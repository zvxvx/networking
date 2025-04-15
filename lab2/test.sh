#! /usr/bin/bash
url1="google.com"
url2="mit.edu"
url3="ewu.edu"

echo "TEST 1 ($url1)"
echo "When graph has loaded, close graph window to proceed to next test."
echo `./lab2.py $url1`

echo "TEST 2 ($url2)"
echo "When graph has loaded, close graph window to proceed to next test."
echo `./lab2.py $url2`

echo "TEST 3 ($url3)"
echo "When graph has loaded, close the window to conclude the testing."
echo `./lab2.py $url3`
