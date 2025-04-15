#! /usr/bin/env python3
# author: Greg Pappas

from sys import argv  # command line arguments
from socket import gethostbyname  # step 1
from subprocess import getstatusoutput  # step 2
from json import loads  # steps 3, 4
from requests import get  # steps 3, 4
import matplotlib.pyplot as plt  # for temp plotting function
import numpy as np  # for temp plotting function


# Takes an array of temps
# and plots them.
def plot_temps(temps):
    xs = [x for x in range(len(temps))]
    plt.plot(xs, temps, label="Hourly tempatures")

    # Label the x and y
    plt.xlabel("Hour")
    plt.ylabel("Temperature F.")
    # Make sure we show the legend.
    plt.legend()
    # Show the plot
    plt.show()


def main():
    # TODO: Look at the code below for an example of how to do
    # API calls. I would recommend first uncommenting and
    # understanding the code, and then commenting the code back
    # out. The code is, largely, step 4.

    # Use cl argument to get ip
    ip = gethostbyname(argv[1])

    # generate output from running bash command in python.
    s, o = getstatusoutput(f"whois {ip}")

    # print exit code, because why not?!
    print(f"Output status code: {s}")

    # break up the output by splitting on newline.
    # this allows us to loop through and work with each line
    splitted = o.split("\n")

    # initialize variables for collect address data
    city = ""
    address = ""
    state = ""
    zip = ""

    # run a loop over the splitted output and use if else
    # structure to isolate lines and assign them to variables.
    # spacing is absolute with the whois output fortunately,
    # so splitting is possible with the following method.
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
    # format initial url with variables integrated
    weatherAdd = f"https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={address},{city},{state},{zip}&benchmark=4&format=json"

    print(weatherAdd)
    # perform a get request on weatherAdd
    response = get(weatherAdd)

    # convert to get request to JSON
    js = loads(response.text)

    # drill down the object for the x,y coords.
    # some URLs do not have weather data available.
    # so an exception is thrown.
    if js["result"]["addressMatches"] == []:
        raise Exception(
            "Domain does not provide sufficent data to get weather information. Try a different domain."
        )
    x = js["result"]["addressMatches"][0]["coordinates"]["x"]
    y = js["result"]["addressMatches"][0]["coordinates"]["y"]

    # API string for weather.gov with coords baked in.
    weather_s = f"https://api.weather.gov/points/{y},{x}"

    # print coords link
    print(weather_s)

    # run a get request on the weather coords.
    response = get(weather_s)

    # convert it to json
    js = loads(response.text)

    # find the hourly forecast URL based on the API page
    forecast_URL = js["properties"]["forecastHourly"]

    # print link that we use for next API call
    print(forecast_URL)

    # call the API again to get theforecast
    final_response = get(forecast_URL)

    # parse json
    js = loads(final_response.text)

    # get temps from the last 4 days
    tempList = []
    for i in range(96):
        tempList.append(js["properties"]["periods"][i]["temperature"])

    # print the list to check against graph to compare values if desired. commented out by default
    # print(f"Weather data: {tempList}")

    # do actual plotting
    plot_temps(tempList)


if __name__ == "__main__":
    main()
