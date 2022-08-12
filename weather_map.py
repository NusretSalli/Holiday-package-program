
import os, sys

import requests

import json

import pandas as pd

import numpy as np

import time as timer

import folium

import tkinter

import tkintermapview


## MAYBE SOMETHING THAT WE WILL BE WORKING ON?

def weather_map():

    ##------------------------------------------- DESCRIPTION OF THE FUNCTION -----------------------------------------------## 
    
    # Purpose: Gives out a weather map of the said location and its surrounding area. 
        
    # Input: Location -> a text string, which has the format "city, country"
        
    # Output: a weather map of the given location and its surrounding area

    ##----------------------------------------------- FUNCTION IMPLEMENTATION -----------------------------------------------#

    # create tkinter window
    placeholder = 2


# create tkinter window
root_tk = tkinter.Tk()

root_tk.geometry(f"{800}x{600}")

root_tk.title("weather_map.py")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)

map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

map_widget.pack()

root_tk.mainloop()