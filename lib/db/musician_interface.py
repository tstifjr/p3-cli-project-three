from models import *
import sys
from cli import exit_program

def fake_func (arg1):
    print("this is an empty function")

def check_musician_name(musician):
    print(f'Is this you? : {musician.name}')
    resp = input('y/n: ')
    if resp == 'y':
        print(f"Welcome, {musician.name}! \n")
        return musician
    elif resp == 'n':
        return None
    else:
        print('invalid response')
        return None
    
def create_new_musician():
    print("Would you like to create a new account?")
    account = input("[y/n]: ")
    if (account == "y" or account == "yes"):
        print("Let's get you set up!")
        first_name = input("First Name: ").rstrip().capitalize()
        last_name = input("Last Name: ").rstrip().capitalize()
        full_name = f"{first_name} {last_name}"
        age = int(input("Age: "))
        email = input("Email: ").rstrip()
        skill = input("Skill Level 1(beginner) - 5(expert): ")
        location = input("Location: ").rstrip()
        instrument_list = session.query(Instrument).all()
        print("What is your primary instrument?\n")
        for instr in instrument_list:
            print(f"{instr.id}. {instr.name}")
        while True:
            instrument_id = int(input("Please enter a number: "))
            if 0 < instrument_id <= len(instrument_list):
                break
            else:
                print(f"Number must be between 1 and {str(len(instrument_list))}")
        print("What genre do you like to play the most?")
        genre_list = session.query(Genre).all()
        for genre in genre_list:
            print(f"{genre.id}. {genre.name}")
        while True:
            genre_id = int(input("Please enter a number: "))
            if 0 < genre_id <= len(genre_list):
                break
            else:
                print(f"Number must be between 1 and {str(len(genre_list))}")
        print("Are you currently looking to join a band?")
        looking = input("[y/n]: ")
        if (looking == "y" or looking =="yes"):
            looking = 1
        else:
            looking = 0
        new_user = Musician(
            name = full_name,
            age = age,
            email = email,
            skill_level = skill,
            location = location,
            instrument_id = instrument_id,
            genre_id = genre_id,
            is_looking = looking
        )
        Musician.save_musician(new_user)
        return new_user


def musician_menu():
    musician = None
    m_menu_dic = {'1' : band_search_menu, #dict to hold functions for each menu option
                '2' : fake_func,
                '3' : fake_func,
                '4' : fake_func}
    
    while True: #initate and stay in Musician Menu
        if not musician: #intro statements
            print("Welcome to the musician's hub!")
            print("Let's see if you're in our database! What is your name?")
        while not isinstance(musician, Musician): #select a musician to be
            name = input("Enter name: ")
            if name == "exit":
                exit_program()
            musician = Musician.find_musician_by_name(name)

            if not musician:
                musician = create_new_musician()
                
            
            if isinstance(musician, Musician):
                musician = check_musician_name(musician)

        #menu options to choose from
        print(""" 
            Please select one of the options bewlow: \n
            1. Search for a band\n
            2. Request audtion\n
            3. View or alter your profile\n
            4. General stats and information\n 
            """)
        
        while True: #loop to select a valid option
            m_menu_select = input("Please enter a number for your choice: ")
            if m_menu_dic.get(m_menu_select):
                m_menu_dic[m_menu_select](musician)
                break
            else: 
                print("Please select a number between 1 and 4")

        print('Would you like to do something else?')
        resp_2 = input('y/n: ')
        if resp_2 == 'n':
            exit_program()

def genre_search():
    genres = session.query(Genre).all()
    looper = ''
    while looper != "no":
        print("Pick a Genre:\n")
        for genre in genres:
            print(f"{genre.id}. {genre.name}")
        genre_selected = input("Enter a number: ")
        print("")
        results = genres[int(genre_selected) - 1].bands
        for result in results:
            print(f"{result.name}")
        print("")
        looper = input("Search for a different genre? [yes or no]: ")


def band_search_menu(musician):
    while True:
        print('Please select your method of band search.')
        print('''
            1. Actively looking for new members.\n
            2. By name\n
            3. By genre\n
            4. By instrument\n
            5. By location       
            ''')
        menu_selections = input('Please choose a number or type quit to exit: ')
        if menu_selections == "quit":
            break
        elif menu_selections == "1":
            pass
        elif menu_selections == "2":
            print("Search for a band by name")
        elif menu_selections == "3":
            genre_search()
        elif menu_selections == "4":
            pass
        elif menu_selections == "5":
            pass