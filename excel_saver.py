
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

        excel_name_existing = str(input(" Name of the existing excel-file you want to save the package to? "))

        sheet_name = str(input(" What should the sheet be called? "))

        # appending the dataframe to the sheet_name sheet

        with pd.ExcelWriter(excel_name_existing, mode='A') as writer:  
            dataframe.to_excel(writer, sheet_name=sheet_name)

        print(f"The dataframe has been saved to {excel_name_existing} under the sheet: {sheet_name}")

    if excel_choice == 2: # if the user wants to save the package in a new excel file

        print("------------------------------", colored("What should the name xlsx-file be (with .xlsx)?", "green"), "---------------------------------------------------")

        excel_name = str(input(" Name of the xlsx-file "))

        dataframe.to_excel(excel_name, engine = "xlsxwriter")

        print(f"the dataframe has been saved to {excel_name}")

    if excel_choice == 3: # if the user wants to cancel

        pass



