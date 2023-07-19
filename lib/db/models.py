from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Column, Boolean, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine( 'sqlite:///project_three.db' )
Session = sessionmaker( bind = engine )
session = Session()


convention = {
    'fk' : 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
}

md = MetaData(naming_convention = convention)

Base = declarative_base(metadata = md)

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

    auditions = relationship('Audition', back_populates='musician')
    bands = association_proxy('auditions', 'band')

    def __repr__(self):
        return f'< Musician: {self.name}, instrument: {self.instrument.name} >'
   


class Instrument (Base):
    __tablename__ = 'instruments'

    id = Column(Integer(), primary_key= True)
    name = Column(String())

    musicians = relationship('Musician', backref = 'instrument')
    bands = relationship("Band", backref = 'instrument')

    def __repr__(self):
        return f'< Instrument: {self.name} >'
    
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

    auditions = relationship("Audition", back_populates = "band")
    musicians = association_proxy('auditions', 'musician')
    

    def __repr__(self):
        return f'< Band: {self.name}, genre: {self.genre.name} >'
    
class Genre (Base):
    __tablename__ = 'genres'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    musicians = relationship('Musician', backref = 'genre')
    bands = relationship("Band", backref = 'genre')
    
    
    def __repr__(self):
        return f'< Genre: {self.name} >'

class Audition (Base):
    __tablename__ = 'auditions'

    id = Column(Integer(), primary_key=True)
    musician_id = Column(Integer(), ForeignKey('musicians.id'))
    band_id = Column(Integer(), ForeignKey('bands.id'))
    requested_by = Column(String())
    is_accepted = Column(Boolean())

    musician = relationship('Musician', back_populates='auditions')
    band = relationship("Band", back_populates="auditions")

    def __repr__(self):
        return f'< Musician {self.musician.name} auditioned for {self.band.name} >'
