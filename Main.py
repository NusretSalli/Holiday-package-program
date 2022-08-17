
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

import tkinter

import tkintermapview


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

                location_option = ["Give out the location with a map", "Give out location by typing it", "Back to main menu"]

                print("-------------------------------", colored("How would you like to give out the location?", "green"),"--------------------------------------")

                location_choice = displayMenu(location_option)

                if(location_choice == 1):

                    weather_reports = Weather("NO INPUT", "MAP") # using the weather API to get the relevant data with the map

                    abroad_package = PackageCreation.essentialCreation("ABROAD") # we store the pre-made package for ABROAD holidays.

                    print(abroad_package.to_markdown())
                
                if(location_choice == 2):

                    # Asking for the location the holiday will take place

                    location = str(input("Please type in the city and country as this: city, countrycode: ")) # we ask for the location

                    weather_reports = Weather(location, "NO MAP") # using the weather API to get the relevant data

                    abroad_package = PackageCreation.essentialCreation("ABROAD") # we store the pre-made package for ABROAD holidays.

                    print(abroad_package.to_markdown())


                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = (["Save the package", "Edit the package", "Save it in a CSV-file", "Nothing, go back to main menu"]) # We ask what the user wants to do with the given package

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package

                    package_name = str(input("What should the package be called?: ")) # we ask the user for its name

                    new_package_dict = {package_name: abroad_package, "Back to main menu": "Back"}

                    # we delete the key "back to main menu" and its value to put it at the end every time a new package is saved

                    del saved_package_dict["Back to main menu"]

                    saved_package_dict.update(new_package_dict)

                    print("\nThe package called " + package_name + " has been saved\n")


                if(package_given_choice == 2): # if the user wants to edit the package

                    placeholder = 2

                
                if(package_given_choice == 3): # if the user wants to save the package in a CSV-file

                    csv_name = str(input("What should the csv-file be called?: "))

                    abroad_package.to_csv(csv_name)

                    print("The package has been saved")


            if(holiday_location_choice == 2): # if the holiday is not abroad

                location = str(input("Please type in the city and country as this: city, countrycode: ")) # Asking for the location the holiday will take place

                weather_reports = Weather(location, "NO") # using the weather API to get the relevant data

                not_abroad_package = PackageCreation.essentialCreation("NOT ABROAD") # storing the pre-made package for NOT ABROAD

                print(not_abroad_package.to_markdown())

                # We ask what the user wants to do with the package

                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = ["Save the package", "Edit the package", "Save it in a CSV-file", "Nothing, go back to main menu"]

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package

                    package_name = str(input("What should the package be called?: ")) # user gives the name of the package

                    new_package_dict = {package_name: not_abroad_package, "Back to main menu": "Back"} # we make a sub-dictionary to put into our main

                    del saved_package_dict["Back to main menu"] # delete the back to menu value from main.

                    saved_package_dict.update(new_package_dict) # we now combine the main and sub-dictionary to the main

                    print("\nThe package called " + package_name + " has been saved\n")


                if(package_given_choice == 2): # if the user wants to edit the package

                    placeholder = 2

                
                if(package_given_choice == 3): # if the user wants to save the package in a CSV-file
                    
                    csv_name = str(input("What should the csv-file be called?: "))

                    not_abroad_package.to_csv(csv_name)

                    print("The package has been saved")
                


            if(holiday_location_choice == 3): # if the holiday is both abroad and not abroad.

                placeholder = 2


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

                    print(saved_package_dict[selected_key].to_markdown())

                    print("-------------------------------", colored("Which column do you want to edit?", "green"), "---------------------")

                    selected_dataframe = saved_package_dict[selected_key] # we pick out the selected dataframe

                    columns = selected_dataframe.columns # we make a "list" of our columns

                    edit_list = list() # we make an empty list that will contain our options

                    # ------------------------------ PROBABLY AN EASIER WAY TO DO THIS - OPTIMIZE IT LATER ----------------------- #

                    for i in columns: # for loop that will iterate through columns

                        edit_list.append(str(i))

                    edit_list.append("Insert a new column") # Appending insert new column option

                    edit_list.append("Back to main menu") # Appending back to main menu
                
                    edit_choice = int(displayMenu(edit_list)) 

                    if(edit_choice <= len(edit_list)-2): # if the user picks one of the existing columns

                        print("-------------------------------", colored("What do you want to do with this column?", "green"), "---------------------")

                        raw_column = list(selected_dataframe.iloc[:, edit_choice-1]) # we take the selected column

                        edit_options = ["Remove an item", "Insert an item", "Remove the entire column", "Go back to main menu"]

                        edit_option_choice = displayMenu(edit_options) # User chooses what to do with the column

                        if(edit_option_choice == 1): # if the user wants to remove an item

                            edit_column = [x for x in raw_column if type(x) == str] # we remove all the nans

                            print("-------------------------------", colored("Which element do you want to remove?", "green"), "---------------------")

                            edit_column.append("Back to main menu")

                            remove_choice = displayMenu(edit_column) # the user chooses an an element

                            if(remove_choice != len(edit_column)): # if the user chooses an element to be removed.

                                confirmation_edit = str(input("Are you sure that you want to remove the element? - type yes if you are sure: "))

                                if(confirmation_edit.upper() == "YES"): # if the user seriously want to delete the element

                                    max_rows = selected_dataframe.shape[0] # max number of rows

                                    edit_column.remove(edit_column[int(remove_choice)-1]) # removing the desired element

                                    edit_column.remove("Back to main menu")

                                    difference_row = max_rows - len(edit_column) # we calculate how many nans we have to put

                                    nan_list = [float("nan")] * difference_row # we make a list of nan that will fill out the rest of the column

                                    inserting_column = edit_column + nan_list # Combining the edited column with the nan_list

                                    edited_dataframe = saved_package_dict[selected_key]

                                    edited_dataframe.iloc[:, edit_choice-1] = inserting_column # we substitute our column with the edited one

                                    if(edited_dataframe.iloc[-1].isna().sum().sum() == edited_dataframe.shape[1]): # if the row only contains nan, we'll remove it

                                        edited_dataframe.drop(index = edited_dataframe.index[-1], axis = 0, inplace = True) # the last row gets dropped / removed

                                        saved_package_dict[selected_key] = edited_dataframe
                                    
                                    else: # if the row still contains items

                                        saved_package_dict[selected_key] = edited_dataframe


                        if(edit_option_choice == 2): # if the user wants to insert an item

                            edit_column = [x for x in raw_column if type(x) == str] # we remove all the nans

                            new_item = str(input("What is the name of the item: ")) # user names the new item

                            edit_column.append(new_item) # we append it to our column

                            max_rows = selected_dataframe.shape[0] # max number of rows

                            difference_row = max_rows - len(edit_column) # we calculate how many nans we have to put

                            if(difference_row != -1): # if the dataframe has space to put the wanted item 

                                nan_list = [float("nan")] * difference_row # We make a list of nan that will fill out the rest of the column

                                inserting_column = edit_column + nan_list # Combining the edited column with the nan_list

                                edited_dataframe = saved_package_dict[selected_key]

                                edited_dataframe.iloc[:, edit_choice-1] = inserting_column # inserting the new column into our dataframe.

                                saved_package_dict[selected_key] = edited_dataframe
                            
                            else: # if you want to insert something into the largest

                                new_row = [float("nan")] * selected_dataframe.shape[1] # number of rows the dataframe have

                                new_row[edit_choice-1] = new_item # we insert the written item into the selected column

                                edited_dataframe = saved_package_dict[selected_key] # we insert the new row into our dataframe.

                                edited_dataframe.loc[len(edited_dataframe)] = new_row # inserted the row at the bottom

                                # we substitute the old dataframe with the updated one

                                saved_package_dict[selected_key] = edited_dataframe
                            
                        if(edit_option_choice == 3): # if the user wants to remove the entire column

                            confirmation_column = str(input("Are you sure that you want to remove the column and all of its content? Type yes if you are sure: "))

                            if(confirmation_column.upper() == "YES"): # if the user confirms the changes

                                selected_dataframe = saved_package_dict[selected_key]

                                selected_dataframe.drop(selected_dataframe.columns[edit_choice-1], axis = 1, inplace = True) # removing the entire column
                                
                                saved_package_dict[selected_key] = selected_dataframe

                                # IF THE ROWS CONTAIN ONLY NANS - remove them  #

                                
                    if(edit_choice == len(edit_list)-1): # if the user picks "insert a new column"

                        selected_dataframe = saved_package_dict[selected_key]

                        column_name = str(input("What should the new column be called? ")) # User gives the column name

                        column_elements = str(input("What should the new column include? Write it as follows: x,y,z...: ")) # A list of elements to be added into the new column

                        column_elements_list = column_elements.split(",") # we make a list of elements

                        max_rows = selected_dataframe.shape[0] # max number of rows

                        difference_row = max_rows - len(column_elements_list) # we calculate how many nans we have to put

                        if(len(column_elements_list) > max_rows): # if the number of elements you want to put is larger than the current number of rows
                            
                            number_new_rows = len(column_elements_list) - max_rows

                            selected_dataframe[colored(column_name, "yellow")] = column_elements_list[0:max_rows] # we insert the maximum allowed elements

                            for i in range(0,number_new_rows): # we loop over the remaining elements that can't fit the dataframe

                                nan_list = [float("nan")] * selected_dataframe.shape[1] # make a list full of nan corresponding to our number of columns

                                nan_list[-1] = column_elements_list[max_rows + i] # we substitute the last element in nan_list with the current item we need to put

                                selected_dataframe.loc[len(selected_dataframe)] = nan_list # we insert the row into our dataframe.

                            saved_package_dict[selected_key] = selected_dataframe

                        else: # if the new column doesn't exceed the maximum number of rows

                            nan_list = [float("nan")] * difference_row

                            new_column = column_elements_list + nan_list

                            selected_dataframe[colored(column_name, "yellow")] = new_column

                            saved_package_dict[selected_key] = selected_dataframe
      
                        
                    
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
