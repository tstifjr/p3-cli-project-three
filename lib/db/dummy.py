from models import *
import sys
# from cli import exit_program

#############manage_profile functions#######################
def manage_profile(musician):
    print("Profile Menu:: press 1. to view your profile or 2. to change your profile \n")
    
    profile_options = {
        '1' : view_profile,
        '2' : change_profile,
        '3' : information_lookup,
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
    print("YOUR PROFILE \n::::::::::::::::::::::")
    print(f':: Name: {musician.name}\n' +
          f':: Instrument: {musician.instrument.name}\n' +
          f':: Genre: {musician.genre.name}\n' +
          f':: skill lvl: {musician.skill_level}\n' +
        #   f':: {musician.location}\n' +
          f':: email: {musician.email}\n::::::::::::::::::::::')
    print('press a to see all your auditions')
    u_input = input('enter:  ')
    if u_input == 'a':
        my_auditions = musician.auditions
        if len(my_auditions) > 0:
            print(f'Your auditions are: \n {my_auditions}')
        else:
            print("sorry, You have no auditions")        

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

def change_profile(musician):
    print("Alter Menu:: enter 1. to change your instrument or 2. to change your genre \n")
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

####################################################




############audition request functions#################

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
    band_id = band_is_valid.id
    print(band_id, musician.id)
    musician.request_audition(band_id)
    #can make this a instance method of musician


####################################################


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