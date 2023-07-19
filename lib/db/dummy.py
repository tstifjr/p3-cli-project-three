from models import *
import sys
# from cli import exit_program

###############Global esque Functions######################
#global function
def choose_an_instrument ():
    instrument_list = Instrument.get_all()
    for instr in instrument_list:
        print(f"{instr.id}. {instr.name}")
    while True:
        instrument_id = int(input("Please enter a number: "))
        if 0 < instrument_id <= len(instrument_list):
            break
        else:
            print(f"Number must be between 1 and {str(len(instrument_list))}")
    return instrument_id

#global function
def choose_a_genre ():
    genre_list = Genre.get_all()
    for genre in genre_list:
        print(f"{genre.id}. {genre.name}")
    while True:
        genre_id = int(input("Please enter a number: "))
        if 0 < genre_id <= len(genre_list):
            break
        else:
            print(f"Number must be between 1 and {str(len(genre_list))}")
    return genre_id

#can be used for either musician or band object
def change_instrument(m_b_object):
    print(f'Your instrument is {m_b_object.instrument.name}')
    print(f'select another insturment from the list ')
    instrument_id = choose_an_instrument()
    m_b_object.update_instrument(instrument_id)
    print(f'Your instrument has been changed to {m_b_object.instrument}')

#can be used for either musician or band object
def change_genre(m_b_object):
    print(f'Your genre is {m_b_object.genre.name}')
    genre_id = choose_a_genre()
    m_b_object.update_genre(genre_id)
    print(f'Your instrument has been changed to {m_b_object.genre}')

#############manage_profile menu#######################
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

####################################################




############audition request menu#################

def validates_band_name (band_name):
    band_obj = session.query(Band).filter(Band.name == band_name).first()
    if band_obj:
        return band_obj
    else:
        print("Not a valid band name")
        return None
    
def make_audition_request(musician):
    print('Please provide the name of the band you want to audition for')
    band_is_valid = None
    while not band_is_valid:
        band_input = input('band name is:  ')
        band_is_valid = validates_band_name(band_input)
    musician.request_audition(band_is_valid)
    #can make this a instance method of musician


############information lookup menu#################

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


#############search menus ####################
def band_search_menu(musician):
    search_menu_dict = {
        '1' : actively_looking,
        '2' : name_search,
        '3' : genre_search,
        '4' : instrument_search
    }
    while True:
        print('Please select your method of band search.')
        print('''
            1. Actively looking for new members.\n
            2. By name\n
            3. By genre\n
            4. By instrument    
            ''')
        menu_selections = input('Please choose a number or type quit to exit: ')
        if menu_selections == "quit":
            break
        elif search_menu_dict.get(menu_selections):
            search_menu_dict[menu_selections](musician)
        else:
            print('invalid input')

def genre_search(arg1):
    genres = Genre.get_all()
    looper = ''
    while looper != "n":
        print("Pick a Genre:\n")
        genre_selected = choose_a_genre()
        print("")
        results = genres[int(genre_selected) - 1].bands
        for result in results:
            print(f"{result.name}")
        print("")
        looper = input("Search for a different genre? [y/n]: ")

def name_search(musician):
    from band_interface import check_band_name
    band = None
    u_input = None
    do_search = False
    options_dict = {
    '1' : display_info,
    '2' : request_audition,
    '3' : new_search
    }

    print('Please Enter the name of the Band to search for')
    while u_input != 'exit':
        while not isinstance(band, Band) or do_search == True:
            do_search = False
            name = input("Enter name: ")
            # if name == "exit":
            #     exit_program()
            band = Band.find_band_by_name(name)
            
            if isinstance(band, Band):
                band = check_band_name(band)    
   
        print('1. To see more about this band, 2. to request an audition, 3. to search for a new band, exit to exit')
        u_input = input('choose a number: ')
        if options_dict.get(u_input):
            do_search = options_dict[u_input](musician, band)
        elif u_input == 'exit':
            continue
        else:
            print('invalid input')

def display_info(musician, band):
    print(f'Some Band info: \n {band.name} \n {band.website}')
    return False

def request_audition(musician, band):
    musician.request_audition(band)
    return False

def new_search(arg1, arg2):
    return True

def instrument_search(arg1):
    print('is instrument search')
    instruments = Instrument.get_all()
    looper = ''
    while looper != "n":
        print("Pick an Instrument:\n")
        inst_selected = choose_an_instrument()
        print("")
        results = instruments[int(inst_selected) - 1].bands
        for result in results:
            print(f"{result.name}")
        print("")
        looper = input("Search for a different genre? [y/n]: ")    

def actively_looking():
    print('these bands are looking for members')

#############################