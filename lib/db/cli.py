from models import *
from functions import *
import sys

def exit_program():
    print("Exiting the Program")
    sys.exit(0)

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
        while not musician: #select a musician to be
            name = input("Enter name: ")
            musician = Musician.find_musician_by_name(name)
            if musician:
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

def band_menu():
    while True:
        print("Welcome to the band hub!")
        break

if __name__ == '__main__':
    print(
        '''
   ______  __ __  __  __                                          
  / ____/_/ // /_/ / / /___ __________ ___  ____  ____  __  __    
 / /   /_  _  __/ /_/ / __ `/ ___/ __ `__ \/ __ \/ __ \/ / / /    
/ /___/_  _  __/ __  / /_/ / /  / / / / / / /_/ / / / / /_/ /     
\____/ /_//_/ /_/ /_/\__,_/_/  /_/ /_/ /_/\____/_/ /_/\__, /      
                                                     /____/  
'''
    )

    print('Are you a musician or a band?')
    x=''
    while not (x == 'm' or x == 'b'):   
        x = input('Press m for musician or press b for band: ')
        if x == 'm':
            musician_menu()
        elif x == 'b':
            band_menu()
        else:
            print('Not a valid response!')

        
        

        


    
            

    