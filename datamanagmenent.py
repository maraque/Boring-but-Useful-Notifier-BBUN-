#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')  # Access the DB Engine

Base = declarative_base()

def check_users():
    if not engine.dialect.has_table(engine, 'Users'):  # If table don't exist, Create.
        metadata = MetaData(engine)
        # Create a table with the appropriate Columns
        Table('Users', metadata,
              Column('Id', Integer, primary_key=True, nullable=False),
              Column('First_Name', String), Column('Last_Name', String),
              Column('Username', String), Column('Password', String),
              Column('Email', String))
        # Implement the creation
        metadata.create_all()


class User(Base):
    __tablename__ = 'Users'

    Id = Column(Integer, primary_key=True)
    First_Name = Column(String)
    Last_Name = Column(String)
    Username = Column(String)
    Password = Column(String)
    Email = Column(String)

check_users()

Session = sessionmaker(bind=engine)
ses = Session()

user1 = User(First_Name='Bob', Last_Name='Smith', Username = 'bmsith', Password='1234', Email='bsmith@email.com')
ses.add(user1)
ses.commit()

rs = ses.query(User).all()

for user in rs:
    print("User %s is %s %s with username %s" %(user.Id, user.First_Name, user.Last_Name, user.Username))
