from flask import Flask
import unittest
from app.db.database import db, ZeiDB
import csv
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Column, Table, MetaData, create_engine
from dateutil.parser import parse


""" Unit Tests: Database """


class TestDatabase(unittest.TestCase):
    basedir = os.path.abspath(os.path.dirname(__file__))        # Grabs the folder where the script runs.

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///' + os.path.join(self.basedir, 'testZei.sqlite3')
        self.db = db

        self.db.init_app(self.app)
        with self.app.app_context():
            self.db.create_all()

            # Functions to test the database
            self.test_print()                   # Adds data into database
            # self.test_print()                   # Check content of database
            # self.test_print()                   # Run a query on content of database

        print("test_database_setUp: OK")

    def tearDown(self):
        """
        Ensures that the database is deleted for next unit test
        """
        self.assertTrue(os.path.exists(os.path.join(self.basedir, 'testZei.sqlite3')))          # Database exists

        with self.app.app_context():
            self.db.drop_all()
            # os.remove(os.path.join(self.basedir, 'testZei.sqlite3'))                            # Deletes the database
            print("test_database_tearDown: OK")

        # self.assertFalse(os.path.exists(os.path.join(self.basedir, 'testZei.sqlite3')))         # Database is deleted


if __name__ == "__main__":
    unittest.main()





"""
from app import app
import unittest

class FlaskBookshelfTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the response data
        self.assertEqual(result.data, "Hello World!!!")
"""

