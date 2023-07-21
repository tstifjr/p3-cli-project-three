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
    print("\n")
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
    print("\n")
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
    print("")
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
        print("Profile Menu:: \n" +
              "  1. to view your profile \n" +
              "  2. to change your profile \n" +
              "  3. see pending requests \n" +
              "  4. see upcoming auditions \n" +
              "  5. remove completed auditions \n")
        while True:
            select_input = input('Profile Menu:: enter number: ')
            if profile_options.get(select_input):
                profile_options[select_input](data_object)
                select_input = input("Profile Menu:: enter to continue or exit to quit")
                break
            elif select_input == 'exit':
                break
            else:
                print('please select a valid number or type exit to quit')

def view_profile(data_object):
    print('!!!!YOUR PROFILE!!!!')
    data_object.show_info

def change_profile(data_object):
    change_options = {'1' : change_instrument,
                      '2' : change_genre}
    select_input = ''
    while select_input != 'exit':
        print("Alter Menu:: enter 1. to change your instrument, 2. to change your genre, or exit to exit\n")
        select_input = input('Alter Menu:: enter number: ')
        if change_options.get(select_input):
           change_options[select_input](data_object)
           select_input = input("Profile Menu:: enter to continue or exit to quit")
        elif select_input == 'exit':
            continue
        else:
            print('please select a valid number or type exit to quit')

def pending_aud_request(data_object):
    sent_requests_status = data_object.sent_requests_status
    incoming_requests = data_object.pending_requests

    print('Status of sent requests is:')
    print(sent_requests_status)
    u_input = input('press enter to continue:: ')
    print('Incoming requests requests are:')
    print(incoming_requests)
    print('Press 1 to manage incoming requests')
    u_input = input(':: ')
    if u_input == '1':
        for request in incoming_requests:
            req_audition = request[1]
            print(request[1])
            print(f'Accept request from {request[0]}?')
            u_input = input('[y/n] or enter to pass: ')
            if u_input == 'y':
                req_audition.update_accepted(status = True)
                print(f'{request[0]} has been accepted')
            elif u_input == 'n':
                req_audition.update_accepted(status = False)
                print(f'{request[0]} has been declined')
            else:
                print(f'passed: {request[0]} still pending')
        print('All requests taken care of.')


def pending_audition(data_object):
    my_auditions = data_object.upcoming_auditions
    print('Your upcoming auditions are:')
    for audition in my_auditions :
        print(audition[1])

def audition_cleanup(data_object):
    options_dict = {'1' : del_1,
                    '2' : del_2,
                    '3' : del_3}
    print('press 1 to delete all rejected requests, 2 to delete completed auditions, and all to delete all auditions')
    resp = input(':: ')
    while True:
        if options_dict.get(resp):
            options_dict[resp](data_object)
            break
        else:
            print('invalid input')
    
def del_1 (data_object):
    rejected_requests = data_object.rejected_requests
    if len(rejected_requests) > 0 :
        print('Are you sure you want to delete?')
        print(rejected_requests)
        resp = input('y to delete: ')
        if resp == 'y':
            data_object.del_rej_aud_all
            print('requests deleted...')
    else:
        print('Sorry, looks like there are no requests')

def del_2 (data_object):
    my_auditions = data_object.upcoming_auditions
    if len(my_auditions) > 0 :
        for audition in my_auditions:
            print(f'Audition with: {audition[0]} has happend?')
            resp = input('[y/n]: ')
            if resp == 'y':
                print('okay to delete?')
                resp = input('[y/n]: ')
                if resp == 'y':
                    data_object.del_sing_aud(audition[1])
                    print('deleted')
                else:
                    print('not deleted')
            else:
                print('Audition has not occured')

def del_3 (data_object):
    print('Are you sure you want to delete all your auditions?')
    resp = input('[y/n]: ')
    if resp == "y":
        data_object.del_all_aud