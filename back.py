from sqlalchemy import create_engine, String, Integer, Column, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4())

Base = declarative_base()

class Pet(Base):
    __tablename__='pets'
    petId = Column('petId', String, primary_key=True, default=generate_uuid, onupdate=generate_uuid)
    petName = Column('petName', String)
    petBreed = Column('petBreed', String)
    petAge = Column('petAge', Integer)
    is_vaccinated = Column('is_vaccinated', Boolean, default=False)

    def __init__(self, petName, petBreed, petAge, is_vaccinated=False):
        self.petName = petName
        self.petBreed = petBreed
        self.petAge = petAge
        self.is_vaccinated = is_vaccinated

def add_pet(session, petName, petBreed, petAge):
    exists = session.query(Pet).filter_by(petName=petName).first()
    if exists:
        print('Name already exists')
    else:
        new_pet = Pet(petName, petBreed, petAge)
        session.add(new_pet)
        session.commit()

def increment_ages(session):
    all_pets = session.query(Pet).all()
    for pet in all_pets:
        pet.petAge += 1      
    session.commit()
    print('All ages incremented by 1')     

# Set up the database and session
db_url = 'sqlite:///petDB.db' 
engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()   

# Example: Add a new pet
petName = 'Wise'
petBreed = 't9'
petAge = 12
add_pet(session, petName, petBreed, petAge)

# Example: Increment ages
increment_ages(session)

# Example: Update existing pets to mark them as vaccinated
pets_to_update = session.query(Pet).filter_by(is_vaccinated=False).all()
for pet in pets_to_update:
    pet.is_vaccinated = True
session.commit()
