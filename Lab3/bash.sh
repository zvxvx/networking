#! /bin/bash

url="ewu.edu"

echo "TEST 1"
curl `http://localhost:5000/address/$url`
echo "Cached version"
curl `http://localhost:5000/address/$url`

