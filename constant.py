import os

USERNAME = os.getenv('USERNAME', 'admin')
PASSWORD = os.getenv('PASSWORD', 'dbpass')
SERVER_IP = os.getenv('SERVER_IP','db')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'admin')