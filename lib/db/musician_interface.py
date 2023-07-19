from models import *
import sys
from cli import exit_program
from dummy import *

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

        print("What is your primary instrument?\n")
        instrument_id = choose_an_instrument()

        print("What genre do you like to play the most?")
        genre_id = choose_a_genre()

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
                '2' : make_audition_request,
                '3' : manage_profile,
                '4' : information_lookup}
    
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
