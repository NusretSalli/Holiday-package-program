
import os, sys

import requests

import json

import pandas as pd

import numpy as np

import time as timer

import tkinter

import tkintermapview


import requests # used for weather API

import json # used for  weather API

import math

import pandas as pd

import numpy as np

import tabulate # to customize the pandas dataframe even more and look cleaner

import time as timer

from displayMenu import displayMenu # menu-creator function

#from Weather import Weather # the Weather API function

#from weather_map import map_creator

from inputverifier import inputNumber # function that makes sure type in a valid option

from termcolor import colored # to give colorful messages to the terminal

import pickle # to store the saved packages 

import PackageCreation # the package-organizer function

import tkinter

import tkintermapview



def map_creator():

    coordinates = []

    # create tkinter window

    root_tk = tkinter.Tk()

    root_tk.geometry(f"{1200}x{1200}") # Size of the Tkinter-window

    root_tk.title("mapper") # Name of the Tkinter-window

    # creating the map on our window

    map = tkintermapview.TkinterMapView(root_tk, width=1200, height=1200, corner_radius=0) # size of the map

    #map.pack(fill="both", expand=True)

    map.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) # the placement of the map

    # set current widget position and zoom

    map.set_position(55.7687725, 10.2956985)  # Denmark

    map.set_zoom(7) # our current zoom-level

    def add_marker(coords):

        # Function that will store the coordinates when clicked and make a marker on the map

        if(len(coordinates) == 0): # checking if we have placed a marker or not

            marker = map.set_marker(coords[0], coords[1])

            coordinates.append(coords[0])

            coordinates.append(coords[1])

        else: # If we already have a marker we update it (SOMEHOW HAVE TO REMOVE THE LAST MARKER AND PLACE A NEW ONE, BUT DOESN'T WORK)

            coordinates[0] = coords[0]

            coordinates[1] = coords[1]

    def left_click_event(coordinates_tuple):

        # Function that will call the add_marker function whenever the person makes a left-click

        if(len(coordinates) != 0): # if the marker exists, we simply ignore it - otherwise we actually call the function

            pass

        else:

            add_marker(coordinates_tuple)

    map.add_left_click_map_command(left_click_event) # We implement the command

    root_tk.mainloop() # We "terminate" the Tkinter-window

    return(coordinates) # We return the latitude and longitude from our list, respectively


#print(map_creator())

#counter = 0

#while True:

    #print("------------------------------", colored("Please choose one of the options", "green"), "---------------------------------------------------")

    #main_menu = ["New holiday", "Saved holiday packages", "Quit"] # we give the user the overall options

    #choice = displayMenu(main_menu)

    
