from models import *
import sys


###############Global esque Functions######################
def exit_program():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠶⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⣀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠉⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠟⢻⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢸⣧⣶⣿⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠃⠀⢠⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠠⠤⣼⡿⠁⠀⠈⠘⣿⣿⡿⣶⡀⠀⠀⣠⣾⠿⠄⠀⣰⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠿⡟⠳⢿⣁⠀⠀⢀⣼⠟⠀⠈⠘⣷⣠⣾⡟⠁⠀⢀⣼⠏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠁⢀⡁⠀⠀⡍⠛⠶⣾⣇⠀⠀⠀⢠⣿⠟⠃⠈⠂⣠⡾⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⢧⡀⠀⠈⠓⣒⡿⠀⠁⡠⠒⠋⠁⣀⠀⣠⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⠃⠀⣀⣀⣠⠾⢿⣿⡿⠛⢻⠀⣠⣎⡀⠀⠀⠀⢈⣾⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠀⠀⠀⠊⠀⠀⠀⠙⣷⣖⣚⣴⣇⣀⠈⠉⠑⠂⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠘⢿⠋⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣇⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣆⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠏⠙⠒⠀⠀⠤⢯⡀⠀⠀⠀⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣠⣿⡟⠀⠀⠀⢠⠆⠀⡤⠁⠀⠀⠒⢻⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⡹⣿⣿⡿⠁⠀⠀⢀⠏⢀⡞⠁⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣼⢿⣿⣷⣯⣵⣒⣤⡤⣞⣀⣞⡀⠀⠀⠀⠀⣼⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⣯⣤⣠⣿⣿⣿⠿⢿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣷⣿⣿⣿⡿⡀⢠⣿⣿⣿⣿⠉⠙⣿⣿⣿⡟⠻⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣸⣿⠟⠿⣿⣿⣶⣿⣿⣿⣿⣿⣆⣠⣿⣿⣿⣷⣶⠶⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡿⠁⠀⠀⠀⠉⢉⡟⠛⠿⠿⠿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡟⠀⠀⠀⠀⠀⠀⠞⠁⠀⠀⠀⠀⠀⠀⢰⡏⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print("Thanks for Stopping By!")
    sys.exit(0)

# could be a class method in Instrument?
def choose_an_instrument ():
    instrument_list = Instrument.get_all()
    for instr in instrument_list:
        print(f"{instr.id}. {instr.name}")
    print("\n")
    while True:
        instrument_id = int(input("\nSelect Number: "))
        if 0 < instrument_id <= len(instrument_list):
            break
        else:
            print(f"\nNumber ust be between 1 and {str(len(instrument_list))}")
    return instrument_id

def choose_a_genre ():
    genre_list = Genre.get_all()
    for genre in genre_list:
        print(f"{genre.id}. {genre.name}")
    print("\n")
    while True:
        genre_id = int(input("\nSelect Number: "))
        if 0 < genre_id <= len(genre_list):
            break
        else:
            print(f"\nNumber must be between 1 and {str(len(genre_list))}")
    return genre_id

#can be used for either musician or band object
def change_instrument(m_b_object):
    print(f'\n\nYour instrument is {m_b_object.instrument.name}')
    print(f'\nSelect Instrument\n')
    instrument_id = choose_an_instrument()
    the_input = input('\nConfirm Change? [y/n]: ')
    if the_input == 'y':
        m_b_object.update_instrument(instrument_id)
        print(f'\nYour Instrument Has Been Changed to {m_b_object.instrument.name}\n')
    else:
        print('\nNo Changes Were Made\n')

#can be used for either musician or band object
def change_genre(m_b_object):
    print(f'\nYour Genre is {m_b_object.genre.name}')
    print(f'\nSelect Genre\n')
    genre_id = choose_a_genre()
    the_input = input('\nConfirm Change? [y/n]: ')
    if the_input == 'y':
        m_b_object.update_genre(genre_id)
        print(f'\nYour Genre Has Been Changed to {m_b_object.genre.name}\n')
    else:
        print('\nNo Changes Were Made\n')

#can be used for either musician or band object
def instrument_search(b_m_obj):
    string = what_is_string(b_m_obj)
    instruments = Instrument.get_all()
    looper = ''
    while looper != "n":
        print("\nPick a Instrument:\n")
        instr_selected = choose_an_instrument()
        print("")
        results = getattr(instruments[int(instr_selected) - 1], string)
        for result in results:
            print(f"{result.name}")
        print("")
        looper = input("\nSearch by a different instrument? [y/n]: ")
        req_aud_from_list(b_m_obj, results)

#can be used for either musician or band object
def genre_search(b_m_obj):
    string = what_is_string(b_m_obj)
    genres = Genre.get_all()
    looper = ''
    results = None
    while looper != "n":
        print("\nPick a Genre:\n")
        genre_selected = choose_a_genre()
        print("")
        results = getattr(genres[int(genre_selected) - 1], string)
        for result in results:
            print(f"{result.name}")
        print("")
        looper = input("\nSearch for a different genre? [y/n]: ")
        req_aud_from_list(b_m_obj, results)

#helper for name and genre search
def what_is_string(b_m_obj):
    if isinstance(b_m_obj, Band):
        return 'musicians'
    if isinstance(b_m_obj, Musician):
        return 'bands' 

#can be used for either musician or band object     
def req_aud_from_list(b_m_obj, list_b_or_m):
    print("")
    if len(list_b_or_m) > 0 :
        print('Would you like to request auditions?')
        check_input = input('\n[y/n]: ')
        if check_input == 'y':
            for result in list_b_or_m:
                print(f'\nMake a request to {result.name}?')
                check_input = input('\n[y/n]: ')
                if check_input == 'y':
                    b_m_obj.request_audition(result)
                else:
                    print('No request made')
        else :
            print('\nNo request(s) made')

