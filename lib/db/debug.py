# from models import session, Band, engine, Base, Genre
from models import *

musicians = session.query(Musician).all()
bands = session.query(Band).all()
auditions = session.query(Audition).all()









import ipdb; ipdb.set_trace()