from models import session, Genre, Instrument, Musician, Band, Audition
from faker import Faker
import random


genre_list = ['Rock', 'Pop', 'Hip Hop', 'Country', 'Jazz', 'R&B', 'Electronic', 'Classical', 'Reggae', 'Metal']
instruments = ['Electric Guitar', 'Bass Guitar', 'Drums', 'Keyboard', 'Vocals', 'Acoustic Guitar', 'Piano', 'Synthesizer', 'Saxophone', 'Harmonica']
band_names = ['Electric Snails', 'Guitar Puppies', 'The Thunderous Socks', 'Screaming Bananas', 'The Rocking Tacos', 'Rampaging Ravioli', 'Furious Pickles', 'The Bouncing Marshmallows', 'Rebellious Mustaches', 'The Shredded Cheese']
fake = Faker()

if __name__ == '__main__':

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
    # session.query(Musician).delete()
    # session.commit()
    # m_list = []
    # for i in range(1, 16):
    #     if i <= 10:
    #         looking = True
    #     else:
    #         looking = False
    #     m1 = Musician(name = fake.name(), 
    #               location = fake.address(), 
    #               age = random.randint(16,55), 
    #               skill_level = random.randint(1,5), 
    #               email = fake.email(), 
    #               instrument_id = random.randint(1,10),
    #               genre_id = random.randint(1,10),
    #               is_looking = looking)
    #     m_list.append(m1)
    # session.add_all(m_list)
    # session.commit()

    # print('seeding bands')
    # session.query(Band).delete()
    # session.commit()
    # b_list = []
    # for index, band in enumerate(band_names):
    #     if index <= 6:
    #         looking = True
    #     else:
    #         looking = False
    #     year = random.randint(1990,2020)
    #     month = random.randint(1,12)
    #     date = f'{str(month)} : {str(year)}'
    #     new_band = Band(name = band, 
    #               location = fake.address(), 
    #               formation_date = date, 
    #               website = f'www.{band.replace(" ", "").lower()}.com', 
    #               genre_id = random.randint(1,10),
    #               instrument_id = random.randint(1,10),
    #               is_looking = looking)
    #     b_list.append(new_band)
    # session.add_all(b_list)
    # session.commit()


    print('seeding audition relations')
    session.query(Audition).delete()
    session.commit()
    # bm_list = []
    # for i in range(1, 16):
    #     bid = random.randint(1,7)
    #     mid = random.randint(1,10)
    #     instance = Audition(band_id = bid, musician_id = mid)
    #     bm_list.append(instance)
    # session.add_all(bm_list)
    # session.commit()