#############3. manage_profile menu#######################

def manage_profile(data_object):    
    profile_options = {
        '1' : view_profile,
        '2' : change_profile,
        '3' : pending_aud_request,
        '4' : pending_audition,
        '5' : audition_cleanup
    }
    select_input = ''

    while select_input != 'exit':
        print("""\n\n
            ::::::Profile Menu::::::
            
            1. View Your Profile
            2. Change Your Profile
            3. See Pending Requests
            4. See Upcoming Auditions
            5. Remove Completed Auditions
\n
Type [exit] to exit

            """)
        while True:
            select_input = input('\nSelect Number: ')
            if profile_options.get(select_input):
                profile_options[select_input](data_object)
                # select_input = input("Tpye [enter] to continue or [exit] to exit")
                break
            elif select_input == 'exit':
                break
            else:
                print('\nPlease select a valid number or type [exit] to quit')

def view_profile(data_object):
    data_object.show_info
    print("\n\n")

def change_profile(data_object):
    change_options = {'1' : change_instrument,
                      '2' : change_genre}
    select_input = ''
    while select_input != 'exit':
        print("""
            ::::::Alter Menu::::::
            
            1. To Change Your Instrument 
            2. To Change Your Genre
\n            
Type [exit] to exit\n""")
        select_input = input('Enter Number: ')
        if change_options.get(select_input):
           change_options[select_input](data_object)
           select_input = input("Type [enter] to continue or [exit] to exit: ")
        elif select_input == 'exit':
            continue
        else:
            print('\nPlease select a valid number')

def pending_aud_request(data_object):
    sent_requests_status = data_object.sent_requests_status
    incoming_requests = data_object.pending_requests
    print(f'\nStatus of requests sent by {data_object.name}:')
    if isinstance(sent_requests_status, list):
        for request in sent_requests_status:
            if request[1] == True:
                print(f"\n{request[0]} | Status: ACCEPTED")
            elif request[1] == False:
                print(f"\n{request[0]} | Status: REJECTED")
            else:
                print(f"\n{request[0]} | Status: PENDING")
    else:
        print(f"\n{sent_requests_status}")
    u_input = input('\nPress [enter] to continue: ')
    func_response = what_is_string(data_object)
    print(f'\nIncoming requests from {func_response}: \n')
    if isinstance(incoming_requests, list):
        for request in incoming_requests:
            print(f"{request[0].name} | Instrument: {request[0].instrument.name} | Genre: {request[0].genre.name}")
        u_input = input('\nPress [m] to manage incoming requests or [enter] to continue: ')
        if u_input == 'm':
            for request in incoming_requests:
                b_m_obj = request[0]
                req_audition = request[1]
                b_m_obj.show_info
                print(f'\nAccept request from {b_m_obj.name}?')
                u_input = input('\n[y/n] or [enter] to pass: ')
                if u_input == 'y':
                    req_audition.update_accepted(status = True)
                    print(f'\n{b_m_obj.name} has been accepted')
                elif u_input == 'n':
                    req_audition.update_accepted(status = False)
                    print(f'\n{b_m_obj.name} has been declined')
                else:
                    print(f"\nPassed: {b_m_obj.name}'s request is still pending")
            print('\nAll requests taken care of.')
    else:
        print(incoming_requests)
    input("\nPress [enter] to continue: ")


def pending_audition(data_object):
    my_auditions = data_object.upcoming_auditions
    print('\nYour upcoming auditions are:')
    if len(my_auditions) > 0:
        for audition in my_auditions :
            print(f"\n{audition[1].musician.name} has an audition with {audition[1].band.name}")
    else:
        print("No upcoming auditions")
    input("\nPress [enter] to continue: ")

def audition_cleanup(data_object):
    options_dict = {'1' : del_1,
                    '2' : del_2,
                    '3' : del_3}
    print("""\n\n
        1. Delete all rejected requests 
        2. Delete completed auditions
        3. Delete all auditions
    """)
    resp = input('\nSelect Number: ')
    while True:
        if options_dict.get(resp):
            options_dict[resp](data_object)
            break
        else:
            print('\nInvalid input')
    
def del_1 (data_object):
    rejected_requests = data_object.rejected_requests
    if len(rejected_requests) > 0 :
        print('\nAre you sure you want to delete?')
        for audition in rejected_requests:
            if isinstance(data_object, Band):
                print(f"\n{audition.musician.name} has rejected audition.")
            else:
                print(f"\n{audition.band.name} has rejected audition.")
        resp = input('\nType [y] to delete or press [enter] to keep: ')
        if resp == 'y':
            data_object.del_rej_aud_all
            print('\nRequests deleted...')
    else:
        print('\nSorry, looks like there are no requests')
    input("\n\nPress [enter] to continue: ")

def del_2 (data_object):
    my_auditions = data_object.upcoming_auditions
    if len(my_auditions) > 0 :
        for audition in my_auditions:
            print(f'\nAudition with: {audition[0]} has happend?')
            resp = input('\n[y/n]: ')
            if resp == 'y':
                print('\nOkay to delete?')
                resp = input('\n[y/n]: ')
                if resp == 'y':
                    data_object.del_sing_aud(audition[1])
                    print('\nDELETED')
                else:
                    print('\nNOT DELETED')
            else:
                print('\nAudition has not occured')
    else:
        print('\nSorry, looks like there are no requests')
    input("\n\nPress [enter] to continue: ")

def del_3 (data_object):
    print('\nAre you sure you want to delete all your auditions?')
    resp = input('\n[y/n]: ')
    if resp == "y":
        data_object.del_all_aud
    input("\n\nPress [enter] to continue: ")