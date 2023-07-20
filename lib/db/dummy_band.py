from models import *
from global_helpers import choose_a_genre, choose_an_instrument, req_aud_from_list

#######################################

#           SEARCH FOR MUSICIANS

######################################

def musician_search_menu(band):
    search_menu_dict = {
        '1' : actively_looking,
        '2' : name_search,
        '3' : genre_search,
        '4' : instrument_search
    }
    while True:
        print('Please select your method of band search.')
        print('''
            1. Actively looking for band to join\n
            2. By name\n
            3. By genre\n
            4. By instrument\n      
            ''')
        menu_selections = input('Please choose a number or type exit to exit: ')
        if menu_selections == "exit":
            break
        elif search_menu_dict.get(menu_selections):
            search_menu_dict[menu_selections](band)
        else:
            print('invalid input')

################           ACTIVELY LOOKING          ############

def actively_looking(band):
    new_input = None
    options_dict = {
        '1' : func_1,
        '2' : func_2,
        '3' : func_3
        }    
    while True:
        print("""
    ╔╦╗┬ ┬┌─┐┬┌─┐┬┌─┐┌┐┌┌─┐  ╦  ┌─┐┌─┐┬┌─┬┌┐┌┌─┐  ╔═╗┌─┐┬─┐  ╔╗ ┌─┐┌┐┌┌┬┐┌─┐
    ║║║│ │└─┐││  │├─┤│││└─┐  ║  │ ││ │├┴┐│││││ ┬  ╠╣ │ │├┬┘  ╠╩╗├─┤│││ ││└─┐
    ╩ ╩└─┘└─┘┴└─┘┴┴ ┴┘└┘└─┘  ╩═╝└─┘└─┘┴ ┴┴┘└┘└─┘  ╚  └─┘┴└─  ╚═╝┴ ┴┘└┘─┴┘└─┘
            """)
        print('1. to see muscians that play the instrument need\n' +
            '2. to see musicians that play your genre\n' +
            '3. to see all musicians\n' +
            '\ntype "exit" to leave this search.\n')
        new_input = input('select number: ')
        print("")
        if new_input == "exit":
            break
        elif options_dict.get(new_input):
            options_dict[new_input](band)
            print('\nsearch some more?')
            new_input = input('[y/n] :')
            if new_input == 'n':
                break
        else :
            print('not a valid input')

def func_1(band):
    print(f"Here are musicians that play {band.instrument.name}\n")
    musician_list = band.musicians_look_same_instr()
    for m in musician_list:
        print(f"{m.name} {m.genre}")
    print("\n")
    req_aud_from_list(band, musician_list)  

def func_2(band):
    print(f"Here are musicians that play {band.genre.name}\n")
    the_list = band.musicians_look_same_genre()
    for m in the_list:
        print(f"{m.name} | {m.instrument.name} | Skill level: {m.skill_level}")
    req_aud_from_list(band, the_list)

def func_3(band):
    looking_list = session.query(Musician).filter(Musician.is_looking == True).all()
    looking_list.sort(key = lambda musician : musician.genre.name) 
    for musician in looking_list:
        print(f"{musician.name} | {musician.instrument.name} | {musician.genre}")
    req_aud_from_list(band, looking_list)
    # input("\nPress any enter to continue: ")


################           NAME SEARCH               ############


def name_search(band):
    while True:
        name = input("Enter the musicians name: ")
        result = Musician.find_musician_by_name(name)
        if isinstance(result, Musician):
            musician_list = [result]
            result.show_info
            req_aud_from_list(band, musician_list)
            print("Would you like to search for a different name? ")
            search_again = input("[y/n]: ")
            if search_again == "n":
                break


################           GENRE SEARCH               ############


def genre_search(band):
    genres = session.query(Genre).all()
    looper = ''
    while looper != "n":
        print("\nPick a Genre:\n")
        genre_selected = choose_a_genre()
        print("")
        results = genres[int(genre_selected) - 1].musicians
        for result in results:
            print(f"{result.name}: {result.instrument}")
        req_aud_from_list(band, results)
        print("")
        looper = input("Search for a different genre? [y/n]: ")


################           INSTRUMENT SEARCH               ############


def instrument_search(band):
    instruments = session.query(Instrument).all()
    looper = ''
    while looper != "n":
        print("\nPick a Instrument:\n")
        instr_selected = choose_an_instrument()
        print("")
        results = instruments[int(instr_selected) - 1].musicians
        for result in results:
            print(f"{result.name} | skill level: {result.skill_level} | Prefers: {result.genre.name}")
        print("")
        req_aud_from_list(band, results)
        looper = input("Search by a different instrument? [y/n]: ")



