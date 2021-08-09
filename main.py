import datetime

import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Computer
from credentials import *

# Create a credentials.py file and create the variables listed below
engine = db.create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER_IP}/{DATABASE_NAME}', echo=True)


Session = sessionmaker(engine)
session = Session()

Base = declarative_base()



test_computer = Computer(
    make='Dell',
    model='Latitude 5490',
    service_tag='1A2B3C',
    asset_tag=125322,
    issued=False,
    issuee=None,
    on_hand=True,
    on_location=False,
    location=None,
    class_location='Test',
    checker='Test Checker',
    time_checked=datetime.datetime.now(),
    notes=None
)

session.add(test_computer)
session.commit()
