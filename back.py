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

    def __init__(self, petName, petBreed,petAge):
        self.petName = petName
        self.petBreed = petBreed
        self.petAge = petAge
     

def add_pet(session, petName, petBreed, petAge):
    exists = session.query(Pet).filter_by(petName=petName).first()
    if exists:
        print('Name already exists')
    else:
        new_pet = Pet(petName, petBreed, petAge)
        session.add(new_pet)
        session.commit()

def delete_pet(session,petName):
    pet_to_delete = session.query(Pet).filter_by(petName=petName).first()
    if pet_to_delete:
        session.delete(pet_to_delete)
        session.commit()
        print(f'{petName} deleted') 
    else:
        print(f'{petName} not found') 
        session.commit()
    


# Set up the database and session
db_url = 'sqlite:///petDB.db' 
engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()   

petName = 'Ki'
petBreed = 'German Shepherd'
petAge = 12
# add_pet(session, petName, petBreed, petAge)
delete_pet(session,'fhy')
