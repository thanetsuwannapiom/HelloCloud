import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

engine = create_engine('sqlite:///user.sqlite3', echo = False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1   = User(name='user1', fullname='Ed jones', nickname = 'ed')
user2   = User(name='user2', fullname='TEd jones', nickname = 'Ted')
session.add(user1)
session.add(user2)
session.commit()
