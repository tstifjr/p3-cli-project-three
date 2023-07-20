from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Column, Boolean, ForeignKey, MetaData, desc
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
    
    @property
    def show_info(self):
        print("::::::::::::::::::::::")
        print(f':: Name: {self.name}\n' +
          f':: Instrument: {self.instrument.name}\n' +
          f':: Genre: {self.genre.name}\n' +
          f':: skill lvl: {self.skill_level}\n' +
          #   f':: {musician.location}\n' +
          f':: email: {self.email}\n::::::::::::::::::::::')
        
    @classmethod
    def find_musician_by_name(cls, name):
        musician_list = session.query(cls).filter(cls.name.like(f'%{name}%')).all()
        if len(musician_list) == 0:
            print("No records found")
            return None
        elif len(musician_list) > 1:
            print("More than one record found. Please provide a full name.")
            return musician_list
        else:
            return musician_list[0]
        
    @classmethod
    def save_musician(cls, musician):
        session.add(musician)
        session.commit()
    
    def request_audition(self, band):
        a = Audition(musician_id = self.id, band_id = band.id, requested_by = 'musician')
        session.add(a)
        session.commit()
        print("your auditon request has been made !!!")

    @classmethod
    def most_skilled_list(cls):
        output = session.query(Musician.name, Musician.skill_level).order_by(desc(Musician.skill_level)).limit(5).all()
        return output
    
    @classmethod
    def get_most_popular_instrument (cls):
        my_list = session.query(Instrument).join(cls).filter(Instrument.id == cls.instrument_id).all()
        is_sorted = sorted(my_list, key = lambda el : len(el.musicians), reverse = True)
        return is_sorted[0].name
    
    @classmethod
    def get_most_popular_genre (cls):
        my_list = session.query(Genre).join(cls).filter(Genre.id == cls.genre_id).all()
        is_sorted = sorted(my_list, key = lambda el : len(el.musicians), reverse = True)
        return is_sorted[0].name
    
    def update_instrument(self, i_id):
        self.instrument_id = i_id
        query_self = session.query(Musician).filter(self.id == Musician.id).first()
        query_self.instrument_id = i_id
        session.commit()

    def update_genre(self, g_id):
        self.genre_id = g_id
        query_self = session.query(Musician).filter(self.id == Musician.id).first()
        query_self.genre_id = g_id
        session.commit()

    def bands_look_same_instr(self):
        query_a = session.query(Band).filter(Band.is_looking == True)
        query_b = session.query(Band).filter(Band.instrument_id == self.instrument_id)
        return query_a.intersect(query_b).all()

    def bands_look_same_genre(self):
        query_a = session.query(Band).filter(Band.is_looking == True)
        query_c = session.query(Band).filter(Band.genre_id == self.genre_id)
        return query_a.intersect(query_c).all()
    
    @property
    def pending_requests(self):
        query = session.query(Band.name, Audition).join(Audition).filter(Audition.is_accepted == None, Audition.requested_by == 'band')
        return query.all()

    @property
    def sent_requests_status(self):
        query  = session.query(Band.name, Audition.is_accepted).join(Audition).filter(Audition.requested_by  == 'musician')
        return query.all()

    @property
    def upcoming_auditions(self):
        query = session.query(Band.name).join(Audition).filter(Audition.is_accepted == True)
        return query.all()
    
    @property
    def rejected_requests(self):
        query = session.query(Audition).filter(Audition.is_accepted == False)
        return query.all()
    
    # def delete_rejected_requests(self, audition_list):
    #     session.delete(audition_list)
    #     session.commit()
    
class Instrument (Base):
    __tablename__ = 'instruments'

    id = Column(Integer(), primary_key= True)
    name = Column(String())

    musicians = relationship('Musician', backref = 'instrument')
    bands = relationship("Band", backref = 'instrument')

    def __repr__(self):
        return f'< Instrument: {self.name} >'
    
    @classmethod
    def get_all(cls):
        list_all = session.query(cls).all()
        return list_all

    
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
    
    @classmethod
    def find_band_by_name(cls, name):
        band_list = session.query(cls).filter(cls.name.like(f'%{name}%')).all()
        if len(band_list) == 0:
            print("No records found")
            return None
        elif len(band_list) > 1:
            print("More than one record found. Please provide the full band name.")
            return band_list
        else:
            return band_list[0]

    @classmethod
    def save_band(cls, band):
        session.add(band)
        session.commit()

    @classmethod
    def get_most_popular_genre (cls):
        my_list = session.query(Genre).join(cls).filter(Genre.id == cls.genre_id).all()
        is_sorted = sorted(my_list, key = lambda el : len(el.bands), reverse = True)
        return is_sorted[0].name
    
    @classmethod
    def get_most_popular_instrument (cls):
        my_list = session.query(Instrument).join(cls).filter(Instrument.id == cls.instrument_id).all()
        is_sorted = sorted(my_list, key = lambda el : len(el.bands), reverse = True)
        return is_sorted[0].name
    
    @classmethod
    def bands_looking (cls):
        query_a = session.query(Band).filter(Band.is_looking == True)
        return query_a.all()
    
    @property
    def show_info(self):
        print(f"")
        print(f"""
:::::::::::: {self.name} :::::::::::::::::::
:::
::: Website:            {self.website}
::: Established:        {self.formation_date}
::: Preferred Genre:    {self.genre.name}
::: Instrument Needed:  {self.instrument.name}
::: Currently Looking:  {self.is_looking}
::: Location:           {self.location}
:::
:::::::::::::::::::::::::::::::::::::::::::::::::::
""")

    def request_audition(self, musician):
        a = Audition(musician_id = musician.id, band_id = self.id, requested_by = 'band')
        session.add(a)
        session.commit()
        print("your auditon request has been made !!!")

    def musicians_look_same_instr(self):
        query_a = session.query(Musician).filter(Musician.is_looking == True)
        query_b = session.query(Musician).filter(Musician.instrument_id == self.instrument_id)
        return query_a.intersect(query_b).all()
    
    def musicians_look_same_genre(self):
        query_a = session.query(Musician).filter(Musician.is_looking == True)
        query_c = session.query(Musician).filter(Musician.genre_id == self.genre_id)
        return query_a.intersect(query_c).all()
   
    @property
    def pending_requests(self):
        query = session.query(Musician.name, Audition).join(Audition).filter(Audition.is_accepted == None, Audition.requested_by == 'musician')
        return query.all()

    @property
    def sent_requests_status(self):
        query  = session.query(Musician.name, Audition.is_accepted).join(Audition).filter(Audition.requested_by  == 'band')
        return query.all()

    @property
    def upcoming_auditions(self):
        query = session.query(Musician.name).join(Audition).filter(Audition.is_accepted == True)
        return query.all()

    @property
    def rejected_requests(self):
        query = session.query(Audition).filter(Audition.is_accepted == False)
        return query.all()
    
class Genre (Base):
    __tablename__ = 'genres'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    musicians = relationship('Musician', backref = 'genre')
    bands = relationship("Band", backref = 'genre')
    
    
    def __repr__(self):
        return f'< Genre: {self.name} >'
    
    @classmethod
    def get_all(cls):
        list_all = session.query(cls).all()
        return list_all

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
    
    def update_accepted(self, status):
        self.is_accepted = status
        session.commit()
