
import requests # used for weather API

import json # used for  weather API

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

### ----------------------------------------------------- SAVED PACKGAGES --------------------------------------------------###

# we create our saved / stored package

stored_package = {}

# we load the stored_package saved in the SavedPackage.p

stored_package = pickle.load( open("SavedPackage.p", "rb"))

if(len(stored_package) == 0): # if the stored_package is empty

    saved_package_dict = {}

    saved_manipulation = {"Back to main menu": "Back"}

    saved_package_dict.update(saved_manipulation)

    saved_package_menu = saved_package_dict

else: # if the stored package is not empty

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

            # Now ask wether the holiday is abroad, not abroad or both

            print("-------------------------------", colored("Where is the holiday located?", "green"),"--------------------------------------")

            holiday_location_menu = np.array(["Abroad,", "Not abroad", "Both"])

            holiday_location_choice = displayMenu(holiday_location_menu)


            if(holiday_location_choice == 1): # if the holiday is abroad

                # asking for the location the holiday will take place

                location = str(input("Please type in the city and country as this: city, countrycode: "))


                # using the weather API to get the relevant data

                weather_reports = Weather(location)

                # we print the essential package for abroad

                print(PackageCreation.essentialCreation("ABROAD"))

                # we ask what the user wants to do with the given package

                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = np.array(["Save the package", "Edit the package", "Save it in a CSV-file", "Nothing, go back to main menu"])

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package
                    
                    # we ask the user for its name

                    package_name = str(input("What should the package be called?: "))

                    new_package_dict = {package_name: PackageCreation.essentialCreation("ABROAD"), "Back to main menu": "Back"}

                    # we delete the key "back to main menu" and its value to put it at the end every time a new package is saved

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

                # using the weather API to get the relevant data

                weather_reports = Weather(location)

                # print the essential package when it is NOT ABROAD

                print(PackageCreation.essentialCreation("NOT ABROAD"))

                # We ask what the user wants to do with the package

                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = np.array(["Save the package", "Edit the package", "Save it in a CSV-file", "Nothing, go back to main menu"])

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package

                    package_name = str(input("What should the package be called?: "))

                    new_package_dict = {package_name: PackageCreation.essentialCreation("NOT ABROAD"), "Back to main menu": "Back"}

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

        # if there are saved packages, then it will be displayed.

        saved_package_list = list(saved_package_menu.keys())

        if(len(saved_package_list) == 1): # checking if we have any saved packages

            print(colored("\nError - no saved packages", "red", attrs=["bold"]))

        else:

            saved_package_choice = displayMenu(saved_package_list)

            # if the user chooses one of the packages
            
            if(saved_package_choice != saved_package_list.index("Back to main menu")+1):
                
                # we store the key that has been selected by the user

                selected_key = str(saved_package_list[int(saved_package_choice-1)])

                print(colored("\nCurrent package: " + selected_key + "\n", "blue"))

                # we ask the user what to do with the chosen saved package

                package_menu = ["View the package", "Edit the package", "Delete the package", "Back to main menu"]

                package_menu_choice = displayMenu(package_menu)

                if(package_menu_choice == 1): # if the user wants to view the package

                    # we extract the value stored in the key, that has been selected.

                    desired_package = saved_package_dict[selected_key]

                    print(desired_package)

                
                if(package_menu_choice == 2): # if the user wants to edit the package

                    placeholder = 2


                if(package_menu_choice == 3): # if the user wants to delete the package
                    
                    # we make a confirmation that the user wants to delete the chosen saved package

                    confirmation = str(input(colored(" Are you sure you want permenantely want to delete the package: " + selected_key + " ? \nType yes if you are sure ", "yellow")))

                    if(confirmation.lower() == "yes"): # if the user really wants to delete the package

                        del saved_package_dict[selected_key]

                        print(colored("\nThe package " + selected_key + " has been permenantely deleted", "yellow"))




    if(choice == 3): # if the user wants to exit the program

        print(colored("\nHave a great day!", "yellow"))

        break


# saving the saved_package list for later use just like IRL

stored_package = pickle.dump(saved_package_dict, open("SavedPackage.p", "wb"))
