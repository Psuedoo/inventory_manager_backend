import sqlalchemy as db
from sqlalchemy.orm import declarative_base, query, sessionmaker, Query
from models import Computer
from credentials import *


def connect():
    engine = db.create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER_IP}/{DATABASE_NAME}', echo=True)

    Session = sessionmaker(engine)
    session = Session()

    Base = declarative_base()

    return engine, session, Base


def add_computer(
        make,
        model,
        service_tag,
        asset_tag,
        issued,
        issuee,
        on_hand,
        on_location,
        location,
        class_location,
        checker,
        time_checked,
        notes
):
    engine, session, Base = connect()

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
        notes=notes,
    )
    session.add(computer)
    return session.commit()

def search_by_make(make):

    engine, session, Base = connect()

    query = session.query(Computer).filter(Computer.make==make)

    return [computer.__dict__ for computer in query.all()]


def search_by_checker(checker):

    engine, session, Base = connect()

    query = session.query(Computer).filter(Computer.checker==checker)

    return [computer.__dict__ for computer in query.all()]

def search(**search_props):
    valid_properties = [
        'make',
        'model',
        'service_tag',
        'asset_tag',
        'issued',
        'issuee',
        'on_hand',
        'on_location',
        'location',
        'class_location',
        'checker',
        'time_checked',
        'notes'
    ]
    filters = {}

    engine, session, Base = connect()

    query = session.query(Computer)

    # Validating inputs
    for key, value in search_props.items():
        if key in valid_properties:
            filters[key] = value
        else:
            print(f'{key} is not a valid searchable property')

    for attr, value in filters.items():
        query = query.filter(getattr(Computer, attr)==value)

    print(query.all())
