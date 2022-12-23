
import pandas as pd

import numpy as np

from termcolor import colored

from displayMenu import displayMenu # menu-creator function

def excel_saver(dataframe):

    '''
    Saving a pandas dataframe to an excel-file
    
    
    '''

    print("------------------------------", colored("how would you save the package?", "green"), "---------------------------------------------------")

    excel_options = ["Save the package in an existing excel file", "save the pacage in a new excel file", "cancel"]

    excel_choice = displayMenu(excel_options)

    if excel_choice == 1: # if the user wants to save it in an existing file (new file or new sheet)

        # TODO - MAKE THIS LATER

        placeholder = 2


    if excel_choice == 2: # if the user wants to save the package in a new excel file

        print("------------------------------", colored("What should the name xlsx-file be (with .xlsx)?", "green"), "---------------------------------------------------")

        excel_name = str(input(" Name of the xlsx-file "))

        dataframe.to_excel(excel_name, engine = "xlsxwriter")

    if excel_choice == 3: # if the user wants to cancel

        pass



