import os, sys

import requests

import json

import pandas as pd

import numpy as np

import time as timer


### MAYBE WE CAN USE PYOWM TO MAKE IT VERY NICE? ###

def Weather(location):

    ##------------------------------------------- DESCRIPTION OF THE FUNCTION -----------------------------------------------## 
    
    # Purpose: extracts all the data that concerns weather for a given location
        
    # Input: Location -> a text string, which has the format "city, country"
        
    # Output: not sure yet -> it can be anything really.


    ##----------------------------------------------- FUNCTION IMPLEMENTATION -----------------------------------------------##

    # the API-key we need to use

    api_key = "4f5ae53c38b5b3cb828838011e3bf60c"

    # we'll have to use the direct geocoding API to get a lattitude and longitude value for a given location

    geo_coordinates = "http://api.openweathermap.org/geo/1.0/direct?q=%s&limit=1&appid=%s" % (location, api_key)

    geo_value = requests.get(geo_coordinates)

    geo_data = json.loads(geo_value.text)

    # we have to extact the lattitude and longitude coordinates - it is a list with a single element - thus 0 in the first index

    lat = geo_data[0]["lat"]

    lon = geo_data[0]["lon"]

    # our URL that makes the call - we have the lattitude and longitude, and thus get all the information we need

    URL = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

    # we use the request-package to get the call.

    response = requests.get(URL)

    # we load the JSON data from the call.

    data = json.loads(response.text)

    # we now take look at the forecast, which is the next 8 days.

    daily = data["daily"]

    # we'll make a for loop that will extract the UNIX-time which we need for our historical weather data

    time_list = []

    for i in range(0,8):

        time = daily[i]["dt"]

        time_list.append(time)

    
    ###---------------------------------------------- HISTORICAL DATA ----------------------------------------------------###

    # we make a for loop that loops through each UNIX-timestamp and look for the temperatures the past 10 years (if that was possible).

    #unix_days = 86400

    #dataframe_historical = pd.DataFrame()


    #for i in range(0,8):

        #for j in range(1,10):

            #history_url = "http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=%s&lon=%s&dt=%s&appid=%s&units=metric" % (lat, lon, time_list[i]-j*unix_days, api_key)

            #history_response = requests.get(history_url)

            #history_data = json.loads(history_response.text)

            #dataframe_historical = dataframe_historical.append(history_data["current"], ignore_index=True)


    ###--------------------------------------------- OUTPUT-CONSTRUCTION -------------------------------------------------###

    # we construct our dataframes for each important "element" we want to consider #

    dataframe_temp = pd.DataFrame()

    dataframe_feels_like = pd.DataFrame()

    humidity_list = []

    dataframe_weather = pd.DataFrame()


    # for loop that iterates through each forecasted days (8 days)

    for i in range(0,8):

        # extract each factor for a given forecasted day

        temp = daily[i]["temp"] # a dictionary with a total of 6 elements

        humidity = daily[i]["humidity"] # integer

        feels_like = daily[i]["feels_like"] # a dictionary with a total of 4 elements

        weather = daily[i]["weather"] # a dictionary with a total of 4 elements. 

        # we append these values to their respective dataframe by row

        dataframe_temp = dataframe_temp.append(temp, ignore_index = True)

        dataframe_feels_like = dataframe_feels_like.append(feels_like, ignore_index = True)

        humidity_list.append(humidity)

        dataframe_weather = dataframe_weather.append(weather, ignore_index = True)

    return(dataframe_temp)




### STUFF TO DO ###

# Get day data and maybe maximum for temp and feels_like

# get weather data more precisely - odds of rain, snow and the amount of rain and snow.


