
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

            # Ask for how long the holiday will last

            number_of_days = int(input(colored(" How long is your holiday in days? ", "yellow"))) # we ask the number of days the holiday last

            # Now ask wether the holiday is abroad, not abroad or both

            print("-------------------------------", colored("Where is the holiday located?", "green"),"--------------------------------------")

            holiday_location_menu = (["Abroad,", "Not abroad", "Both"]) # User chooses where the holiday takes place

            holiday_location_choice = displayMenu(holiday_location_menu)

            if(holiday_location_choice == 1): # if the holiday is abroad

                location_option = ["Give out the location with a map", "Give out the location by typing it", "Back to main menu"]

                print("-------------------------------", colored("How would you like to give out the location?", "green"),"--------------------------------------")

                location_choice = displayMenu(location_option)

                if(location_choice == 1): # if the user wants to give the location with a map

                    weather_reports = Weather("NO INPUT", "MAP") # using the weather API to get the relevant data with the map

                    abroad_package = PackageCreation.essentialCreation("ABROAD") # we store the pre-made package for ABROAD holidays.

                    print("\n")

                    print(abroad_package.to_markdown())
                
                if(location_choice == 2): # if the user wants to give the location by typing it

                    # Asking for the location the holiday will take place

                    location = str(input("Please type in the city and country as this: city, countrycode: ")) # we ask for the location

                    weather_reports = Weather(location, "NO MAP") # using the weather API to get the relevant data
                    
                    print("\n")

                    abroad_package = PackageCreation.essentialCreation("ABROAD") # we store the pre-made package for ABROAD holidays.

                    print(abroad_package.to_markdown())


                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = (["Save the package", "Edit the package", "Save it in a Excel-file", "Nothing, go back to main menu"]) # We ask what the user wants to do with the given package

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package

                    save_package(abroad_package, saved_package_dict) # using our save_package function


                if(package_given_choice == 2): # if the user wants to edit the package

                    edited_package = edit_package(abroad_package)

                    print(edited_package.to_markdown())

                    print("-------------------------------", colored("What do you want to do with the edited package?", "green"), "---------------------")

                    edited_options = ["Save the package", "Save it in a Excel-file", "Nothing, Go back to main menu"]

                    edited_options_choice = displayMenu(edited_options)

                    if(edited_options_choice == 1): # if the user wants to save the package

                        save_package(edited_package, saved_package_dict) # using our save_package function


                    if(edited_options_choice == 2): # if the user wants to save the package in a Excel-file

                        excel_name = str(input(colored("What should the Excel-file be called? (remember the .xlsx extension): ", "yellow"))) # name of the file

                        edited_package.to_excel(excel_name)

                        print("The package has been saved")

                    
                    if(edited_options_choice == 3): # if the user wants to go back to main menu.

                        pass

                
                if(package_given_choice == 3): # if the user wants to save the package in a Excel-file

                    excel_name = str(input(colored("What should the Excel-file be called? (remember the .xlsx extension): ", "yellow"))) # name of the file

                    abroad_package.to_excel(excel_name)

                    print("The package has been saved")


            if(holiday_location_choice == 2): # if the holiday is not abroad

                location = str(input("Please type in the city and country as this: city, countrycode: ")) # Asking for the location the holiday will take place

                weather_reports = Weather(location, "NO") # using the weather API to get the relevant data

                not_abroad_package = PackageCreation.essentialCreation("NOT ABROAD") # storing the pre-made package for NOT ABROAD

                print(not_abroad_package.to_markdown())

                # We ask what the user wants to do with the package

                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = ["Save the package", "Edit the package", "Save it in a Excel-file", "Nothing, go back to main menu"]

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package
                    
                    save_package(not_abroad_package, saved_package_dict) # using our save_package function


                if(package_given_choice == 2): # if the user wants to edit the package

                    edit_package(not_abroad_package)

                
                if(package_given_choice == 3): # if the user wants to save the package in a Excel-file
                    
                    excel_name = str(input(colored("What should the Excel-file be called? (remember the .xlsx extension): ", "yellow"))) # name of the file

                    not_abroad_package.to_excel(excel_name)

                    print("The package has been saved")
                


            if(holiday_location_choice == 3): # if the holiday is both abroad and not abroad.

                placeholder = 2
        
        if(holiday_choice == 2): # if the user picks skiing holiday
            
            # Ask for how long the holiday will last

            number_of_days = int(input(colored(" How long is your holiday in days? ", "yellow"))) # we ask the number of days the holiday last

            
            print("-------------------------------", colored("Which type of gear will you have / need during your skiing holiday?", "green"), "---------------------")

            # Is it Ski / Snowboard (or maybe both?)

            type_options = ["Ski", "Snowboard", "BOTH", "Cancel"]

            type_choice = displayMenu(type_options) - 1 # Our indexer

            print("-------------------------------", colored("What transportation will be used?", "green"), "---------------------")

            # what type of transport will be used?

            ski_transport_options = ["Boat", "Boat and car", "Plane", "Car", "Cancel"]

            ski_transport_choice = displayMenu(ski_transport_options) - 1 # Our indexer


            print("-------------------------------", colored("How do you plan on staying during your holiday?", "green"), "---------------------")

            ski_stay_options = ["Hut", "Hotel / Hostel", "Other", "Cancel"]

            ski_stay_choice = displayMenu(ski_stay_options) - 1 # Our indexer


            # TODO - implement the ski holiday - look above - functionize it


            # TODO - implement the camping holiday as well as the custom holiday function


    

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

                package_menu = ["View the package", "Edit the package", "Delete the package", "Back to main menu"]

                package_menu_choice = displayMenu(package_menu)

                if(package_menu_choice == 1): # if the user wants to view the package

                    desired_package = saved_package_dict[selected_key] # we extract the value stored in the key, that has been selected.

                    print(desired_package.to_markdown())

                
                if(package_menu_choice == 2): # if the user wants to edit the package

                    selected_dataframe = saved_package_dict[selected_key]

                    edit_package(selected_dataframe) # using our edit_package function
                        
                    
                if(package_menu_choice == 3): # if the user wants to delete the package
                    
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
