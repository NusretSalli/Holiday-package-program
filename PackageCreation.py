
import pandas as pd

from tabulate import tabulate

from termcolor import colored


# TODO - implement temperature and humidity into the package-creation

def essentialCreation(type):

    #------------------------------------------------- Essential Package ---------------------------------------------------------#

    # our must have list

    must_have = ["Toothbrush", "Toothpaste", "Deodorant", "Medicine", "Hair Brush", "Tampons", "Shampoo", "Insurance", "wallet"]

    # we make a dataframe out of it with a single column.

    must_have_dataframe = pd.DataFrame(must_have)

    # nice to have list

    nice_to_have = ["First aid", "Vaseline", "Condoms", "Make up", "Student-ID"]

    # nice to have dataframe

    nice_to_have_dataframe = pd.DataFrame(nice_to_have)

    # longer stays list

    longer_stays = ["Shaving equipments", "Nail cutter"]

    # longer stays dataframe

    longer_stays_dataframe = pd.DataFrame(longer_stays)

    # abroad list

    abroad = ["Passport", "Health insurance"]

    # abroad dataframe

    abroad_dataframe = pd.DataFrame(abroad)

    # we concatenate all the different dataframes into a single, big one.

    essential_package = pd.concat([must_have_dataframe, nice_to_have_dataframe, longer_stays_dataframe, abroad_dataframe], ignore_index=True, axis=1)

    # we rename the column names to something appropriate

    essential_package.columns = [
        colored("Must have", "yellow"),
        colored("Nice to have", "yellow"),
        colored("Longer stays", "yellow"),
        colored("Abroad", "yellow")]

    not_abroad_package = essential_package[[
        colored("Must have", "yellow"),
        colored("Nice to have", "yellow"),
        colored("Longer stays", "yellow")]]

    if(type.upper() == "ABROAD"):

        return(essential_package)
    
    elif(type.upper() == "NOT ABROAD"):

        return(not_abroad_package)

    else:

        pass


def entertainmentCreation():

    # ------------------------------------------------ General / entertainment stuff ----------------------------------------------------#

    # a package that contains all entertainment-stuff

    entertainment_package = ["Reading material", "Laptop", "gaming devices", "Chargers", "Powerbank", "Cards / dices", "Board games", "Ball games"]


