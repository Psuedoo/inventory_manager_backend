from datetime import datetime

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
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    service_tag = Column(String, nullable=False)
    asset_tag = Column(String, nullable=False)
    issued = Column(Boolean, nullable=False)
    assigned_to = Column(String, default='Unassigned', nullable=False)
    on_hand = Column(Boolean, nullable=False)
    on_location = Column(Boolean, nullable=False)
    computer_location = Column(String, nullable=False)
    class_location = Column(String, default='N/A', nullable=False)
    checker = Column(String, nullable=False)
    time_checked = Column(DateTime, default=datetime.now(), nullable=False)
    notes = Column(String, default='', nullable=False)

