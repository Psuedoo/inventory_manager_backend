from sqlalchemy.orm.session import sessionmaker
from constant import *
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Boolean, DateTime

Base = declarative_base()

def initialize_db():
    engine = create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER_IP}/{DATABASE_NAME}', echo=True)
    
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    Base.metadata.bind = engine
    Base.metadata.create_all(checkfirst=True)

    return session

class Computer(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, Sequence('computer_id_seq'), primary_key=True)
    make = Column(String)
    model = Column(String)
    service_tag = Column(String)
    asset_tag = Column(Integer)
    issued = Column(Boolean)
    assigned_to = Column(String)
    on_hand = Column(Boolean)
    on_location = Column(Boolean)
    computer_location = Column(String)
    class_location = Column(String)
    checker = Column(String)
    time_checked = Column(DateTime)
    notes = Column(String)

