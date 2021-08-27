import sqlalchemy as db
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker 
from .models import Computer, initialize_db
from constant import *

class DatabaseHandler:
    def __init__(self):
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.SERVER_IP = SERVER_IP
        self.DATABASE_NAME = DATABASE_NAME
        self.session = initialize_db()

    def validate_inputs(self, props):
        valid_properties = [
            'id',
            'make',
            'model',
            'service_tag',
            'asset_tag',
            'issued',
            'assigned_to',
            'on_hand',
            'on_location',
            'computer_location',
            'class_location',
            'checker',
            'time_checked',
            'notes'
        ]
        valididated_props = {}

        # Validating inputs
        for key, value in props.items():

            if key in valid_properties and value:
                valididated_props[key] = value
            else:
                print(f'{key} is not a valid property')

        return valididated_props


    def add_computer(self, computer):
        if not computer.time_checked:
            computer.time_checked = datetime.now()

        valid_computer = Computer(
                make=computer.make,
                model=computer.model,
                service_tag=computer.service_tag,
                asset_tag=computer.asset_tag,
                issued=computer.issued,
                assigned_to=computer.assigned_to,
                on_hand=computer.on_hand,
                on_location=computer.on_location,
                computer_location=computer.computer_location,
                class_location=computer.class_location,
                checker=computer.checker,
                time_checked=computer.time_checked,
                notes=computer.notes
            )
        
        self.session.add(valid_computer)
        return self.session.commit()

    def remove_computer(self, computer):
        self.session.delete(computer)
        self.session.commit()

    def update_computer(self, computer_id, computer):
        db_computer = self.search({'id': computer_id})[0]

        db_computer.make = computer.make
        db_computer.model = computer.model
        db_computer.service_tag = computer.service_tag
        db_computer.asset_tag = computer.asset_tag
        db_computer.issued = computer.issued
        db_computer.assigned_to = computer.assigned_to
        db_computer.on_hand = computer.on_hand
        db_computer.on_location = computer.on_location
        db_computer.computer_location = computer.computer_location
        db_computer.class_location = computer.class_location
        db_computer.checker = computer.checker
        db_computer.time_checked = datetime.now()
        db_computer.notes = computer.notes

        self.session.commit()


    def search(self, search_props: dict):

        filters = self.validate_inputs(search_props)

        query = self.session.query(Computer)

        for attr, value in filters.items():
            print(attr, value)
            query = query.filter(getattr(Computer, attr)==value)

        return query.all()
