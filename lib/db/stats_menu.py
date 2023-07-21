from models import *

def stats_menu():
#######################################

#           BAND STATS MENU

########################################

    def band_stats():
        print("""
 ____    __    _  _  ____     ___  ____   __   ____  ___ 
(  _ \  /__\  ( \( )(  _ \   / __)(_  _) /__\ (_  _)/ __)
 ) _ < /(__)\  )  (  )(_) )  \__ \  )(  /(__)\  )(  \__ \ 
(____/(__)(__)(_)\_)(____/   (___/ (__)(__)(__)(__) (___/
        """)

        print(f"""



Most Popular Genre
```````````````````
{Band.get_most_popular_genre()}


Instrument Most Needed by Bands
```````````````````````````````
{Band.get_most_popular_instrument()}


Most Auditions
``````````````
{Band.get_band_with_most_auditions()}


Percent of Bands Looking
````````````````````````
{Band.percent_looking_band()}
        

        
        """)

        input("Please [enter] to continue:")

#######################################

#           MUSICIAN STATS MENU

########################################


    def musician_stats():
        print("""
 __  __  __  __  ___  ____  ___  ____    __    _  _    ___  ____   __   ____  ___ 
(  \/  )(  )(  )/ __)(_  _)/ __)(_  _)  /__\  ( \( )  / __)(_  _) /__\ (_  _)/ __)
 )    (  )(__)( \__ \ _)(_( (__  _)(_  /(__)\  )  (   \__ \  )(  /(__)\  )(  \__ \ 
(_/\/\_)(______)(___/(____)\___)(____)(__)(__)(_)\_)  (___/ (__)(__)(__)(__) (___/
        """)

        print(f"""
Most Popular Genre                              
```````````````````                             
{Musician.get_most_popular_genre()}                                       

Most Popular Instrument
````````````````````````
{Musician.get_most_popular_instrument()}

Total Musician by Skills
`````````````````````````
{Musician.skilled_list()}

Most Auditions
``````````````
{Musician.get_musician_with_most_auditions()}

Percent of Bands Looking
````````````````````````
{Musician.percent_looking_musician()}

        """)

        input("Please [enter] to continue:")
#######################################

#           MAIN STATS MENU

########################################

    

    while True:
        print("""



 ___  ____   __   ____  ___    __  __  ____  _  _  __  __ 
/ __)(_  _) /__\ (_  _)/ __)  (  \/  )( ___)( \( )(  )(  )
\__ \  )(  /(__)\  )(  \__ \   )    (  )__)  )  (  )(__)( 
(___/ (__)(__)(__)(__) (___/  (_/\/\_)(____)(_)\_)(______)
        """)
        print("""
        Please select an option:

            1. Band Stats
            2. Musician Stats              



Type [exit] to go back to Main Menu

        """)
        selection = input("Enter a number: ")
        if selection == "1":
            band_stats()
        elif selection == "2":
            musician_stats()
        elif selection == "exit":
            print("\n\n\n\n\n\n")
            break
        else:
            print("Invalid repsonse. Please enter either 1 or 2.")

    