import sqlalchemy as db
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

    def add_computer(self, computer):
        self.session.add(computer)
        return self.session.commit()

    def remove_computer(self, computer):
        self.session.delete(computer)
        self.session.commit()

    def search(self, **search_props):
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

        query = self.session.query(Computer)

        # Validating inputs
        for key, value in search_props.items():
            if key in valid_properties:
                filters[key] = value
            else:
                print(f'{key} is not a valid searchable property')

        for attr, value in filters.items():
            print(attr, value)
            query = query.filter(getattr(Computer, attr)==value)

        return query.all()
