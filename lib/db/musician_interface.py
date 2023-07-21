from models import *
from global_helpers import exit_program
from musician_functions import *

def check_musician_name(musician):
    print(f'\nIs this your Name? : {musician.name}')
    resp = input('\ny/n: ')
    if resp == 'y':
        print(f"\n\nWelcome, {musician.name}! \n")
        return musician
    elif resp == 'n':
        return None
    else:
        print('\nInvalid response')
        return None

def create_new_musician():
    print("Would you like to create a new account?\n")
    account = input("[y/n]: ")
    if (account == "y" or account == "yes"):
        print("Let's get you set up!\n")
        first_name = input("First Name: ").rstrip().capitalize()
        last_name = input("Last Name: ").rstrip().capitalize()
        full_name = f"{first_name} {last_name}"
        age = int(input("Age: "))
        email = input("Email: ").rstrip()
        skill = input("Skill Level 1(beginner) - 5(expert): ")
        location = input("Location: ").rstrip()

        print("What is your primary instrument?\n")
        instrument_id = choose_an_instrument()

        print("What genre do you like to play the most?\n")
        genre_id = choose_a_genre()

        print("Are you currently looking to join a band?\n")
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
    m_menu_dic = {
        '1' : band_search_menu, 
        '2' : make_audition_request,
        '3' : manage_profile,
    }
    
    while True: 
        if not musician: #intro statements
            print("""\n\n\n\n
 __  __           _      _               _    _       _     
|  \/  |         (_)    (_)             | |  | |     | |    
| \  / |_   _ ___ _  ___ _  __ _ _ __   | |__| |_   _| |__  
| |\/| | | | / __| |/ __| |/ _` | '_ \  |  __  | | | | '_ \ 
| |  | | |_| \__ \ | (__| | (_| | | | | | |  | | |_| | |_) |
|_|  |_|\__,_|___/_|\___|_|\__,_|_| |_| |_|  |_|\__,_|_.__/ 
```````````````````````````````````````````````````````````
\n\n
            """)
            print("Welcome to the musician hub!")
            print("Let's see if you're in our database! What is your name?\n\n\n\n")
        while not isinstance(musician, Musician): 
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

 _____  _                       __  __       _           _____      _           _   _             
|  __ \| |                     |  \/  |     | |         / ____|    | |         | | (_)            
| |__) | | ___  __ _ ___  ___  | \  / | __ _| | _____  | (___   ___| | ___  ___| |_ _  ___  _ __  
|  ___/| |/ _ \/ _` / __|/ _ \ | |\/| |/ _` | |/ / _ \  \___ \ / _ \ |/ _ \/ __| __| |/ _ \| '_ \ 
| |    | |  __/ (_| \__ \  __/ | |  | | (_| |   <  __/  ____) |  __/ |  __/ (__| |_| | (_) | | | |
|_|    |_|\___|\__,_|___/\___| |_|  |_|\__,_|_|\_\___| |_____/ \___|_|\___|\___|\__|_|\___/|_| |_|
```````````````````````````````````````````````````````````````````````````````````````````````````
\n
            1. Search for a band\n
            2. Request audition\n
            3. View or alter your profile\n
            """)
        
        while True: 
            m_menu_select = input("\n\n\nSelect Number: ")
            if m_menu_dic.get(m_menu_select):
                m_menu_dic[m_menu_select](musician)
                break
            else: 
                print("\nPlease select a number between 1 and 3")

        print('\nWould you like to do something else?')
        resp_2 = input('\n[y/n]: ')
        if resp_2 == 'n':
            break
            # exit_program()
