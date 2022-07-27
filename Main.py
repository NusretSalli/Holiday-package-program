
import os, sys

import requests

import json

import pandas as pd

import numpy as np

import time as timer

from displayMenu import displayMenu

from Weather import Weather # the Weather API function

from inputverifier import inputNumber

from termcolor import colored

import pickle


###----------------------------------------------- HOLIDAY STUFF PACKAGES --------------------------------------------------###

#------------------------------------------------- Essential Package ---------------------------------------------------------#

# our must have list

must_have = ["Toothbrush", "Toothpaste", "Deodorant", "Medicine", "Hair Brush", "Tampons", "Shampoo", "Insurance", "wallet"]

# we make a dataframe out of it with a single column.

must_have_dataframe = pd.DataFrame(must_have)

# nice to have list

nice_to_have = ["First aid", "Vaseline", "Condoms", "Make up", "Student-ID"]

# nice to have dataframe

nice_to_have_dataframe = pd.DataFrame(nice_to_have)

# longer stays list

longer_stays = ["Shaving equipments", "Nail cutter"]

# longer stays dataframe

longer_stays_dataframe = pd.DataFrame(longer_stays)

# abroad list

abroad = ["Passport", "Health insurance"]

# abroad dataframe

abroad_dataframe = pd.DataFrame(abroad)

# we concatenate all the different dataframes into a single, big one.

essential_package = pd.concat([must_have_dataframe, nice_to_have_dataframe, longer_stays_dataframe, abroad_dataframe], ignore_index=True, axis=1)

# we rename the column names to something appropriate

essential_package.columns = ["Must have | ", " Nice to have | ", "Longer stays | ", "Abroad |",]

not_abroad_package = essential_package[["Must have | ", " Nice to have | ", "Longer stays | "]]

# ------------------------------------------------------- Skiing Package -----------------------------------------------------#


# ------------------------------------------------------- Camping Package ----------------------------------------------------#



### ----------------------------------------------------- SAVED PACKGAGES --------------------------------------------------###

stored_package = {}

stored_package = pickle.load( open("SavedPackage.p", "rb"))

if(len(stored_package) == 0):

    saved_package_dict = {"Hello":"Hello1", "Marie":"Marie2", "Nus":"Nus2"}

    saved_manipulation = {"Back to main menu": "Back"}

    saved_package_dict.update(saved_manipulation)

    saved_package_menu = saved_package_dict

else:

    saved_package_dict = stored_package

    saved_package_menu = saved_package_dict



###------------------------------------------------------- MENU ------------------------------------------------------------###

while True:

    print("------------------------------", colored("Please choose one of the options", "green"), "---------------------------------------------------")

    main_menu = np.array(["New holiday", "Saved holiday packages", "Quit"])

    choice = displayMenu(main_menu)

    if(choice == 1): # if the user picks a new holiday option

        print("---------------------------", colored("What type of holiday is it?", "green"),"--------------------------------------------------")

        holiday_menu = np.array(["Basic holiday", "Skiing holiday", "Camping holiday", "Custom Holiday", "Back to main menu"])

        holiday_choice = displayMenu(holiday_menu)


        if(holiday_choice == 1): # if the holiday is basic 

             # Ask for how long the holiday will last

            number_of_days = int(input(colored(" How long is your holiday in days? ", "yellow")))

            # now ask wether the holiday is abroad, not abroad or both

            print("-------------------------------", colored("Where is the holiday located?", "green"),"--------------------------------------")

            holiday_location_menu = np.array(["Abroad,", "Not abroad", "Both"])

            holiday_location_choice = displayMenu(holiday_location_menu)

            if(holiday_location_choice == 1): # if the holiday is abroad

                # asking for the location the holiday will take place

                location = str(input("Please type in the city and country as this: city, countrycode: "))

                weather_reports = Weather(location)

                print(essential_package)

                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = np.array(["Save the package", "Edit the package", "Save it in a CSV-file", "Nothing, go back to main menu"])

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package

                    package_name = str(input("What should the package be called?: "))

                    new_package_dict = {package_name: essential_package, "Back to main menu": "Back"}

                    del saved_package_dict["Back to main menu"]

                    saved_package_dict.update(new_package_dict)

                    print("\nThe package called " + package_name + " has been saved\n")


                if(package_given_choice == 2): # if the user wants to edit the package

                    placeholder = 2

                
                if(package_given_choice == 3): # if the user wants to save the package in a CSV-file

                    placeholder = 2


            if(holiday_location_choice == 2): # if the holiday is not abroad

                # Asking for the location the holiday will take place

                location = str(input("Please type in the city and country as this: city, countrycode: "))

                weather_reports = Weather(location)

                print(not_abroad_package)

                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = np.array(["Save the package", "Edit the package", "Save it in a CSV-file", "Nothing, go back to main menu"])

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package

                    package_name = str(input("What should the package be called?: "))

                    new_package_dict = {package_name: essential_package, "Back to main menu": "Back"}

                    del saved_package_dict["Back to main menu"]

                    saved_package_dict.update(new_package_dict)

                    print("\nThe package called " + package_name + " has been saved\n")


                if(package_given_choice == 2): # if the user wants to edit the package

                    placeholder = 2

                
                if(package_given_choice == 3): # if the user wants to save the package in a CSV-file

                    placeholder = 2
                


            if(holiday_location_choice == 3): # if the holiday is both abroad and not abroad.

                placeholder = 2


    if(choice == 2): # if the user picks saved holiday packages

        saved_package_list = list(saved_package_menu.keys())

        if(len(saved_package_list) == 1):

            print(colored("\nError - no saved packages", "red", attrs=["bold"]))

        else:

            saved_package_choice = displayMenu(saved_package_list)


            if(saved_package_choice != saved_package_list.index("Back to main menu")+1): # if the user chooses one of the packages
                
                selected_key = str(saved_package_list[int(saved_package_choice-1)])


                print(colored("\nCurrent package: " + selected_key + "\n", "blue"))

                package_menu = ["View the package", "Edit the package", "Delete the package", "Back to main menu"]

                package_menu_choice = displayMenu(package_menu)

                if(package_menu_choice == 1): # if the user wants to view the package

                    # we extract the value stored in the key, that has been selected.

                    desired_package = saved_package_dict[selected_key]

                    print(desired_package)

                
                if(package_menu_choice == 2): # if the user wants to edit the package

                    placeholder = 2


                if(package_menu_choice == 3): # if the user wants to delete the package

                    confirmation = str(input(colored(" Are you sure you want permenantely want to delete the package: " + selected_key + " ? \nType yes if you are sure ", "yellow")))

                    if(confirmation.lower() == "yes"): # if the user really wants to delete the package

                        del saved_package_dict[selected_key]

                        print(colored("\nThe package " + selected_key + " has been permenantely deleted", "yellow"))




    if(choice == 3):

        print(colored("\nHave a great day!", "yellow"))

        break


# saving the saved_package list for later use just like IRL

stored_package = pickle.dump(saved_package_dict, open("SavedPackage.p", "wb"))
