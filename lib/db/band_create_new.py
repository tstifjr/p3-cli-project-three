from models import *
from global_helpers import choose_an_instrument, choose_a_genre

def create_new_band():
    print("Would you like to create a new account?\n")
    account = input("[y/n]: ")
    if (account == "y" or account == "yes"):
        print("Let's get you set up!\n")
        band_name = input("Band Name: ").rstrip().capitalize()
        formation_date = int(input("What year did the band form: "))
        website = input("Band website: ").rstrip()
        location = input("Location: ").rstrip()

        print("What role are you trying to fill?\n")
        instrument_id = choose_an_instrument()

        print("What is the primary genre you play?\n")
        genre_id = choose_a_genre()

        print("Are you currently looking for a new band member?\n")
        looking = input("[y/n]: ")
        if (looking == "y" or looking =="yes"):
            looking = 1
        else:
            looking = 0
        new_user = Band(
            name = band_name,
            formation_date = formation_date,
            website = website,
            location = location,
            instrument_id = instrument_id,
            genre_id = genre_id,
            is_looking = looking
        )
        Band.save_band(new_user)
        return new_user