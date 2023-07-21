from models import *
from musician_interface import *
from band_interface import band_menu
from stats_menu import stats_menu




if __name__ == '__main__':
    x=''
    while True:
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
        print("Welcome to C#Harmony! We provide a platform for musicians and bands to find each other and collaborate!\n\n\n\n")
        print('Are you a musician or a band?\n')   
        x = input('Press [m] for musician, [b] for band, [g] for general stats, or [exit] to quit: ')
        if x == 'm':
            musician_menu()
        elif x == 'b':
            band_menu()
        elif x =="g":
            stats_menu()
        elif x == "exit":
            exit_program()
        else:
            print('Not a valid response!')
