"""
Author: 蛇道
Url: https://github.com/caminodelaserpiente
"""


from qr_generator.qr_generator import *


def banner():
    banner= """
      __ _  _ __          __ _   ___  _ __    ___  _ __   __ _ | |_   ___   _ __ 
     / _` || '__|        / _` | / _ \| '_ \  / _ \| '__| / _` || __| / _ \ | '__|
    | (_| || |          | (_| ||  __/| | | ||  __/| |   | (_| || |_ | (_) || |   
     \__, ||_|    _____  \__, | \___||_| |_| \___||_|    \__,_| \__| \___/ |_|   
        |_|      |_____| |___/                                                   \n"""
    print(banner)



def option_type():
    options = {
        0: 'bye',
        1: 'Unstyled',
        2: 'Styled'
    }
    menu = f""" 
    ----------------------------------------------------
        - Select type to create QR. (e.g. >>> 1)
            [0] {options[0]}
            [1] {options[1]}
            [2] {options[2]}"""
    print(menu)
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            response = int(input("Select option.\n>>> "))
            if response in options.keys():
                return response
            else:
                print("[Error] Please enter a valid option.\n")
                attempts += 1
        except ValueError:
            attempts += 1
            print("[Error] Please enter a valid numerical option.\n")
    print("Exceeded maximum attempts. Exiting the program.")
    exit()


def option_styled():
    options = {
        1: RoundedModuleDrawer(),
        2: HorizontalBarsDrawer(),
        3: VerticalBarsDrawer(),
        4: CircleModuleDrawer(),
        5: GappedSquareModuleDrawer()
    }
    menu = f"""
    ----------------------------------------------------
        - Select option to convert. (e.g. >>> 2)
            [0] RoundedModuleDrawer
            [1] HorizontalBarsDrawer
            [2] VerticalBarsDrawer
            [3] CircleModuleDrawer
            [4] GappedSquareModuleDrawer"""
    print(menu)
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            response = int(input("Select option.\n>>> "))
            if response in options.keys():
                return options[response]
            else:
                print("[Error] Please enter a valid option.\n")
                attempts += 1
        except ValueError:
            attempts += 1
            print("[Error] Please enter a valid numerical option.\n")
    print("Exceeded maximum attempts. Exiting the program.")
    exit()


def qr_generator():
    banner()
    try:
        while True:
            response = option_type()
            if response == 0:
                print('bye')
                break
            elif response == 1:
                qr_unstyled()
            elif response == 2:
                response = option_styled()
                qr_styled(response)
    except KeyboardInterrupt:
        print("\ninterrupted by the user bye")
