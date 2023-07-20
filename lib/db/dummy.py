from models import *
import sys
from global_helpers import *

#############band search menus ####################

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

############actively looking###############

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
    print(the_list)
    req_aud_from_list(musician, the_list)

def func_2 (musician):
    print('Here are some bands play your genre')
    the_list = musician.bands_look_same_genre()
    print(the_list)
    req_aud_from_list(musician, the_list)

def func_3 (musician):
    print('Here are all the bands looking for members')
    the_list = Band.bands_looking()
    print(the_list)
    req_aud_from_list(musician, the_list)

##############name search functions######################

def name_search(musician):
    from band_interface import check_band_name
    band = None
    u_input = None
    options_dict = {
    '1' : display_info,
    '2' : request_audition,
    '3' : new_search
    }

    print('Please Enter the name of the Band to search for')
    while u_input != 'exit':
        while not isinstance(band, Band):
            name = input("Enter Band's name: ")
            band = Band.find_band_by_name(name)
            if isinstance(band, Band):
                print(f"You've selected {band.name}")    

        print('1. To see more about this band, 2. to request an audition, 3. to search for a new band, exit to exit')
        u_input = input('choose a number: ')
        if options_dict.get(u_input):
            band = options_dict[u_input](musician, band)
        elif u_input == 'exit':
            break
        else:
            print('invalid input')

def display_info(musician, band):
    print(f'Some Band info: \n {band.name} \n {band.website}')
    return band

def request_audition(musician, band):
    musician.request_audition(band)
    return band

def new_search(arg1, arg2):
    return None

############ 2. audition request menu#################

def validates_band_name (band_name):
    band_obj = session.query(Band).filter(Band.name == band_name).first()
    if band_obj:
        return band_obj
    else:
        print("Not a valid band name")
        return None
    
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

#############3. manage_profile menu#######################

def manage_profile(musician):
    print("Profile Menu:: press 1. to view your profile or 2. to change your profile \n")
    
    profile_options = {
        '1' : view_profile,
        '2' : change_profile,
    }
    select_input = ''
    while select_input != 'exit':
        select_input = input('Profile Menu:: enter number: ')
        if profile_options.get(select_input):
            profile_options[select_input](musician)
            print('Profile Menu:: select another number or type exit to quit')
        elif select_input == 'exit':
            continue
        else:
            print('please select a valid number or type exit to quit')

def view_profile(musician):
    u_input = None
    while u_input != 'exit':
        print('press a to see all your auditions, i to see your info, exit to exit')
        u_input = input('enter:  ')
        if u_input == 'i':
            musician.show_info
        elif u_input == 'a':
            my_auditions = musician.auditions
            if len(my_auditions) > 0:
                print(f'Your auditions are: \n {my_auditions}')
            else:
                print("sorry, You have no auditions")
        elif u_input == 'exit':
            continue
        else:
            print('not a valid input')        

def change_profile(musician):
    print("Alter Menu:: enter 1. to change your instrument, 2. to change your genre, or exit to exit\n")
    change_options = {'1' : change_instrument,
                      '2' : change_genre}
    select_input = ''
    while select_input != 'exit':
        select_input = input('Alter Menu:: enter number: ')
        if change_options.get(select_input):
           change_options[select_input](musician)
           print('Alter Menu:: select another number or type exit to quit')
        elif select_input == 'exit':
            continue
        else:
            print('please select a valid number or type exit to quit')

############4. information lookup menu#################

def information_lookup(arg1):
    print('The most popular genre for bands is...')
    print(f'{Band.get_most_popular_genre()} \n')
    # most popular genre for bands
    
    print('The most requested instrument by bands is...')
    print(f'{Band.get_most_popular_instrument()} \n')
    # most requested instrument by bands

    print('The top 5 most skilled musicians are...')
    print(f'{Musician.most_skilled_list()} \n')
    # top 5 most skilled musicians