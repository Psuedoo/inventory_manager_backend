import sqlalchemy as db
from sqlalchemy.orm import declarative_base, sessionmaker
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
