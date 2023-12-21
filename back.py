from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4())

Base = declarative_base()

class Pet(Base):
    __tablename__='pets'
    petId = Column('petId',String,primary_key=True,default=generate_uuid)
    petName = Column('petName',String)
    petBreed = Column('petBreed',String)
    petAge = Column('petAge',Integer)

    def __init__(self,petName,petBreed,petAge):
        self.petName = petName
        self.petBreed = petBreed
        self.petAge = petAge

def add_pet(petName,petBreed,petAge):
            