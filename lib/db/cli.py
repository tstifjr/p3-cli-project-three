from models import *
from musician_interface import *
from band_interface import band_menu
from stats_menu import stats_menu




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
    print("Disclaimer: input exit to exit the program at any time")
    print('Are you a musician or a band?')
    x=''
    while not (x == 'm' or x == 'b'):   
        x = input('Press [m] for musician, [b] for band, or [g] for general stats: ')
        if x == 'm':
            musician_menu()
        elif x == 'b':
            band_menu()
        elif x =="g":
            stats_menu()
        else:
            print('Not a valid response!')
