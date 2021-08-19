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
        if type(computer) == dict:
            valid_inputs = self.validate_inputs(computer)

            valid_computer = Computer(
                make=valid_inputs.get('make', None),
                model=valid_inputs.get('model', None),
                service_tag=valid_inputs.get('service_tag', None),
                asset_tag=valid_inputs.get('asset_tag', None),
                issued=valid_inputs.get('issued', False),
                assigned_to=valid_inputs.get('assigned_to', None),
                on_hand=valid_inputs.get('on_hand', False),
                on_location=valid_inputs.get('on_location', False),
                computer_location=valid_inputs.get('computer_location', None),
                class_location=valid_inputs.get('class_location', None),
                checker=valid_inputs.get('checker', None),
                time_checked=valid_inputs.get('time_checked', datetime.now()),
                notes=valid_inputs.get('notes', '')
            )

        else:
            valid_computer = computer

        self.session.add(valid_computer)
        return self.session.commit()

    def remove_computer(self, computer):
        self.session.delete(computer)
        self.session.commit()

    def search(self, search_props: dict):

        filters = self.validate_inputs(search_props)

        query = self.session.query(Computer)

        for attr, value in filters.items():
            print(attr, value)
            query = query.filter(getattr(Computer, attr)==value)

        return query.all()