def skiingCreation(type, transport, stay):

    ### --------------------------------------------------- FUNCTION DESCRIPTION -----------------------------------------------###

    ## INPUTS ##
    # type: Wether the user wants to do skiing or snowboarding
    # transport: How they will travel to the said location
    # Stay: Where they will be staying during their skiing holiday

    
    # ------------------------------------------------------- Skiing Package -----------------------------------------------------#

    # skiing clothes list

    skiing_clothes = ["Underwear", "Casual clothes", "Skiing underwear", "Inner layer", "Skiing socks", "Skiing jacket", "Skiing trousers", "Beanie", "Mittens", "Buff", "Swimwear"]

    skiing_clothes_dataframe = pd.DataFrame(skiing_clothes)

    # Skiing gear that is a must list

    skiing_gear_must_have = ["Ski","Backpack (preferably water-proof)", "boots", "Helmet", "Carapace", "Goggles", "Ski poles"]

    skiing_gear_must_dataframe = pd.DataFrame(skiing_gear_must_have)

    # Skiing gear that is nice to have list

    skiing_gear_nice_have = ["Go pro", "Gear for avalanches", "Hand / feet warmers", "cooling / heating blanket", "Ski lubricant"]

    skiing_gear_nice_dataframe = pd.DataFrame(skiing_gear_nice_have)

    # Snowboard gear that is a must list

    snowboard_gear_must_have = ["Helmet", "Carapace", "Goggles", "Snowboard", "Snowboard boots"]

    snowboard_gear_must_dataframe = pd.DataFrame(snowboard_gear_must_have)

    # Skiing cross country gear list

    skiing_cross_country_gear = ["Ski", "Ski poles", "Ski lubricant"]

    skiing_cross_country_dataframe = pd.DataFrame(skiing_cross_country_gear)

    # Items to take or stuff to do if you stay in a hut

    skiing_hut = ["Linens", "Towels", "Food", "check for facilities in the hut"]

    skiing_hut_dataframe = pd.DataFrame(skiing_hut)

    # items to take or stuff to do if you stay in a hotel / hostel

    skiing_hotel_hostel = ["Linens if necessary", "HOTEL"]

    skiing_hotel_hostel_dataframe = pd.DataFrame(skiing_hotel_hostel)

    skiing_boatandcar_transport = ["Toilet gadgets", "Entertainment", "Swimwear", "Clothes", "BOATCAR"]

    skiing_boatandcar_transport_dataframe = pd.DataFrame(skiing_boatandcar_transport)

    skiing_flight_transport = ["Passport", "Entertainment", "Neck Pillow", "PLANE"]

    skiing_flight_transport_dataframe = pd.DataFrame(skiing_flight_transport)

    skiing_car_transport = ["Entertainment", "CAR RIDE"]

    skiing_car_transport_dataframe = pd.DataFrame(skiing_car_transport)


    ##-------------------------------------------- A bunch of if statements ----------------------------------------------------------- ## 

    # if statements if the type = ski

    if(type == "SKI" and (transport == "BOAT" or transport == "CAR AND BOAT") and stay == "HUT"):

        skiing_package = pd.concat([
        skiing_clothes_dataframe, 
        skiing_gear_must_dataframe, 
        skiing_gear_nice_dataframe,
        skiing_boatandcar_transport_dataframe,
        skiing_hut_dataframe],
        ignore_index = True, axis = 1)

        skiing_package.columns = [
        colored("Skiing clothes", "yellow"),
        colored("Must skiing gear", "yellow"),
        colored("Optional skiing gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]



        return(skiing_package)
    
    if(type == "SKI" and (transport == "BOAT" or transport == "CAR AND BOAT") and (stay == "HOTEL" or stay == "HOSTEL")):
        
        
        skiing_package = pd.concat([
        skiing_clothes_dataframe, 
        skiing_gear_must_dataframe, 
        skiing_gear_nice_dataframe,
        skiing_boatandcar_transport_dataframe,
        skiing_hotel_hostel_dataframe],
        ignore_index = True, axis = 1)

        skiing_package.columns = [
        colored("Skiing clothes", "yellow"),
        colored("Must skiing gear", "yellow"),
        colored("Optional skiing gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(skiing_package)

    if(type == "SKI" and (transport == "BOAT" or transport == "CAR AND BOAT") and stay == "OTHER"):

        skiing_package = pd.concat([
        skiing_clothes_dataframe, 
        skiing_gear_must_dataframe, 
        skiing_gear_nice_dataframe,
        skiing_boatandcar_transport_dataframe],
        ignore_index = True, axis = 1)

        skiing_package.columns = [
        colored("Skiing clothes", "yellow"),
        colored("Must skiing gear", "yellow"),
        colored("Optional skiing gear", "yellow"),
        colored("Transport items", "yellow")]

        return(skiing_package)
    

    if(type == "SKI" and transport == "PLANE" and (stay == "HOTEL" or stay == "HOSTEL")):

        skiing_package = pd.concat([
        skiing_clothes_dataframe, 
        skiing_gear_must_dataframe, 
        skiing_gear_nice_dataframe,
        skiing_flight_transport_dataframe,
        skiing_hotel_hostel_dataframe],
        ignore_index = True, axis = 1)

        skiing_package.columns = [
        colored("Skiing clothes", "yellow"),
        colored("Must skiing gear", "yellow"),
        colored("Optional skiing gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(skiing_package)

    if(type == "SKI" and transport == "PLANE" and stay == "HUT"):

        skiing_package = pd.concat([
        skiing_clothes_dataframe, 
        skiing_gear_must_dataframe, 
        skiing_gear_nice_dataframe,
        skiing_flight_transport_dataframe,
        skiing_hut_dataframe],
        ignore_index = True, axis = 1)

        skiing_package.columns = [
        colored("Skiing clothes", "yellow"),
        colored("Must skiing gear", "yellow"),
        colored("Optional skiing gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(skiing_package)

    if(type == "SKI" and transport == "PLANE" and stay == "OTHER"):

        skiing_package = pd.concat([
        skiing_clothes_dataframe, 
        skiing_gear_must_dataframe, 
        skiing_gear_nice_dataframe,
        skiing_flight_transport_dataframe],
        ignore_index = True, axis = 1)

        skiing_package.columns = [
        colored("Skiing clothes", "yellow"),
        colored("Must skiing gear", "yellow"),
        colored("Optional skiing gear", "yellow"),
        colored("Transport items", "yellow")]

        return(skiing_package)


    if(type == "SKI" and transport == "CAR" and stay == "OTHER"):

        skiing_package = pd.concat([
        skiing_clothes_dataframe, 
        skiing_gear_must_dataframe, 
        skiing_gear_nice_dataframe,
        skiing_car_transport_dataframe],
        ignore_index = True, axis = 1)

        skiing_package.columns = [
        colored("Skiing clothes", "yellow"),
        colored("Must skiing gear", "yellow"),
        colored("Optional skiing gear", "yellow"),
        colored("Transport items", "yellow")]

        return(skiing_package)

    if(type == "SKI" and transport == "CAR" and (stay == "HOTEL" or stay == "HOSTEL")):

        skiing_package = pd.concat([
        skiing_clothes_dataframe, 
        skiing_gear_must_dataframe, 
        skiing_gear_nice_dataframe,
        skiing_car_transport_dataframe,
        skiing_hotel_hostel_dataframe],
        ignore_index = True, axis = 1)

        skiing_package.columns = [
        colored("Skiing clothes", "yellow"),
        colored("Must skiing gear", "yellow"),
        colored("Optional skiing gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(skiing_package)

    if(type == "SKI" and transport == "CAR" and stay == "HUT"):

        skiing_package = pd.concat([
        skiing_clothes_dataframe, 
        skiing_gear_must_dataframe, 
        skiing_gear_nice_dataframe,
        skiing_car_transport_dataframe,
        skiing_hut_dataframe],
        ignore_index = True, axis = 1)

        skiing_package.columns = [
        colored("Skiing clothes", "yellow"),
        colored("Must skiing gear", "yellow"),
        colored("Optional skiing gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(skiing_package)


    # if statements if the type = Snowboards

    if(type == "SNOWBOARD" and (transport == "BOAT" or transport == "CAR AND BOAT") and stay == "HUT"):

        snowboard_package = pd.concat([
        snowboard_gear_must_dataframe,
        skiing_boatandcar_transport_dataframe,
        skiing_hut_dataframe],
        ignore_index = True, axis = 1)

        snowboard_package.columns = [
        colored("Snowboard must gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(snowboard_package)
    
    if(type == "SNOWBOARD" and (transport == "BOAT" or transport == "CAR AND BOAT") and stay == "OTHER"):

        snowboard_package = pd.concat([
        snowboard_gear_must_dataframe,
        skiing_boatandcar_transport_dataframe],
        ignore_index = True, axis = 1)

        snowboard_package.columns = [
        colored("Snowboard must gear", "yellow"),
        colored("Transport items", "yellow")]

        return(snowboard_package)
    
    if(type == "SNOWBOARD" and (transport == "BOAT" or transport == "CAR AND BOAT") and (stay == "HOTEL" or stay == "HOSTEL")):

        snowboard_package = pd.concat([
        snowboard_gear_must_dataframe,
        skiing_boatandcar_transport_dataframe,
        skiing_hotel_hostel_dataframe],
        ignore_index = True, axis = 1)

        snowboard_package.columns = [
        colored("Snowboard must gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(snowboard_package)
    

    if(type == "SNOWBOARD" and transport == "PLANE" and (stay == "HOTEL" or stay == "HOSTEL")):

        snowboard_package = pd.concat([
        snowboard_gear_must_dataframe,
        skiing_flight_transport_dataframe,
        skiing_hotel_hostel_dataframe],
        ignore_index = True, axis = 1)

        snowboard_package.columns = [
        colored("Snowboard must gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(snowboard_package)
    
    if(type == "SNOWBOARD" and transport == "PLANE" and stay == "HUT"):

        snowboard_package = pd.concat([
        snowboard_gear_must_dataframe,
        skiing_flight_transport_dataframe,
        skiing_hut_dataframe],
        ignore_index = True, axis = 1)

        snowboard_package.columns = [
        colored("Snowboard must gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(snowboard_package)
    
    if(type == "SNOWBOARD" and transport == "PLANE" and stay == "OTHER"):

        snowboard_package = pd.concat([
        snowboard_gear_must_dataframe,
        skiing_flight_transport_dataframe],
        ignore_index = True, axis = 1)

        snowboard_package.columns = [
        colored("Snowboard must gear", "yellow"),
        colored("Transport items", "yellow")]

        return(snowboard_package)


    if(type == "SNOWBOARD" and transport == "CAR" and stay == "OTHER"):

        snowboard_package = pd.concat([
        snowboard_gear_must_dataframe,
        skiing_car_transport_dataframe],
        ignore_index = True, axis = 1)

        snowboard_package.columns = [
        colored("Snowboard must gear", "yellow"),
        colored("Transport items", "yellow")]

        return(snowboard_package)

    if(type == "SNOWBOARD" and transport == "CAR" and (stay == "HOTEL" or stay == "HOSTEL")):

        snowboard_package = pd.concat([
        snowboard_gear_must_dataframe,
        skiing_car_transport_dataframe,
        skiing_hotel_hostel_dataframe],
        ignore_index = True, axis = 1)

        snowboard_package.columns = [
        colored("Snowboard must gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(snowboard_package)
    
    if(type == "SNOWBOARD" and transport == "CAR" and stay == "HUT"):

        snowboard_package = pd.concat([
        snowboard_gear_must_dataframe,
        skiing_car_transport_dataframe,
        skiing_hut_dataframe],
        ignore_index = True, axis = 1)

        snowboard_package.columns = [
        colored("Snowboard must gear", "yellow"),
        colored("Transport items", "yellow"),
        colored("Stay items", "yellow")]

        return(snowboard_package)


def campingCreation(activity, stay_camp):

    # ------------------------------------------------------- Camping Package ----------------------------------------------------#

    # Items to take if you will be hiking when camping 

    camping_hiking = ["Hiking boots", "Food / drinks", "Backpack"]

    camping_hiking_dataframe = pd.DataFrame(camping_hiking)
    
    # items to take with you if you will be biking when camping

    camping_biking = ["Bicycle", "Helmet", "bike repair tool kit", "patching gadgets"]

    camping_biking_dataframe = pd.DataFrame(camping_biking)

    # Items to take if you will be living in a tent

    camping_tent = ["Tent", "Sleeping bag", "Sleeping pad", "Pillow", "Lamp", "Thermos", "Trash bags", "Folding chairs", "Drinking bottle"]

    camping_tent_dataframe = pd.DataFrame(camping_tent)

    # items to take with you to sustain yourself in a tent with food and drinks

    camping_tent_consumeables = ["Cups", "Cooking gears", "Ligther or matches", "Ignition blocks", "washing gears"]

    camping_tent_consumeables_dataframe = pd.DataFrame(camping_tent_consumeables)

    # items to take with you if you specifically will stay in a hotel / hostel

    camping_hotel_hostel = ["Linens if necessary"]

    camping_hotel_hostel_dataframe = pd.DataFrame(camping_hotel_hostel)

    if(activity == "HIKING" and stay_camp == "TENT"):

        camping_package = pd.concat([
        camping_hiking_dataframe,
        camping_tent_dataframe,
        camping_tent_consumeables_dataframe],
        ignore_index= True, axis = 1)

        camping_package.columns = [
        colored("Hiking items", "yellow"),
        colored("Tent items", "yellow"),
        colored("Consumeables items", "yellow")]

        return(camping_package)
    
    if(activity == "HIKING" and (stay_camp == "HOTEL" or stay_camp == "HOSTEL")):

        camping_package = pd.concat([
        camping_hiking_dataframe,
        camping_hotel_hostel_dataframe],
        ignore_index= True, axis = 1)

        camping_package.columns = [
        colored("Hiking items", "yellow"),
        colored("Hotel / hostel items", "yellow")]

        return( camping_package)
    
    if(activity == "BIKING" and stay_camp == "TENT"):

        camping_package = pd.concat([
        camping_biking_dataframe,
        camping_tent_dataframe,
        camping_tent_consumeables_dataframe],
        ignore_index= True, axis = 1)

        camping_package.columns = [
        colored("Biking items", "yellow"),
        colored("Tent items", "yellow"),
        colored("Consumeables items", "yellow")]

        return(camping_package)


    if(activity == "BIKING" and (stay_camp == "HOTEL" or stay_camp == "HOSTEL")):

        camping_package = pd.concat([
        camping_biking_dataframe,
        camping_hotel_hostel_dataframe],
        ignore_index= True, axis = 1)

        camping_package.columns = [
        colored("Biking items", "yellow"),
        colored("Hotel / hostel items", "yellow")]

        return(camping_package)


def bigcityCreation(transport):

    # ------------------------------------------------------- Big city holiday --------------------------------------------------#

    # stuff to take with you during your big city holiday

    big_city_stuff = ["Shoes for hiking", "belt bag", "OTHER STUFF?"]

    big_city_stuff_dataframe = pd.DataFrame(big_city_stuff)

    # Stuff to take with you if you will take a flight

    city_flight = ["Shoes for traveling", "Entertainment", "hand luggage for 100 ml item"]

    city_flight_dataframe = pd.DataFrame(city_flight)

    # Stuff to take with you if you will not take a flight

    city_no_flight = ["Shoes for traveling","Entertainment"]

    city_no_flight_dataframe = pd.DataFrame(city_no_flight)

    if(transport == "FLIGHT"):

        big_city_package = pd.concat([
        big_city_stuff_dataframe,
        city_flight_dataframe],
        ignore_index= True, axis = 1)

        big_city_package.columns = [
        colored("Big city items", "yellow"),
        colored("Transport items", "yellow")]

        return(big_city_package)

    
    if(transport == "NO FLIGHT"):

        big_city_package = pd.concat([
        big_city_stuff_dataframe,
        city_no_flight_dataframe],
        ignore_index= True, axis = 1)

        big_city_package.columns = [
        colored("Big city items", "yellow"),
        colored("Transport items", "yellow")]

        return(big_city_package)




