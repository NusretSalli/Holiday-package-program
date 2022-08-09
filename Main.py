
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

                abroad_package = PackageCreation.essentialCreation("ABROAD")

                print(abroad_package.to_markdown())

                # we ask what the user wants to do with the given package

                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = np.array(["Save the package", "Edit the package", "Save it in a CSV-file", "Nothing, go back to main menu"])

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package
                    
                    # we ask the user for its name

                    package_name = str(input("What should the package be called?: "))

                    new_package_dict = {package_name: abroad_package, "Back to main menu": "Back"}

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

                not_abroad_package = PackageCreation.essentialCreation("NOT ABROAD")

                print(not_abroad_package.to_markdown())

                # We ask what the user wants to do with the package

                print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

                package_given_menu = np.array(["Save the package", "Edit the package", "Save it in a CSV-file", "Nothing, go back to main menu"])

                package_given_choice = displayMenu(package_given_menu)

                if(package_given_choice == 1): # if the user wants to save the package

                    package_name = str(input("What should the package be called?: "))

                    new_package_dict = {package_name: not_abroad_package, "Back to main menu": "Back"}

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

            
            if(saved_package_choice != saved_package_list.index("Back to main menu")+1): # if the user chooses one of the packages
                
                # we store the key that has been selected by the user

                selected_key = str(saved_package_list[int(saved_package_choice-1)])

                print(colored("\nCurrent package: " + selected_key + "\n", "blue"))

                # we ask the user what to do with the chosen saved package

                package_menu = ["View the package", "Edit the package", "Delete the package", "Back to main menu"]

                package_menu_choice = displayMenu(package_menu)

                if(package_menu_choice == 1): # if the user wants to view the package

                    # we extract the value stored in the key, that has been selected.

                    desired_package = saved_package_dict[selected_key]

                    print(desired_package.to_markdown())

                
                if(package_menu_choice == 2): # if the user wants to edit the package

                    print(saved_package_dict[selected_key].to_markdown())

                    print("-------------------------------", colored("Which column do you want to edit?", "green"), "---------------------")

                    selected_dataframe = saved_package_dict[selected_key]

                    columns = selected_dataframe.columns

                    edit_list = list()

                    # ------------------------------ PROBABLY AN EASIER WAY TO DO THIS - OPTIMIZE IT LATER ----------------------- #
                    for i in columns:

                        edit_list.append(str(i))

                    edit_list.append("Insert a new column")

                    edit_list.append("Back to main menu")
                    

                    edit_choice = int(displayMenu(edit_list)) 

                    
                    if(edit_choice <= len(edit_list)-2): # if the user picks one of the existing columns

                        print("-------------------------------", colored("What do you want to do with this column?", "green"), "---------------------")

                        raw_column = list(selected_dataframe.iloc[:, edit_choice-1])

                        edit_options = ["Remove an item", "Insert an item", "Remove the entire column", "Go back to main menu"]

                        edit_option_choice = displayMenu(edit_options)

                        if(edit_option_choice == 1): # if the user wants to remove an item

                            edit_column = [x for x in raw_column if type(x) == str] # we remove all the nans

                            print("-------------------------------", colored("Which element do you want to remove?", "green"), "---------------------")

                            edit_column.append("Back to main menu")

                            remove_choice = displayMenu(edit_column) # the user chooses an option

                            if(remove_choice != len(edit_column)): # if the user chooses an element to be removed.

                                confirmation_edit = str(input("Are you sure that you want to remove the element? - type yes if you are sure: "))

                                if(confirmation_edit.upper() == "YES"):

                                    max_rows = selected_dataframe.shape[0] # max number of rows

                                    edit_column.remove(edit_column[int(remove_choice)-1]) # removing the desired element

                                    edit_column.remove("Back to main menu")

                                    difference_row = max_rows - len(edit_column) # we calculate how many nans we have to put

                                    nan_list = [float("nan")] * difference_row

                                    inserting_column = edit_column + nan_list

                                    edited_dataframe = saved_package_dict[selected_key]

                                    edited_dataframe.iloc[:, edit_choice-1] = inserting_column

                                    if(edited_dataframe.iloc[-1].isna().sum().sum() == edited_dataframe.shape[1]):

                                        edited_dataframe.drop(index = edited_dataframe.index[-1], axis = 0, inplace = True)

                                        saved_package_dict[selected_key] = edited_dataframe
                                    
                                    else:

                                        saved_package_dict[selected_key] = edited_dataframe





                        if(edit_option_choice == 2): # if the user wants to insert an item

                            edit_column = [x for x in raw_column if type(x) == str] # we remove all the nans

                            new_item = str(input("What is the name of the item: "))

                            edit_column.append(new_item)

                            max_rows = selected_dataframe.shape[0] # max number of rows

                            difference_row = max_rows - len(edit_column) # we calculate how many nans we have to put

                            if(difference_row != -1): # if the dataframe has space to put the wanted item 

                                nan_list = [float("nan")] * difference_row

                                inserting_column = edit_column + nan_list

                                edited_dataframe = saved_package_dict[selected_key]

                                edited_dataframe.iloc[:, edit_choice-1] = inserting_column

                                saved_package_dict[selected_key] = edited_dataframe
                            
                            else: # if you want to insert something into the largest

                                new_row = [float("nan")] * selected_dataframe.shape[1]

                                # we insert the written item into the selected column

                                new_row[edit_choice-1] = new_item

                                # we insert the new row into our dataframe.

                                edited_dataframe = saved_package_dict[selected_key]

                                # inserted the row at the bottom

                                edited_dataframe.loc[len(edited_dataframe)] = new_row

                                # we substitute the old dataframe with the updated one

                                saved_package_dict[selected_key] = edited_dataframe
                            
                        if(edit_option_choice == 3): # if the user wants to remove the entire column

                            confirmation_column = str(input("Are you sure that you want to remove the column and all of its content? Type yes if you are sure: "))

                            if(confirmation_column.upper() == "YES"): # if the user confirms the changes

                                selected_dataframe = saved_package_dict[selected_key]

                                selected_dataframe.drop(selected_dataframe.columns[edit_choice-1], axis = 1, inplace = True)
                                
                                saved_package_dict[selected_key] = selected_dataframe

                                
                        

                    if(edit_choice == len(edit_list)-1): # if the user picks "insert a new column"

                        selected_dataframe = saved_package_dict[selected_key]

                        column_name = str(input("What should the new column be called? "))

                        column_elements = str(input("What should the new column include? Write it as follows: x,y,z...: "))

                        column_elements_list = column_elements.split(",")

                        max_rows = selected_dataframe.shape[0] # max number of rows

                        difference_row = max_rows - len(column_elements_list) # we calculate how many nans we have to put

                        if(len(column_elements_list) > max_rows): # if the number of elements you want to put is larger than the current number of rows
                            
                            number_new_rows = len(column_elements_list) - max_rows

                            selected_dataframe[colored(column_name, "yellow")] = column_elements_list[0:max_rows] # we insert the maximum allowed elements

                            for i in range(0,number_new_rows): # we loop over the remaining elements that can't fit the dataframe
                                
                                # make a list full of nan corresponding to our number of columns

                                nan_list = [float("nan")] * selected_dataframe.shape[1]

                                # we substitute the last element in nan_list with the current item we need to put

                                nan_list[-1] = column_elements_list[max_rows + i]

                                # we insert the row into our dataframe.

                                selected_dataframe.loc[len(selected_dataframe)] = nan_list

                            saved_package_dict[selected_key] = selected_dataframe


                        # ------------- we have to do something if you want to make a new column that is the "maximum" column ---------- #
                        else:

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
