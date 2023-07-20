from models import *
from global_helpers import choose_a_genre, choose_an_instrument

#######################################

#           SEARCH FOR MUSICIANS

######################################
def genre_search():
    genres = session.query(Genre).all()
    looper = ''
    while looper != "n":
        print("Pick a Genre:\n")
        genre_selected = choose_a_genre()
        print("")
        results = genres[int(genre_selected) - 1].musicians
        for result in results:
            print(f"{result.name}")
        print("")
        looper = input("Search for a different genre? [y/n]: ")

def name_search():
    while True:
        name = input("Enter the musicians name: ")
        result = Musician.find_musician_by_name(name)
        if isinstance(result, Musician):
            result.show_info
            print("Would you like to search for a different name? ")
            search_again = input("[y/n]: ")
            if search_again == "n":
                break
            

def instrument_search():
    instruments = session.query(Genre).all()
    looper = ''
    while looper != "n":
        print("Pick a Instrument:\n")
        instr_selected = choose_an_instrument()
        print("")
        results = instruments[int(instr_selected) - 1].musicians
        for result in results:
            print(f"{result.name}")
        print("")
        looper = input("Search by a different instrument? [y/n]: ")

def actively_looking():
    looking_list = session.query(Musician).filter(Musician.is_looking == True).all()
    looking_list.sort(key = lambda musician : musician.genre.name) 
    for musician in looking_list:
        print(f"{musician.name} {musician.genre}")
    input("\nPress any key to continue: ")

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
            5. By location       
            ''')
        menu_selections = input('Please choose a number or type exit to exit: ')
        if menu_selections == "exit":
            break
        elif search_menu_dict.get(menu_selections):
            search_menu_dict[menu_selections]()
        else:
            print('invalid input')