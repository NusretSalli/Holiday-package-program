

from termcolor import colored


def inputNumber(prompt):
    
    ## DESCRIPTION OF THE FUNCTION ## 
    
    # Purpose: Prompt the user to pick a valid option
    
    # Usage: Used in the main script
        
    # Input: User input

    # Output: menu choice 
    
    while True:
        
        try:
            
            num = float(input(prompt))
            
            break
        
        except ValueError:
            
            print(colored("INVALID INPUT: only integers allowed", "red"))
            
            pass
        
    return num