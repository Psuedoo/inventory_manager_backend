import os
import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Sequence, Boolean, DateTime
from sqlalchemy.types import MatchType
from credentials import *

Base = declarative_base()


class Computer(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, Sequence('computer_id_seq'), primary_key=True)
    make = Column(String)
    model = Column(String)
    service_tag = Column(String)
    asset_tag = Column(Integer)
    issued = Column(Boolean)
    issuee = Column(String)
    on_hand = Column(Boolean)
    on_location = Column(Boolean)
    location = Column(String)
    class_location = Column(String)
    checker = Column(String)
    time_checked = Column(DateTime)
    notes = Column(String)


if __name__ == '__main__':

    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    SERVER_IP = os.getenv('SERVER_IP')
    DATABASE_NAME = os.getenv('DATABASE_NAME')

    engine = db.create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER_IP}/{DATABASE_NAME}', echo=True)

    Session = sessionmaker(engine)
    session = Session()

    Base.metadata.create_all(engine, checkfirst=True)
    print('added')
