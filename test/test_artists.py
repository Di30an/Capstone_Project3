import sqlite3
import unittest
from unittest import TestCase





from exceptions.artwork_error import Artwork_Error

from sql_databse.database import SQLArtworkDB

class TestArtistDB(TestCase):
    test_db_url = 'test_artworks.db'

    """
    Before running these tests create test_miles.db
    Create artists and artwork data
    ('CREATE TABLE IF NOT EXISTS artists (artist TEXT NOT NULL, email TEXT)')
    ('CREATE TABLE IF NOT EXISTS artworks ( "artist" TEXT, "artwork_name" TEXT, "price"	INTEGER,	"available"	TEXT)')
    """
    def setUp(self):
        database.db = self.test_db_url
        # drop everything from the DB to always start with an empty database
        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('DROP TABLE IF EXISTS artists')
            conn.execute('DROP TABLE IF EXISTS artworks ')
        conn.close()

        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS artists (artist TEXT NOT NULL, email TEXT)')
            conn.execute('CREATE TABLE IF NOT EXISTS artworks ( "artist" TEXT, "artwork_name" TEXT, "price"	INTEGER,"available"	TEXT)')
        conn.close()

        self.db = SQLArtworkDB()

    def test_add_Artist(self):
        # artist, email
        a1 = ('Andrew', 'Andrew@Gmail.com')
        self.db.add_Artist(a1)
        expected = {'Andrew':'Andrew@Gmail.com'}
        self.compare_db_to_expected (expected)

        a2 = ('Ben', 'Ben@Gmail.com')
        self.db.add_Artist(a1)
        expected = {'Andrew':'Andrew@Gmail.com','Ben' :'Ben@Gmail.com'}
        self.compare_db_to_expected (expected)

        a2 = ('Stan', 'Stan@Gmail.com')
        self.db.add_Artist(a1)
        expected = {'Andrew':'Andrew@Gmail.com','Ben' :'Ben@Gmail.com','Stan' :'Stan@Gmail.com'}
        self.compare_db_to_expected (expected)

    def test_search_Artwork(self):
        # artist_search
        pass

    def test_displayAvailable(self):
        # artist_search
        pass

    def test_add_new_artwork(self):
        #artist
        pass

    def test_change_availblity(self):

        pass
    
