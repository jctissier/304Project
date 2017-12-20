import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
# DEBUG = True

# Connect to the database
# Choose your environment, then uncomment which database you want to work with
# Mac
# SQLALCHEMY_DATABASE_URI = 'sqlite://///' + os.path.join(basedir, 'testData.sqlite3')
# SQLALCHEMY_DATABASE_URI = 'sqlite://///' + os.path.join(basedir, 'private/Data.sqlite3')

# WINDOWS
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'testData.sqlite3')
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'private/Data.sqlite3')

# TestDB

SQLALCHEMY_TRACK_MODIFICATIONS = False