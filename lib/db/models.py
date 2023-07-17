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

class Instrument (Base):
    __tablename__ = 'instruments'

    id = Column(Integer(), primary_key= True)
    name = Column(String())