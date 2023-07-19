from models import *
from functions import *



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
    def musician_menu():
        while True:
            musician = None
            print("Welcome to the musician's hub!")
            print("Let's see if you're in our database! What is your name?")
            while True:
                name = input("Enter name: ")
                musician_list = session.query(Musician).filter(Musician.name.like(f'%{name}%')).all()
                if len(musician_list) > 1:
                    print("More than one record found. Please provide a full name.")
                elif len(musician_list) == 0:
                    print("No records found")
                else:
                    musician = musician_list[0]
                    break
            print(f"Welcome, {musician.name}!")
            while True:
                print("""
                    Please select one of the options bewlow: \n
                    1. Search for a band\n
                    2. Request audtion\n
                    3. View or alter your profile\n
                    4. General stats and information\n 
                    """)
                m_menu_select = input("Please enter a number for your choice: ")
                if m_menu_select == '1':
                    band_search_menu(musician)
                    break
                if m_menu_select == '2':
                    break
                if m_menu_select == '3':
                    break
                if m_menu_select == '4':
                    break
                else:
                    print("Please select a number between 1 and 4")
            break
        

    def band_menu():
        while True:
            print("Welcome to the band hub!")
            break

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

        
        

        


    
            

    