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

    # base API string for weather.gov
    weather_s = "https://api.weather.gov/points/"

    # sys.argv[1] gives us the command line input
    # sys.argv[0] is the name of the python file
    print(weather_s + argv[1])

    # use the commandline input and the weather_s to make API call
    response = get(weather_s + argv[1])

    # convert it to json
    js = loads(response.text)

    # find the forecast URL based on the API page
    forecast_URL = js["properties"]["forecastHourly"]

    # print link that we use for next API call
    print(forecast_URL)

    # call the API again to get theforecast
    final_response = get(forecast_URL)

    # parse json
    js = loads(final_response.text)

    tempList = []
    for i in range(7):
        tempList.append(js["properties"]["periods"][i]["temperature"])

    # print the list to check against graph
    print(tempList)

    # do actual plotting
    plot_temps(tempList)


if __name__ == "__main__":
    main()
