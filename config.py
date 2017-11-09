import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
# DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite://///' + os.path.join(basedir, 'Zei.sqlite3')

SQLALCHEMY_TRACK_MODIFICATIONS = False