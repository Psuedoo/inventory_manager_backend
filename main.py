import datetime
import random

import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Computer
from credentials import *
from db_handler import *

# Create a credentials.py file and create the variables listed below
engine = db.create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER_IP}/{DATABASE_NAME}', echo=True)

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


def generate_computer():
    make = 'Dell',
    model = f'Latitude {random.randint(1000, 9000)}'
    service_tag = f'{random.randint(4000, 5000)}'
    asset_tag = random.randint(124000, 126000)
    issued = random.choice([True, False])
    if issued:
        issuee = 'Test Issuee'
        on_hand = False
    else:
        issuee = None
        on_hand = random.choice([True, False])

    if on_hand:
        on_location = False
        location = None
        class_location = None
    else:
        on_location = True
        location = f'Classroom {random.choice(["2400", "2401", "2300", "2301"])}'
        class_location = random.choice(['Lab', 'Podium'])

    checker = random.choice(['Tracy', 'Stefan', 'Josh', 'Austin'])
    time_checked = datetime.datetime.now()
    notes = None

    success =add_computer(
        make=make,
        model=model,
        service_tag=service_tag,
        asset_tag=asset_tag,
        issued=issued,
        issuee=issuee,
        on_hand=on_hand,
        on_location=on_location,
        location=location,
        class_location=class_location,
        checker=checker,
        time_checked=time_checked,
        notes=notes
    )

    if success:
        print('Successfully added')


for _ in range(10):
    generate_computer()
