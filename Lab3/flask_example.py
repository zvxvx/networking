# author: Greg Pappas

from flask import Flask
from json import loads
from requests import get
from socket import gethostbyname
from subprocess import getstatusoutput


app = Flask(__name__)

addressCache = {}
weatherCache = {}
rangeCache = {}


@app.route(f"/address/<domain>")
def address(domain):
    if addressCache.get(domain) != None:
        return addressCache.get(domain)

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

    final = f"{address}, {city}, {state}, {zip}\n"
    addressCache.update({domain: f"Cached: {final}"})
    return final


@app.route("/weather/<domain>")
def weather(domain):
    if weatherCache.get(domain) != None:
        return weatherCache.get(domain)

    addressLine = address(domain)
    weatherAdd = f"https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={addressLine}&benchmark=4&format=json"

    response = get(weatherAdd)
    js = loads(response.text)

    if js["result"]["addressMatches"] == []:
        # I decided not to cache this response in case weather information does get added at any point in time, and when it does, it will be cached accordingly.
        return "Domain does not provide sufficent data to get weather information. Try a different domain.\n"

    x = js["result"]["addressMatches"][0]["coordinates"]["x"]
    y = js["result"]["addressMatches"][0]["coordinates"]["y"]

    weather_s = f"https://api.weather.gov/points/{y},{x}"
    response = get(weather_s)
    js = loads(response.text)

    forecast = js["properties"]["forecast"]
    response = get(forecast)
    js = loads(response.text)

    currentForecast = js["properties"]["periods"][0]["detailedForecast"] + "\n"

    weatherCache.update({domain: f"Cached: {currentForecast}"})
    return currentForecast


@app.route("/range/<domain>")
def range(domain):
    if rangeCache.get(domain) != None:
        return rangeCache.get(domain)

    host = gethostbyname(domain)
    status, output = getstatusoutput(f"whois {host}")
    splitted = output.splitlines()
    netRange = ""

    for line in splitted:
        if line.startswith("NetRange"):
            netRange = (
                f"Network range for {domain} is {line.partition("NetRange")[2][1:].strip()}\n"
            )

    rangeCache.update({domain: f"Cached: {netRange}"})
    return netRange


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
