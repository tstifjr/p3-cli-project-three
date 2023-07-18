from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Column, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine( 'sqlite:///project_three.db' )
Session = sessionmaker( bind = engine )
session = Session()

Base = declarative_base()


class Musician (Base):
    __tablename__ = 'musicians'

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    age = Column(Integer())
    email = Column(String())
    skill_level = Column(Integer())
    location = Column(String())
    instrument_id = Column(Integer(), ForeignKey('instruments.id'))
    genre_id = Column(Integer(), ForeignKey('genres.id'))
    is_looking = Column(Boolean())

class Instrument (Base):
    __tablename__ = 'instruments'

    id = Column(Integer(), primary_key= True)
    name = Column(String())

class Band (Base):
    __tablename__ = 'bands'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    formation_date = Column(String())
    location = Column(String())
    website = Column(String())
    genre_id = Column(Integer(), ForeignKey('genres.id'))
    instrument_id = Column(Integer(), ForeignKey('instruments.id'))
    is_looking = Column(Boolean())

class Genre (Base):
    __tablename__ = 'genres'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __repr__(self):
        return f'Genre: {self.name}, id: {self.id}'

class Audition (Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key=True)
    musician_id = Column(Integer(), ForeignKey('musicians.id'))
    band_id = Column(Integer(), ForeignKey('bands.id'))
    musician_accepts = Column(Boolean())
    band_accepts = Column(Boolean())
