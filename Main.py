
import requests # used for weather API

import json # used for  weather API

import math

import pandas as pd

import numpy as np

import tabulate # to customize the pandas dataframe even more and look cleaner

import time as timer

from displayMenu import displayMenu # menu-creator function

from Weather import Weather # the Weather API function

from inputverifier import inputNumber # function that makes sure type in a valid option

from termcolor import colored # to give colorful messages to the terminal

import pickle # to store the saved packages 

import PackageCreation # the package-organizer function

from edit_package import edit_package

from save_package import save_package # our save_package function

from Holidayque import basic_holiday, ski_holiday, camping_holiday

from excel_saver import excel_saver


### ----------------------------------------------------- SAVED PACKGAGES --------------------------------------------------###

# we create our saved / stored package

stored_package = {}

# we load the stored_package saved in the SavedPackage.p

stored_package = pickle.load( open("SavedPackage.p", "rb"))

if(len(stored_package) == 0): # if the stored_package is empty

    saved_package_dict = {} # we make our empty dictionary

    saved_manipulation = {"Back to main menu": "Back"} # put back to main menu option to use

    saved_package_dict.update(saved_manipulation)

    saved_package_menu = saved_package_dict

else: # if the stored package is not empty

    saved_package_dict = stored_package 

    saved_package_menu = saved_package_dict

###------------------------------------------------------- MENU ------------------------------------------------------------###

while True:

    print("------------------------------", colored("Please choose one of the options", "green"), "---------------------------------------------------")

    main_menu = ["New holiday", "Saved holiday packages", "Quit"] # we give the user the overall options

    choice = displayMenu(main_menu)

    if(choice == 1): # if the user picks a new holiday option

        print("---------------------------", colored("What type of holiday is it?", "green"),"--------------------------------------------------")

        holiday_menu = (["Basic holiday", "Skiing holiday", "Camping holiday", "Custom Holiday", "Back to main menu"]) # Options when it comes to holidays 

        holiday_choice = displayMenu(holiday_menu)

        if(holiday_choice == 1): # if the holiday is basic 

            basic_holiday(saved_package_dict)
        
        if(holiday_choice == 2): # if the user picks skiing holiday

            ski_holiday(saved_package_dict)


        if(holiday_choice == 3): # if the user picks camping holiday

            camping_holiday(saved_package_dict)

    

    # TODO - implement an option to save your saved package in an excel file.

    if(choice == 2): # if the user picks saved holiday packages

        saved_package_list = list(saved_package_menu.keys()) # if there are saved packages, then it will be displayed.

        if(len(saved_package_list) == 1): # checking if we have any saved packages

            print(colored("\nError - no saved packages", "red", attrs=["bold"]))

        else:

            saved_package_choice = displayMenu(saved_package_list)

            
            if(saved_package_choice != saved_package_list.index("Back to main menu")+1): # if the user chooses one of the packages

                selected_key = str(saved_package_list[int(saved_package_choice-1)]) # we store the key that has been selected by the user

                print(colored("\nCurrent package: " + selected_key + "\n", "blue"))

                # we ask the user what to do with the chosen saved package

                package_menu = ["View the package", "Edit the package", "Save the package in an excel file", "Delete the package", "Back to main menu"]

                package_menu_choice = displayMenu(package_menu)

                if(package_menu_choice == 1): # if the user wants to view the package

                    desired_package = saved_package_dict[selected_key] # we extract the value stored in the key, that has been selected.

                    print(desired_package.to_markdown())

                
                if(package_menu_choice == 2): # if the user wants to edit the package

                    selected_dataframe = saved_package_dict[selected_key]

                    edit_package(selected_dataframe) # using our edit_package function
                
                if(package_menu_choice == 3): # if the user wants to save the package in an excel-file

                    selected_dataframe = saved_package_dict[selected_key]

                    # TODO - FIX THIS EXCEL SAVER - DOESN'T RUN RIGHT NOW

                    excel_saver(selected_dataframe)
                    
                if(package_menu_choice == 4): # if the user wants to delete the package
                    
                    # we make a confirmation that the user wants to delete the chosen saved package

                    confirmation = str(input(colored(" Are you sure you want permenantely want to delete the package: " + selected_key + " ? \nType yes if you are sure ", "yellow")))

                    if(confirmation.upper() == "YES"): # if the user really wants to delete the package

                        del saved_package_dict[selected_key]

                        print(colored("\nThe package " + selected_key + " has been permenantely deleted", "yellow"))


    if(choice == 3): # if the user wants to exit the program

        print(colored("\nHave a great day!", "yellow"))

        break


# saving the saved_package list for later use just like IRL

stored_package = pickle.dump(saved_package_dict, open("SavedPackage.p", "wb"))
