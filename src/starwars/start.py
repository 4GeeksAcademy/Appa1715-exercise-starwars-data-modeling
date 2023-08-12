import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(String(20), nullable=False)
    firstname = Column(String(20), unique=True, nullable=False)
    lastname = Column(String(20), unique=True, nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    favorites = Column(String(20), ForeignKey('favorites.id'), unique =True)


class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character = Column(Integer, ForeignKey('characters.id'), unique =True)
    planet = Column(Integer, ForeignKey('planet.id'), unique =True)
    starships = Column(Integer, ForeignKey('starships.id'), unique =True)
    user = relationship(User)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable =False)
    gravity = Column(String(20))
    color = Column(String(20))
    planet = Column(Integer, ForeignKey('characters.planets'), unique =True)
   

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    hairColor = Column(String(20))
    gender = Column(String(20))
    height = Column(Integer)
    planet = Column(String(20),unique= True)
    color = Column(String(20))
    name = Column(String(20), nullable =False)

 
    
class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    color = Column(String(20))
    pilot = Column(String(20), ForeignKey('characters.id'), unique =True)
    lenght = Column(Integer)
    character = relationship(Characters)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'starWars.png')
