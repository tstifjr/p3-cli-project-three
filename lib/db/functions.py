from models import *

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