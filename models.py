# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)

class Student(Person):
    __tablename__ = 'students'
    id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    grade = Column(String)

    person = relationship("Person", backref="student")

class Employee(Person):
    __tablename__ = 'employees'
    id = Column(Integer, ForeignKey('people.id'), primary_key=True)
    department = Column(String)

    person = relationship("Person", backref="employee")
