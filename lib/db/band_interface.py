from models import *
import sys
from dummy_band import musician_search_menu

def fake_fun(band):
    print("Placeholder")

def check_band_name(band):
    print(f'Is this your band? : {band.name}')
    resp = input('y/n: ')
    if resp == 'y':
        print(f"Welcome, {band.name}! \n")
        return band
    elif resp == 'n':
        return None
    else:
        print('invalid response')
        return None

def band_menu():
    from cli import exit_program
    band = None
    b_menu_dict = {
        "1": musician_search_menu,
        "2": fake_fun,
        "3": fake_fun,
        "4": fake_fun
    }

    while True: #initate and stay in Musician Menu
        if not band:
            print("\n\n\n\n\n")
            print("""
╔╗ ┌─┐┌┐┌┌┬┐  ╦ ╦┬ ┬┌┐ 
╠╩╗├─┤│││ ││  ╠═╣│ │├┴┐
╚═╝┴ ┴┘└┘─┴┘  ╩ ╩└─┘└─┘   
"""
                ) #intro statements
            print("Welcome to the band hub!")
            print("Let's see if you're in our database! What is your band's name?\n\n\n\n")
        while not isinstance(band, Band): #select a musician to be
            name = input("Enter name: ")
            if name == "exit":
                exit_program()
            band = Band.find_band_by_name(name)

            if not band:
                #band = create_new_band()
                pass
            
            if isinstance(band, Band):
                band = check_band_name(band)


        print(""" 
            Please select one of the options below: \n
            1. Search for musicians\n
            2. Request audtion\n
            3. View or alter your profile\n
            4. General stats and information\n 
            """)
        
        while True:
            b_menu_select = input("Please enter a number for your choice: ")
            if b_menu_dict.get(b_menu_select):
                b_menu_dict[b_menu_select](band)
                break
            else: 
                print("Please select a number between 1 and 4")

        print('Would you like to do something else?')
        resp_2 = input('y/n: ')
        if resp_2 == 'n':
            exit_program()

        

