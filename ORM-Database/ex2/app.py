from models import Base, Member
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

# Create engine
db_uri = 'sqlite:///Ex2.sqlite3'
engine = create_engine(db_uri, echo=False)

#Creat All Tables
#Base.metadata.drop_all(engine)\
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user = Member(
    name='Mac',
    description='im testing this',
    vip=True,
    join_date=datetime.date.today(),
    number=45.0
)
session.add(user)
session.commit()
print(user)
