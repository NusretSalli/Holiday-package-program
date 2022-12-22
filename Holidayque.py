
from termcolor import colored # to give colorful messages to the terminal

from displayMenu import displayMenu # menu-creator function

import PackageCreation # the package-organizer function

from Weather import Weather # the Weather API function

from edit_package import edit_package

from save_package import save_package # our save_package function


def basic_holiday(saved_package_dict):

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


'''
            
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
            
            '''



def ski_holiday(saved_package_dict):

# Ask for how long the holiday will last

    number_of_days = int(input(colored(" How long is your holiday in days? ", "yellow"))) # we ask the number of days the holiday last

    
    print("-------------------------------", colored("Which type of gear will you have / need during your skiing holiday?", "green"), "---------------------")

    # Is it Ski / Snowboard (or maybe both?)

    type_options = ["Ski", "Snowboard", "BOTH", "Cancel"]

    type_choice = int(displayMenu(type_options) - 1) # Our indexer

    if type_choice == 3: # if we pick "cancel"

        pass


    print("-------------------------------", colored("What transportation will be used?", "green"), "---------------------")

    # what type of transport will be used?

    ski_transport_options = ["Boat", "Car and boat", "Plane", "Car", "Cancel"]

    ski_transport_choice = int(displayMenu(ski_transport_options) - 1) # Our indexer

    if ski_transport_choice == 4: # if the user picks cancel

        pass

    else:

        print("-------------------------------", colored("How do you plan on staying during your holiday?", "green"), "---------------------")

        ski_stay_options = ["Hut", "Hostel","Hotel", "Other", "Cancel"]

        ski_stay_choice = int(displayMenu(ski_stay_options) - 1) # Our indexer

        if ski_stay_choice == 4: # if the user picks "cancel"

            pass
        
        else:

            # creating the package based on the inputs provided

            ski_package = PackageCreation.skiingCreation(type_options[type_choice].upper(),
            ski_transport_options[ski_transport_choice].upper(),
            ski_stay_options[ski_stay_choice].upper())

            print(ski_package.to_markdown())

    print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

    package_given_menu = (["Save the package", "Edit the package", "Save it in a Excel-file", "Nothing, go back to main menu"]) # We ask what the user wants to do with the given package

    package_given_choice = displayMenu(package_given_menu)

    if(package_given_choice == 1): # if the user wants to save the package

        save_package(ski_package, saved_package_dict) # using our save_package function


    if(package_given_choice == 2): # if the user wants to edit the package

        edited_package = edit_package(ski_package)

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

        ski_package.to_excel(excel_name)

        print("The package has been saved")


def camping_holiday(saved_package_dict):

    # Ask for how long the holiday will last

    number_of_days = int(input(colored(" How long is your holiday in days? ", "yellow"))) # we ask the number of days the holiday last

    
    print("-------------------------------", colored("what type of activity will you be doing during your holiday?", "green"), "---------------------")

    # Is it Ski / Snowboard (or maybe both?)

    activity_options = ["Hiking", "Biking", "Cancel"]

    activity_choice = int(displayMenu(activity_options) - 1) # Our indexer

    if activity_choice == 2: # if we pick "cancel"

        pass
        
    else:

        print("-------------------------------", colored("Where will you stay during your holiday?", "green"), "---------------------")

        stay_options = ["Tent", "Hostel", "Hotel", "Cancel"]

        stay_choice = int(displayMenu(stay_options)-1) # our indexer

        if stay_options == 3: # if the user pickes cancel

            pass
        
        else:

            camping_package = PackageCreation.campingCreation(activity_options[activity_choice].upper(), stay_options[stay_choice].upper())

            print(camping_package.to_markdown())

    
    print("-------------------------------", colored("What do you want to do with the given package?", "green"), "---------------------")

    package_given_menu = (["Save the package", "Edit the package", "Save it in a Excel-file", "Nothing, go back to main menu"]) # We ask what the user wants to do with the given package

    package_given_choice = displayMenu(package_given_menu)

    if(package_given_choice == 1): # if the user wants to save the package

        save_package(camping_package, saved_package_dict) # using our save_package function


    if(package_given_choice == 2): # if the user wants to edit the package

        edited_package = edit_package(camping_package)

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

        camping_package.to_excel(excel_name)

        print("The package has been saved")
