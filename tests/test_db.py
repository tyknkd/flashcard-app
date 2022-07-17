#!/usr/bin/python3

# https://docs.python.org/3/library/unittest.html
import unittest
import sqlite3
import os
import dbScripts

def get_cursor(dbname):
    '''
    Get cursor to specified database
    :dbname: Database file
    :return: Cursor to database
    '''
    # Connection to database
    connection = sqlite3.connect(dbname)
                                  
    # Return cursor to interact with database
    return connection.cursor()

# Name of database to test 
dbName = 'test.db'

class StoreDBTestCase(unittest.TestCase):
            
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # Create test database
        dbScripts.createDB(dbName)
        dbScripts.initialPopulate(dbName)

    def tearDown(self):
        # Remove test database
        if os.path.exists(dbName):
            os.remove(dbName)

                                                                                                            def test_init(self):
        '''
        Test initialization of database
        '''
        self.assertTrue(os.path.exists(dbName))
