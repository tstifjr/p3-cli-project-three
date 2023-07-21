from models import *
from dummy_band import musician_search_menu, make_audition_request
from global_helpers import *
from band_create_new import create_new_band

def check_band_name(band):
    print(f'\nIs this your band? : {band.name}')
    resp = input('\n[y/n]: ')
    if resp == 'y':
        print(f"\n\nWelcome, {band.name}! \n")
        return band
    elif resp == 'n':
        return None
    else:
        print('invalid response')
        return None

def band_menu():
    band = None
    b_menu_dict = {
        "1": musician_search_menu,
        "2": make_audition_request,
        "3": manage_profile
    }

    while True: 
        if not band:
            print("\n\n\n\n\n")
            print("""
╔╗ ┌─┐┌┐┌┌┬┐  ╦ ╦┬ ┬┌┐ 
╠╩╗├─┤│││ ││  ╠═╣│ │├┴┐
╚═╝┴ ┴┘└┘─┴┘  ╩ ╩└─┘└─┘ 
```````````````````````
"""
                ) #intro statements
            print("\n\n\n\nWelcome to the band hub!\n")
            print("Let's see if you're in our database! What is your band's name?\n\n\n\n")
        while not isinstance(band, Band): 
            name = input("\nEnter name: ")
            print("\n")
            if name == "exit":
                exit_program()
            band = Band.find_band_by_name(name)

            if not band:
                band = create_new_band()
            
            if isinstance(band, Band):
                band = check_band_name(band)


        print(""" \n\n\n\n\n\n\n
    ╔═╗┬  ┌─┐┌─┐┌─┐┌─┐  ╔╦╗┌─┐┬┌─┌─┐  ╔═╗┌─┐┬  ┌─┐┌─┐┌┬┐┬┌─┐┌┐┌
    ╠═╝│  ├┤ ├─┤└─┐├┤   ║║║├─┤├┴┐├┤   ╚═╗├┤ │  ├┤ │   │ ││ ││││
    ╩  ┴─┘└─┘┴ ┴└─┘└─┘  ╩ ╩┴ ┴┴ ┴└─┘  ╚═╝└─┘┴─┘└─┘└─┘ ┴ ┴└─┘┘└┘
    ````````````````````````````````````````````````````````````



            1. Search for musicians\n
            2. Request audtion\n
            3. View or alter your profile\n
            """)
        
        while True:
            b_menu_select = input("\n\n\nSelect Number: ")
            if b_menu_dict.get(b_menu_select):
                b_menu_dict[b_menu_select](band)
                break
            else: 
                print("\nPlease select a number between 1 and 3")

        print('\nWould you like to do something else?')
        resp_2 = input('\n[y/n]: ')
        if resp_2 == 'n':
            break
            # exit_program()

        

