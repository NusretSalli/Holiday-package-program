from inputverifier import * 

import numpy as np

from termcolor import colored

def displayMenu(options):
    
    ## DESCRIPTION OF THE FUNCTION ## 
    
    # Disclaimer: This code was taken from module 5
    
    # Purpose: Displays a menu with options
    
    # Usage: Used in the main script
        
    # Input: A list of options the user can choose from
    
    # Output: A valid integer 
    
    for i in range(len(options)):
        
        print(colored("{:d}. {:s}".format(i+1, options[i]),"magenta"))
        
    choice = 0

    option_list = list(range(1,len(options)+1))

    while choice not in option_list:
        
        choice = inputNumber(colored("Please choose a menu item: ", "yellow"))

        print("\n")
        
    return choice