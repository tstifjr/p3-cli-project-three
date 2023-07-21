from models import *
import sys
from global_helpers import *

#######################################

#           SEARCH FOR BANDS

########################################

def band_search_menu(musician):
    search_menu_dict = {
        '1' : actively_looking,
        '2' : name_search, 
        '3' : genre_search, #imported from global
        '4' : instrument_search #imported from global
    }
    while True:
        print('''

  _____                     _       __  __      _   _               _ 
 / ____|                   | |     |  \/  |    | | | |             | |
| (___   ___  __ _ _ __ ___| |__   | \  / | ___| |_| |__   ___   __| |
 \___ \ / _ \/ _` | '__/ __| '_ \  | |\/| |/ _ \ __| '_ \ / _ \ / _` |
 ____) |  __/ (_| | | | (__| | | | | |  | |  __/ |_| | | | (_) | (_| |
|_____/ \___|\__,_|_|  \___|_| |_| |_|  |_|\___|\__|_| |_|\___/ \__,_|
``````````````````````````````````````````````````````````````````````


            1. Actively looking for new members.\n
            2. By name\n
            3. By genre\n
            4. By instrument 
\n\n\n   
            ''')
        menu_selections = input('Select number or type [exit] to exit: ')
        if menu_selections == "exit":
            break
        elif search_menu_dict.get(menu_selections):
            search_menu_dict[menu_selections](musician)
        else:
            print('Invalid input')

################           ACTIVELY LOOKING          ############

def actively_looking(musician):
    new_input = None
    options_dict = {'1' : func_1,
                    '2' : func_2,
                    '3' : func_3}    
    while True:
        print("""
              
  ____                  _       _                 _    _                __             __  __           _      _                 
 |  _ \                | |     | |               | |  (_)              / _|           |  \/  |         (_)    (_)                
 | |_) | __ _ _ __   __| |___  | |     ___   ___ | | ___ _ __   __ _  | |_ ___  _ __  | \  / |_   _ ___ _  ___ _  __ _ _ __  ___ 
 |  _ < / _` | '_ \ / _` / __| | |    / _ \ / _ \| |/ / | '_ \ / _` | |  _/ _ \| '__| | |\/| | | | / __| |/ __| |/ _` | '_ \/ __|
 | |_) | (_| | | | | (_| \__ \ | |___| (_) | (_) |   <| | | | | (_| | | || (_) | |    | |  | | |_| \__ \ | (__| | (_| | | | \__ \ 
 |____/ \__,_|_| |_|\__,_|___/ |______\___/ \___/|_|\_\_|_| |_|\__, | |_| \___/|_|    |_|  |_|\__,_|___/_|\___|_|\__,_|_| |_|___/
 `````````````````````````````````````````````````````````````` __/ | ```````````````````````````````````````````````````````````                                                            
                                                               |___/   
            

            1. See bands that need your instrument
            
            2. See bands that play your genre
            
            3. See all bands
\n\n

Type [exit] to leave this search
        """)
        new_input = input('\nSelect Number: ')
        
        if new_input == "exit":
            break
        elif options_dict.get(new_input):
            options_dict[new_input](musician)
            print('\nSearch some more?')
            new_input = input('\n[y/n] :')
            if new_input == 'n':
                break
        else :
            print('\nNot a valid input')

def func_1 (musician):
    print(f"\n::::::Here are Bands That Play {musician.instrument.name}::::::\n")
    the_list = musician.bands_look_same_instr()
    for b in the_list:
        print(f"{b.name} | Genre: {b.genre.name}")
    print("")
    req_aud_from_list(musician, the_list)

def func_2 (musician):
    print(f"\n::::::Here are Bands That Play {musician.genre.name}::::::\n")
    the_list = musician.bands_look_same_genre()
    for b in the_list:
        print(f"{b.name} | instrument needed: {b.instrument.name}")
    req_aud_from_list(musician, the_list)

def func_3 (musician):
    print('\n::::::All Bands Currently Looking::::::\n')
    the_list = Band.bands_looking()
    the_list.sort(key = lambda band : band.genre.name)
    for b in the_list:
        print(f"{b.name} | Genre: {b.genre.name} | instrument needed: {b.instrument.name}")
    req_aud_from_list(musician, the_list)

################           NAME SEARCH               ############

def name_search(musician):
    while True:
        name = input("\nEnter the Band's name: ")
        result = Band.find_band_by_name(name)
        if isinstance(result, Band):
            the_list = [result]
            result.show_info
            req_aud_from_list(musician, the_list)
            print("\nWould you like to search for a different name? ")
            search_again = input("\n[y/n]: ")
            if search_again == "n":
                break

#######################################

#           REQUEST AUDITION

########################################

def make_audition_request(musician):
    print('\nPlease provide the name of the band you want to audition for')
    band = None
    while not isinstance(band, Band):
        band_input = input("\nBand's name is:  ")
        band = Band.find_band_by_name(band_input)
    print(f"\nSend audition request to {band.name}?\n")
    band.show_info
    response = input("\n[y/n]: ")
    if (response == "y" or response == "yes"):
        musician.request_audition(band)
