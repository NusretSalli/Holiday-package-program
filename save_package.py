

def save_package(saved_package, main_package):

    package_name = str(input("What should the package be called?: ")) # we ask the user for its name

    new_package_dict = {package_name: saved_package, "Back to main menu": "Back"}

    # we delete the key "back to main menu" and its value to put it at the end every time a new package is saved

    del main_package["Back to main menu"]

    main_package.update(new_package_dict)

    print("\nThe package called " + package_name + " has been saved\n")