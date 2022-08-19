import os, sys

import requests

import json

import pandas as pd

import numpy as np

import datetime

import weather_map # our weather_map function

def Weather(location, map):

    ##------------------------------------------- DESCRIPTION OF THE FUNCTION -----------------------------------------------## 
    
    # Purpose: extracts all the data that concerns weather for a given location
        
    # Input: Location -> a text string, which has the format "city, country"
        
    # Output: not sure yet -> it can be anything really.


    ##----------------------------------------------- FUNCTION IMPLEMENTATION -----------------------------------------------##

    # the API-key we need to use

    api_key = "4f5ae53c38b5b3cb828838011e3bf60c"

    if(map == "MAP" and location == "NO INPUT"):

        coordinates = weather_map.map_creator() # [lat, lon] values

        URL = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (coordinates[0], coordinates[1], api_key)

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

            converted_time = datetime.datetime.fromtimestamp(time)

            time_list.append(converted_time.strftime("%Y-%m-%d"))

        
        ###---------------------------------------------- HISTORICAL DATA ----------------------------------------------------###

        # we make a for loop that loops through each UNIX-timestamp and look for the temperatures the past year (if that is possible).
        #unix_days = 86400
        #dataframe_historical = pd.DataFrame()


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

    else:

        # we'll have to use the direct geocoding API to get a lattitude and longitude value for a given location

        geo_coordinates = "http://api.openweathermap.org/geo/1.0/direct?q=%s&limit=1&appid=%s" % (location, api_key)

        geo_value = requests.get(geo_coordinates)

        geo_data = json.loads(geo_value.text)

        # we have to extact the lattitude and longitude coordinates - it is a list with a single element - thus 0 in the first index

        lat = geo_data[0]["lat"]

        lon = geo_data[0]["lon"]

        # our URL that makes the call - we have the lattitude and longitude, and thus get all the information we need

        URL = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

        URL2 = "https://pro.openweathermap.org/data/2.5/forecast/climate?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

        # we use the request-package to get the call.

        response = requests.get(URL2)

        # we load the JSON data from the call.

        data = json.loads(response.text)

        # we now take look at the forecast, which is the next 30 days.

        daily = data["list"]

        
        ## --------------------------------------------- Creating our date -----------------------------------------------##

        time_list = [] # list that will contain our date

        for i in range(0,30): # loop through each UNIX-timestamp

            time = daily[i]["dt"] # extracting the time

            converted_time = datetime.datetime.fromtimestamp(time) # convert it to date

            time_list.append(converted_time.strftime("%d/%m/%Y")) # Only appending the day/month/year

        
        ## ------------------------------ List of all the values we want to extract ------------------------------------------- ##
        
        humidity_list = []

        day_list = []

        min_list = []

        max_list = []

        eve_list = []

        day_feels_like_list = []

        min_feels_like_list = []

        max_feels_like_list = []

        eve_feels_like_list = []

        weather_list = []


        # for loop that iterates through each forecasted days (30 days)

        for i in range(0,30):

            # extract each factor for a given forecasted day

            temp = daily[i]["temp"] # a dictionary with a total of 6 elements

            day_list.append(temp["day"]) # appending the day-temperature to our list

            min_list.append(temp["min"]) # appending the min-temperature to our list

            max_list.append(temp["max"]) # appending the max-temperature to our list

            eve_list.append(temp["eve"]) # appending the evening-temperature to our list


            feels_like = daily[i]["feels_like"] # a dictionary with a total of 4 elements

            feels_like_list = list(feels_like.values()) # make a list of all the values in the dictionary used for max and min

            day_feels_like_list.append(feels_like["day"]) # appending the day-temperature to our list

            min_feels_like_list.append(min(feels_like_list)) # finding the min value from our feels_like_list

            max_feels_like_list.append(max(feels_like_list)) # finding the max value from our feels_like_list

            eve_feels_like_list.append(feels_like["eve"]) # appending the evening-temperature to our list


            humidity = daily[i]["humidity"] # integer

            humidity_list.append(humidity) # Appending the humidity-value into the list


            weather = daily[i]["weather"] # a dictionary with a total of 4 elements.

            weather_list.append(weather[0]["description"]) # we get the weather condition from our weather variable

    
    # constructing our entire dictionary that will be turned into a dataframe

    whole_data = {
        "day": day_list,
        "min": min_list,
        "max": max_list,
        "evening": eve_list,
        "humidity (%)": humidity_list, 
        "Weather condition": weather_list,
        "Date": time_list}

    data_dataframe = pd.DataFrame(whole_data) # Constructing our dataframe

    data_dataframe = data_dataframe.set_index("Date") # our index becomes our date

    return(data_dataframe.to_markdown())

#print(Weather("London, GB", "NO MAP"))


### STUFF TO DO ###

# Get day data and maybe maximum for temp and feels_like

# get weather data more precisely - odds of rain, snow and the amount of rain and snow.

