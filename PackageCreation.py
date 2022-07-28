
import pandas as pd



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

    essential_package.columns = ["Must have | ", " Nice to have | ", "Longer stays | ", "Abroad |",]

    not_abroad_package = essential_package[["Must have | ", " Nice to have | ", "Longer stays | "]]

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


def skiingCreation():


    # ------------------------------------------------------- Skiing Package -----------------------------------------------------#

    # skiing clothes list

    skiing_clothes = ["Underwear", "Casual clothes", "Skiing underwear", "Inner layer", "Skiing socks", "Skiing jacket", "Skiing trousers", "Beanie", "Mittens", "Buff", "Swimwear"]

    # Skiing gear that is a must list

    skiing_gear_must_have = ["Ski","Backpack (preferably water-proof)", "boots", "Helmet", "Carapace", "Goggles", "Ski poles"]

    # Skiing gear that is nice to have list

    skiing_gear_nice_have = ["Go pro", "Gear for avalanches", "Hand / feet warmers", "cooling / heating blanket", "Ski lubricant"]

    # Snowboard gear that is a must list

    snowboard_gear_must_have = ["Helmet", "Carapace", "Goggles", "Snowboard", "Snowboard boots"]

    # Skiing cross country gear list

    skiing_cross_country_gear = ["Ski", "Ski poles", "Ski lubricant"]

    # Items to take or stuff to do if you stay in a hut

    skiing_hut = ["Linens", "Towels", "Food", "check for facilities in the hut"]

    # items to take or stuff to do if you stay in a hotel / hostel

    skiing_hotel_hostel = ["Linens if necessary"]


def campingCreation():

    # ------------------------------------------------------- Camping Package ----------------------------------------------------#

    # Items to take if you will be hiking when camping 

    camping_hiking = ["Hiking boots", "Food / drinks", "Backpack"]

    # Items to take if you will be living in a tent

    camping_tent = ["Tent", "Sleeping bag", "Sleeping pad", "Pillow", "Lamp", "Thermos", "Trash bags", "Folding chairs", "Drinking bottle"]

    # items to take with you to sustain yourself in a tent with food and drinks

    camping_tent_consumeables = ["Cups", "Cooking gears", "Ligther or matches", "Ignition blocks", "washing gears"]

    # items to take with you if you specifically will stay in a hotel / hostel

    camping_hotel_hostel = ["Linens if necessary"]


def bigcityCreation():

     # ------------------------------------------------------- Big city holiday --------------------------------------------------#

    # Stuff to take with you if you will not take a flight

    city_no_flight = ["Shoes for traveling", "Entertainment", "hand luggage for 100 ml item"]

    # Stuff to take with you if you will take a flight

    city_flight = ["Shoes for traveling","Entertainment"]




