from models import session, Genre, Instrument, Musician, Band, Audition
from faker import Faker
import random


genre_list = ['Vampire Rock', 'Time-Traveling Country', 'Space Cowboy R&B', 'Zombie Electronica', 'Galatic Hip Hop', 'Gnome Blues',  'Whiskerwave',  'Disco-Yeti', 'Polka Punk', 'Bubblegum Funk', 'Unicorn Jazz', 'Electro Swingtime', 'Robot Reggae', 'Mermaid Metal', 'Pixie Pop']
instruments = ['Guitar', 'Bass Guitar', 'Drums', 'Vocals', 'Piano', 'Synthesizer', 'Saxophone', 'Harmonica', 'Violin', 'Cow Bell']
band_names = [
    'Electric Snails',
    'Guitar Puppies', 
    'The Thunderous Socks', 
    'Screaming Bananas', 
    'The Rocking Tacos',
    'Rampaging Ravioli',
    'Furious Pickles',
    'The Bouncing Marshmallows', 
    'Rebellious Mustaches',
    'The Shredded Cheese',
    "The Wacky Wallabies",
    "Banana Slammers",
    "Galactic Pickles",
    "Funky Monkeys",
    "Cheese Whizbangs",
    "Electric Eggplants",
    "Dizzy Llamas",
    "Disco Chickens",
    "Polka Dot Pandas",
    "Groovy Guppies",
    "Hula Hoop Hooligans",
    "Jello Jammers",
    "Rubber Duck Rebels",
    "Lava Lamp Legends",
    "Sock Puppet Symphony",
    "Bubblegum Boomerangs",
    "Yodeling Yetis",
    "Fuzzy Nunchucks",
    "Ninja Narwhals",
    "Marshmallow Meteorites",
    "Sushi Samurai",
    "Peanut Butter Penguins",
    "Tofu Tornadoes",
    "Waffle Wombats",
    "Acoustic Armadillos",
    "Zany Zippers",
    "Crispy Cacti",
    "Twirling Tater Tots",
    "Somersaulting Seals",
    "Yawning Yaks"
]

fake = Faker()

if __name__ == '__main__':
    print('hello')
    # print('seeding genres...')
    # session.query(Genre).delete()
    # session.commit()
    # g_list = [Genre(name = genre) for genre in genre_list]
    # session.add_all(g_list)
    # session.commit()

    # print('seeeding instruments...')
    # session.query(Instrument).delete()
    # session.commit()
    # i_list = [Instrument(name = instrument) for instrument in instruments]
    # session.add_all(i_list)
    # session.commit()

    # print('seeding musicians')
    # # session.query(Musician).delete()
    # # session.commit()
    # m_list = []
    # for i in range(1, 71):
    #     if i < 40:
    #         looking = True
    #     else:
    #         looking = random.choice([True, False])
    #     m1 = Musician(name = fake.name(), 
    #               location = fake.address(), 
    #               age = random.randint(16,55), 
    #               skill_level = random.randint(1,5), 
    #               email = fake.email(), 
    #               instrument_id = random.randint(1,len(instruments)),
    #               genre_id = random.randint(1,len(genre_list)),
    #               is_looking = looking)
    #     m_list.append(m1)
    # session.add_all(m_list)
    # session.commit()

    # print('seeding bands')
    # session.query(Band).delete()
    # session.commit()
    # b_list = []
    # for index, band in enumerate(band_names):
    #     if index <= 22:
    #         looking = True
    #     else:
    #         looking = random.choice([True, False])
    #     year = random.randint(1990,2020)
    #     # month = random.randint(1,12)
    #     # date = f'{str(month)} : {str(year)}'
    #     new_band = Band(name = band, 
    #               location = fake.address(), 
    #               formation_date = year, 
    #               website = f'www.{band.replace(" ", "").lower()}.com', 
    #               genre_id = random.randint(1,len(genre_list)),
    #               instrument_id = random.randint(1,len(instruments)),
    #               is_looking = looking)
    #     b_list.append(new_band)
    # session.add_all(b_list)
    # session.commit()


    # print('seeding audition relations')
    # # session.query(Audition).delete()
    # # session.commit()

    # # a1 = Audition(musician_id = 6, band_id = 6, requested_by = "band")
    # # a2 = Audition (musician_id = 11, band_id = 6,requested_by = 'musician')
    # # a3 = Audition (musician_id= 13, band_id = 10, requested_by = 'musician', is_accepted = True)
    # # a4 = Audition (band_id = 1, musician_id = 2, requested_by =  'band', is_accepted = False)
    # # a5 = Audition (band_id = 8, musician_id =3, requested_by = 'band' )

    # # session.add_all([a1, a2, a3, a4, a5])
    # # session.commit()

    # bm_list = []
    # for i in range(1, 40):
    #     i_id = random.randint(1,10)
    #     grab_all_musicians = session.query(Musician.id).filter(Musician.instrument_id == i_id).all()
    #     grab_all_bands = session.query(Band.id).filter(Band.instrument_id == i_id).all()
    #     r_b = random.choice(grab_all_bands)
    #     r_m = random.choice(grab_all_musicians)
    #     request = random.choice(['musician', 'band'])
    #     accept = random.choice([True, False, None])
    #     instance = Audition(band_id = r_b[0], musician_id = r_m[0], requested_by = request, is_accepted = accept )
    #     bm_list.append(instance)
    
    # for i in range(1, 12):
    #     g_id = random.randint(1,15)
    #     grab_all_musicians = session.query(Musician.id).filter(Musician.genre_id == g_id).all()
    #     grab_all_bands = session.query(Band.id).filter(Band.genre_id == g_id).all()
    #     r_b = random.choice(grab_all_bands)
    #     r_m = random.choice(grab_all_musicians)
    #     request = random.choice(['musician', 'band'])
    #     yolo = random.choice([True, False, None])
    #     instance = Audition(band_id = r_b[0], musician_id = r_m[0], requested_by = request, is_accepted = yolo )
    #     bm_list.append(instance)

    # session.add_all(bm_list)
    # session.commit()

    # print('seed one musician')
    # m1 = Musician(name = "Gene Frenkle", 
    #               location = fake.address(), 
    #               age = 42, 
    #               skill_level = 5, 
    #               email = fake.email(), 
    #               instrument_id = 10,
    #               genre_id = 1,
    #               is_looking = True)
    # session.add(m1)
    # session.commit()   