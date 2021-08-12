import datetime
import random

import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Computer
from db_handler import *

# Create a credentials.py file and create the variables listed below
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
SERVER_IP = os.getenv('SERVER_IP')
DATABASE_NAME = os.getenv('DATABASE_NAME')

engine = db.create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER_IP}/{DATABASE_NAME}', echo=True)

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()


def generate_computer(service_tag):
    make = 'Dell',
    model = f'Latitude {random.randint(1000, 9000)}'
    service_tag = f'{service_tag}'
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

    computer = Computer(
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

    success = add_computer(computer)

    if success:
        print('Successfully added')


for i in range(15):
   generate_computer(i)


print(search(one='one', two='two', make='Dell', service_tag="10"))

computer = search(service_tag="10")

remove_computer(computer)

