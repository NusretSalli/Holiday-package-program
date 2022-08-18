
import pandas as pd

import numpy as np

from termcolor import colored # to give colorful messages to the terminal

from displayMenu import displayMenu # menu-creator function

import PackageCreation # the package-organizer function

dataframe_test = PackageCreation.essentialCreation("ABROAD")

def edit_package(dataframe):

    while True:

        print(dataframe.to_markdown())

        print("-------------------------------", colored("Which column do you want to edit?", "green"), "---------------------")

        selected_dataframe = dataframe # we pick out the selected dataframe

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

            edit_options = ["Remove an item", "Insert an item", "Remove the entire column", "Go back to package option"]

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

                        edited_dataframe = dataframe

                        edited_dataframe.iloc[:, edit_choice-1] = inserting_column # we substitute our column with the edited one

                        if(edited_dataframe.iloc[-1].isna().sum().sum() == edited_dataframe.shape[1]): # if the row only contains nan, we'll remove it

                            edited_dataframe.drop(index = edited_dataframe.index[-1], axis = 0, inplace = True) # the last row gets dropped / removed

                            dataframe = edited_dataframe
                        
                        else: # if the row still contains items

                            dataframe = edited_dataframe


            if(edit_option_choice == 2): # if the user wants to insert an item

                edit_column = [x for x in raw_column if type(x) == str] # we remove all the nans

                new_item = str(input("What is the name of the item: ")) # user names the new item

                edit_column.append(new_item) # we append it to our column

                max_rows = selected_dataframe.shape[0] # max number of rows

                difference_row = max_rows - len(edit_column) # we calculate how many nans we have to put

                if(difference_row != -1): # if the dataframe has space to put the wanted item 

                    nan_list = [float("nan")] * difference_row # We make a list of nan that will fill out the rest of the column

                    inserting_column = edit_column + nan_list # Combining the edited column with the nan_list

                    edited_dataframe = dataframe

                    edited_dataframe.iloc[:, edit_choice-1] = inserting_column # inserting the new column into our dataframe.

                    dataframe = edited_dataframe
                
                else: # if you want to insert something into the largest

                    new_row = [float("nan")] * selected_dataframe.shape[1] # number of rows the dataframe have

                    new_row[edit_choice-1] = new_item # we insert the written item into the selected column

                    edited_dataframe = dataframe # we insert the new row into our dataframe.

                    edited_dataframe.loc[len(edited_dataframe)] = new_row # inserted the row at the bottom

                    # we substitute the old dataframe with the updated one

                    dataframe = edited_dataframe
                
            if(edit_option_choice == 3): # if the user wants to remove the entire column

                confirmation_column = str(input("Are you sure that you want to remove the column and all of its content? Type yes if you are sure: "))

                if(confirmation_column.upper() == "YES"): # if the user confirms the changes

                    selected_dataframe = dataframe

                    selected_dataframe.drop(selected_dataframe.columns[edit_choice-1], axis = 1, inplace = True) # removing the entire column
                    
                    dataframe = selected_dataframe

                    # IF THE ROWS CONTAIN ONLY NANS - remove them  #

                    
        if(edit_choice == len(edit_list)-1): # if the user picks "insert a new column"

            selected_dataframe = dataframe

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

                dataframe = selected_dataframe

            else: # if the new column doesn't exceed the maximum number of rows

                nan_list = [float("nan")] * difference_row

                new_column = column_elements_list + nan_list

                selected_dataframe[colored(column_name, "yellow")] = new_column

                dataframe = selected_dataframe
        
        if(edit_choice == len(edit_list)): # If the user wants to exit the while true

            break

    return dataframe