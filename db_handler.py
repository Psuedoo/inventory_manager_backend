import os
import sqlalchemy as db
from sqlalchemy import engine
from sqlalchemy.orm import declarative_base, query, sessionmaker, Query
from models import Computer


def connect():
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    SERVER_IP = os.getenv('SERVER_IP')
    DATABASE_NAME = os.getenv('DATABASE_NAME')

    engine = db.create_engine(f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER_IP}/{DATABASE_NAME}', echo=True)
    Session = sessionmaker(engine)
    session = Session()

    Base = declarative_base()

    return engine, session, Base


def add_computer(computer):
    engine, session, Base = connect()

    session.add(computer)
    return session.commit()

def remove_computer(computer):
    engine, session, Base = connect()

    session.delete(computer)
    session.commit()

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

    if len(query.all()) == 1:
        return query.first()
    elif len(query.all()) > 1:
        return query.all()
    else:
        return None
