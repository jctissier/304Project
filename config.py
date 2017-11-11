import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
# DEBUG = True

# Connect to the database

# Mac
SQLALCHEMY_DATABASE_URI = 'sqlite://///' + os.path.join(basedir, 'projectDB.sqlite3')

# Windows
# SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\edwar\\Documents\\cpsc304\\304Project\\projectDB.sqlite3'

SQLALCHEMY_TRACK_MODIFICATIONS = False