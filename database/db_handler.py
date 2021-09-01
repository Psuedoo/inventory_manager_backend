import sqlalchemy as db
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker 
from .models import Computer, Role, User, initialize_db
from constant import *

class DatabaseHandler:
    def __init__(self):
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.SERVER_IP = SERVER_IP
        self.DATABASE_NAME = DATABASE_NAME
        self.session = initialize_db()

    def validate_inputs(self, props):
        """Validate inputs for searching."""
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
            'notes',
            'username',
            'password',
            'name'
        ]
        valididated_props = {}

        # Validating inputs
        for key, value in props.items():

            if key in valid_properties and value:
                valididated_props[key] = value
            else:
                print(f'{key} is not a valid property')

        return valididated_props

    def search(self, search_type, search_props: dict):
        """Dynamically searches the database."""

        filters = self.validate_inputs(search_props)

        if search_type == 'Computer':
            search_table = Computer
        if search_type == 'User':
            search_table = User
        if search_type == 'Role':
            search_table = Role

        
        query = self.session.query(search_table)

        for attr, value in filters.items():
            query = query.filter(getattr(search_table, attr)==value)

        return query.all()

    def add_computer(self, computer):
        """Adds a computer to database."""
        if not computer.time_checked:
            computer.time_checked = datetime.now()

        self.session.add(computer)
        return self.session.commit()

    def remove_computer(self, computer_id):
        """Removes a computer from the database."""
        computer = self.search('Computer', {'id': computer_id})[0]
        self.session.delete(computer)
        self.session.commit()

    def update_computer(self, computer_id, computer):
        """"Updates a computer in the database."""
        db_computer = self.search('Computer', {'id': computer_id})[0]

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

    def add_user(self, user):
        """Adds a user to the database."""
        self.session.add(user)
        self.session.commit()

    def remove_user(self, user_id):
        """Removes a user from the database."""
        user = self.search('User', {'id': user_id})[0]
        self.session.delete(user)
        self.session.commit()

    def update_user(self, user_id, user):
        """Updates a user in the database."""
        db_user = self.search('User', {'id': user_id})[0]

        db_user.name = user.name
        db_user.username = user.username
        db_user.password = user.password
        db_email = user.email
        db_role = user.role


    def add_role(self, role):
        """Adds a role to the database."""
        self.session.add(role)
        return self.session.commit()

    def remove_role(self, role_id):
        """Removes a role from the database."""
        role = self.search('Role', {'id': role_id})[0]
        self.session.delete(role)
        self.session.commit()

    def update_role(self, role_id, role):
        """Updates a role in the database."""
        db_role = self.search('Role', {'id': role_id})[0]

        db_role.name = role.name

        self.sesion.commit()
