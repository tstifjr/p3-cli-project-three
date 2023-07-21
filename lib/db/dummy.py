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
        print('Please select your method of band search.')
        print('''
            1. Actively looking for new members.\n
            2. By name\n
            3. By genre\n
            4. By instrument    
            ''')
        menu_selections = input('Please choose a number or type exit to exit: ')
        if menu_selections == "exit":
            break
        elif search_menu_dict.get(menu_selections):
            search_menu_dict[menu_selections](musician)
        else:
            print('invalid input')

################           ACTIVELY LOOKING          ############

def actively_looking(musician):
    new_input = None
    options_dict = {'1' : func_1,
                    '2' : func_2,
                    '3' : func_3}    
    while True:
        print('1. to see bands that need your instrument and are looking\n' +
            '2. to see bands that play your genre and are looking\n' +
            '3. to see all bands currently looking for members\n' +
            'exit to leave this search.\n')
        new_input = input('select number: ')
        if new_input == "exit":
            break
        elif options_dict.get(new_input):
            options_dict[new_input](musician)
            print('search some more?')
            new_input = input('[y/n] :')
            if new_input == 'n':
                break
        else :
            print('not a valid input')

def func_1 (musician):
    print('Here are some bands need a member who plays your insturment')
    the_list = musician.bands_look_same_instr()
    for b in the_list:
        print(f"{b.name} | Genre: {b.genre.name}")
    req_aud_from_list(musician, the_list)

def func_2 (musician):
    print('Here are some bands play your genre')
    the_list = musician.bands_look_same_genre()
    for b in the_list:
        print(f"{b.name} | instrument needed: {b.instrument.name}")
    req_aud_from_list(musician, the_list)

def func_3 (musician):
    print('Here are all the bands looking for members')
    the_list = Band.bands_looking()
    the_list.sort(key = lambda band : band.genre.name)
    for b in the_list:
        print(f"{b.name} | Genre: {b.genre.name} | instrument needed: {b.instrument.name}")
    req_aud_from_list(musician, the_list)

################           NAME SEARCH               ############

def name_search(musician):
    print('Please Enter the name of the Band to search for')
    while True:
        name = input("Enter the Band's name: ")
        result = Band.find_band_by_name(name)
        if isinstance(result, Band):
            the_list = [result]
            result.show_info
            req_aud_from_list(musician, the_list)
            print("Would you like to search for a different name? ")
            search_again = input("[y/n]: ")
            if search_again == "n":
                break

#######################################

#           REQUEST AUDITION

########################################

def make_audition_request(musician):
    print('Please provide the name of the band you want to audition for')
    band = None
    while not isinstance(band, Band):
        band_input = input("Band's name is:  ")
        band = Band.find_band_by_name(band_input)
    print(f"Send audition request to {band.name}?\n")
    band.show_info
    response = input("[y/n]: ")
    if (response == "y" or response == "yes"):
        musician.request_audition(band)
