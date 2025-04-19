# author: Greg Pappas

from flask import Flask
from json import loads
from requests import get
from socket import gethostbyname
from subprocess import getstatusoutput


app = Flask(__name__)


@app.route(f"/address/<domain>")
def address(domain):
    host = gethostbyname(domain)
    status, output = getstatusoutput(f"whois {host}")
    splitted = output.splitlines()

    city = ""
    address = ""
    state = ""
    zip = ""

    for line in splitted:
        if line.startswith("City"):
            city = line.partition("City")[2][1:].strip()
        elif line.startswith("Address"):
            address = line.partition("Address")[2][1:].strip()
        # this is used for select websites.
        elif line.startswith("StateProv"):
            state = line.partition("StateProv")[2][1:].strip()
        elif line.startswith("State"):
            state = line.partition("State")[2][1:].strip()
        elif line.startswith("PostalCode"):
            zip = line.partition("PostalCode")[2][1:].strip()

    final = address + ", " + city + ", " + state + ", " + zip
    return final


@app.route("/weather/<domain>")
def weather(domain):
    addressLine = address(domain)
    weatherAdd = f"https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={addressLine}&benchmark=4&format=json"

    response = get(weatherAdd)
    js = loads(response.text)

    if js["result"]["addressMatches"] == []:
        return "Domain does not provide sufficent data to get weather information. Try a different domain."

    x = js["result"]["addressMatches"][0]["coordinates"]["x"]
    y = js["result"]["addressMatches"][0]["coordinates"]["y"]

    weather_s = f"https://api.weather.gov/points/{y},{x}"
    response = get(weather_s)
    js = loads(response.text)

    forecast = js["properties"]["forecast"]
    response = get(forecast)
    js = loads(response.text)

    currentForecast = js["properties"]["periods"][0]["detailedForecast"]
    return currentForecast


@app.route("/range/<domain>")
def range(domain):
    host = gethostbyname(domain)
    status, output = getstatusoutput(f"whois {host}")
    splitted = output.splitlines()

    for line in splitted:
        if line.startswith("NetRange"):
            return f"Network range for {domain} is" + line.partition("NetRange")[2][1:]


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
