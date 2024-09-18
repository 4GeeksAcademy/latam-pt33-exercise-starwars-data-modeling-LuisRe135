import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'nv
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable = False)
    password = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    subscription_date = Column(Date, index=True, nullable = False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'))
    planet = Column(String(250), ForeignKey('planets.id'), nullable = True)
    character = Column(String(250), ForeignKey('people.id'), nullable = True)
    vehicle = Column(String(250), ForeignKey('vehicles.id'), nullable = True)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    population = Column(Integer, nullable = False)
    climate = Column(String(250), nullable = False)
    diameter = Column(Integer, nullable = False)
    gravity = Column(Integer, nullable = False)
    orbital_period = Column(Integer, nullable = False)
    rotation_period = Column(Integer, nullable = False)
    surface_water = Column(Integer, nullable = False)
    terrain = Column(String(250), nullable = False)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    birth_year = Column(String(250), nullable = False)
    eye_color = Column(String(250), nullable = False)
    gender = Column(String(250), nullable = True)
    hair_color = Column(String(250), nullable = True)
    homeworld = Column(String(250), nullable = False)
    mass = Column(Integer, nullable = False)
    skin_color = Column(String(250), nullable = False)
    vehicles = Column(String(250), nullable = False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name= Column(String(250), nullable = False)
    model = Column(String(250), nullable = False)
    cost_in_credits = Column(Integer, nullable = False)
    passengers = Column(Integer, nullable = False)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
