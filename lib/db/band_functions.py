from models import *
from global_helpers import *

#######################################

#           SEARCH FOR MUSICIANS

########################################

def musician_search_menu(band):
    search_menu_dict = {
        '1' : actively_looking,
        '2' : name_search,
        '3' : genre_search,
        '4' : instrument_search
    }
    while True:
        print("""\n\n\n\n\n
        ╔═╗┌─┐┌─┐┬─┐┌─┐┬ ┬  ╔╦╗┌─┐┌┬┐┬ ┬┌─┐┌┬┐
        ╚═╗├┤ ├─┤├┬┘│  ├─┤  ║║║├┤  │ ├─┤│ │ ││
        ╚═╝└─┘┴ ┴┴└─└─┘┴ ┴  ╩ ╩└─┘ ┴ ┴ ┴└─┘─┴┘
        ``````````````````````````````````````
\n\n
              """)
        print('''
            1. Actively looking for band to join\n
            2. By name\n
            3. By genre\n
            4. By instrument\n
\n

Type [exit] to leave this search      
            ''')
        menu_selections = input('Select Number: ')
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
        print("""\n\n\n\n\n
    ╔╦╗┬ ┬┌─┐┬┌─┐┬┌─┐┌┐┌┌─┐  ╦  ┌─┐┌─┐┬┌─┬┌┐┌┌─┐  ╔═╗┌─┐┬─┐  ╔╗ ┌─┐┌┐┌┌┬┐┌─┐
    ║║║│ │└─┐││  │├─┤│││└─┐  ║  │ ││ │├┴┐│││││ ┬  ╠╣ │ │├┬┘  ╠╩╗├─┤│││ ││└─┐
    ╩ ╩└─┘└─┘┴└─┘┴┴ ┴┘└┘└─┘  ╩═╝└─┘└─┘┴ ┴┴┘└┘└─┘  ╚  └─┘┴└─  ╚═╝┴ ┴┘└┘─┴┘└─┘
    ````````````````````````````````````````````````````````````````````````
\n\n
            """)
        print("""
            1. See muscians that play the instrument need

            2. See musicians that play your genre

            3. See all musicians
\n\n

Type [exit] to leave this search

        """)
        new_input = input('Select Number: ')
        print("")
        if new_input == "exit":
            break
        elif options_dict.get(new_input):
            options_dict[new_input](band)
            print('\nsearch some more?')
            new_input = input('\n[y/n] :')
            if new_input == 'n':
                break
        else :
            print('not a valid input')

def func_1(band):
    print(f"\n::::::Here are Musicians That Play {band.instrument.name}::::::\n")
    musician_list = band.musicians_look_same_instr()
    for m in musician_list:
        print(f"{m.name} | Genre: {m.genre.name}")
    print("")
    req_aud_from_list(band, musician_list)  

def func_2(band):
    print(f"\n::::::Here are Musicians That Play {band.genre.name}::::::\n")
    the_list = band.musicians_look_same_genre()
    for m in the_list:
        print(f"{m.name} | {m.instrument.name} | Skill level: {m.skill_level}")
    req_aud_from_list(band, the_list)

def func_3(band):
    print("\n::::::All Musicians Currently Looking::::::\n")
    looking_list = session.query(Musician).filter(Musician.is_looking == True).all()
    looking_list.sort(key = lambda musician : musician.genre.name) 
    for m in looking_list:
        print(f"{m.name} | {m.instrument.name} | Genre: {m.genre.name}")
    req_aud_from_list(band, looking_list)
    # input("\nPress any enter to continue: ")


################           NAME SEARCH               ############

def name_search(band):
    while True:
        name = input("\nEnter the Musician's name: ")
        result = Musician.find_musician_by_name(name)
        if isinstance(result, Musician):
            musician_list = [result]
            result.show_info
            req_aud_from_list(band, musician_list)
            print("\nWould you like to search for a different name? ")
            search_again = input("\n[y/n]: ")
            if search_again == "n":
                break

#######################################

#           REQUEST AUDITION

########################################

def make_audition_request(band):
    print('\nPlease provide the name of the musician you want to audition')
    musician = None
    while not isinstance(musician, Musician):
        musician_input = input("\nMusician's name is:  ")
        musician = Musician.find_musician_by_name(musician_input)
    musician.show_info
    print(f"\nSend audition request to {musician.name}?")
    response = input("\n[y/n]: ")
    if (response == "y" or response == "yes"):
        band.request_audition(musician)
    
