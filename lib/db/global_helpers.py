from models import *
import sys


###############Global esque Functions######################
def exit_program():
    print("Exiting the Program")
    sys.exit(0)

# could be a class method in Instrument?
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
    the_input = input('are you sure you want to change [y/n]')
    if the_input == 'y':
        m_b_object.update_instrument(instrument_id)
        print(f'Your instrument has been changed to {m_b_object.instrument}')
    else:
        print('no changes were made')

#can be used for either musician or band object
def change_genre(m_b_object):
    print(f'Your genre is {m_b_object.genre.name}')
    print(f'select another genre from the list ')
    genre_id = choose_a_genre()
    the_input = input('are you sure you want to change [y/n]')
    if the_input == 'y':
        m_b_object.update_genre(genre_id)
        print(f'Your genre has been changed to {m_b_object.genre}')
    else:
        print('no changes were made')

#can be used for either musician or band object
def instrument_search(b_m_obj):
    string = what_is_string(b_m_obj)
    instruments = Instrument.get_all()
    looper = ''
    while looper != "n":
        print("Pick a Instrument:\n")
        instr_selected = choose_an_instrument()
        print("")
        results = getattr(instruments[int(instr_selected) - 1], string)
        for result in results:
            print(f"{result.name}")
        print("")
        looper = input("Search by a different instrument? [y/n]: ")
        req_aud_from_list(b_m_obj, results)

#can be used for either musician or band object
def genre_search(b_m_obj):
    string = what_is_string(b_m_obj)
    genres = Genre.get_all()
    looper = ''
    results = None
    while looper != "n":
        print("Pick a Genre:\n")
        genre_selected = choose_a_genre()
        print("")
        results = getattr(genres[int(genre_selected) - 1], string)
        for result in results:
            print(f"{result.name}")
        print("")
        looper = input("Search for a different genre? [y/n]: ")
        req_aud_from_list(b_m_obj, results)

#helper for name and genre search
def what_is_string(b_m_obj):
    if isinstance(b_m_obj, Band):
        return 'musicians'
    if isinstance(b_m_obj, Musician):
        return 'bands' 

#can be used for either musician or band object     
def req_aud_from_list(b_m_obj, list_b_or_m):
    if len(list_b_or_m) > 0 :
        print('would you like to request auditions?')
        check_input = input('[y/n]: ')
        if check_input == 'y':
            for result in list_b_or_m:
                print(f'make a request to {result.name}?')
                check_input = input('[y/n]: ')
                if check_input == 'y':
                    b_m_obj.request_audition(result)
                else:
                    print('no request made')
        else :
            print('no request(s) made')