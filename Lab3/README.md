# lab3

### Completed by Greg Pappas

## Setup

#### Run the following in the terminal.

- `python3 flask_example.py`

## Usage:

#### Run the following in the terminal.

- `curl http://127.0.0.1:5000/<endpoint>/<domain>`

## Examples:

#### Run the following in the terminal.

- `curl http://127.0.0.1:5000/address/google.com`
- `curl http://127.0.0.1:5000/range/google.com`
- `curl http://127.0.0.1:5000/weather/google.com`

## Program description

This program provides three endpoint API calls via a flask server.

- **Address**, which provides the physical location of the IP address belonging to the domain name.
- **Range**, which lists the IP address range of the domain name.
- **Weather**, which provides detailed weather of the current forecast where the IP address is physically located.

## Questions

1. Identify the following in the URL: http://localhost:5000/weather/google.com
-  Domain: google
-  Path: /weather/google.com
-  Port: 5000
-  Protocol: http

2. Identify the following in the URL: https://translate.google.com/
- Domain: google
- Subdomain: translate
- TLD: .com
- Path: /
- Protocol: https
- Port: 443

3. What is a Python decorator?

- It is a function that takes a function in as an argument to add additional functionality without modifying the function used as an argument.

4. Is there any problem with your cache implementation? Would your cache implementation work in production?

- It would work, but in production, it is standard to have cache expire after a certain period to update potentially state results. My implementation does not have cache that expires.
