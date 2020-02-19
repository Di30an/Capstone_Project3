import sqlite3
from database_abc import ArtistDB
from model.artist_model import Artists , Artwork
from .config import db_path
from utils.validation import ensure_positive_float
from exceptions import artwork_error
db = db_path

class SQLArtworkDB(ArtistDB):
    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS artists (artist TEXT NOT NULL, email TEXT)')
            conn.execute('CREATE TABLE IF NOT EXISTS artworks ( "artist" TEXT, "artwork_name" TEXT, "price"	INTEGER,	"available"	TEXT)')

    def add_Artist(self, name, email):

        insert_sql = "INSERT INTO artists (artist , email) VALUES (?,?)"
        
        with sqlite3.connect(db) as conn :
            c = conn.cursor()
            c.execute(' SELECT * FROM artists WHERE artist =(?)',(name,))
            all_rows = c.fetchall()

            rows_mod = conn.execute(insert_sql ,(name, email) ) 
            print(f" {name} Added to the database.")
        conn.close()
        return rows_mod

    def search_Artwork(self, artist_search):

        read_sql = "SELECT artist , artwork_name FROM artworks WHERE artist = (?)"

        with sqlite3.connect(db) as conn :
            c = conn.cursor()
            c.execute (read_sql ,(artist_search,) )
            all_rows = c.fetchall()

            # Checking if there are any Artwork and returning the proper values.
            if len (all_rows) == 0 :
                print(f'{artist_search} has no Artwork here.')
            else:
                for row in all_rows:
                    print (row[0] + " " + row[1])
        
    def displayAvailable(self, artist_search):
        read_sql = "SELECT artist , artwork_name FROM artworks WHERE artist = (?) AND available = 'AVAILABLE' "

        with sqlite3.connect(db) as conn :
            c = conn.cursor()
            c.execute (read_sql ,(artist_search,) )
            all_rows = c.fetchall()

            # Checking if there are any Artwork and returning the proper values.
            if len (all_rows) == 0 :
                print(f'{artist_search} has no Artwork here.')
            else:
                for row in all_rows:
                    print (row[0] + " " + row[1])



    def add_new_artwork(self , artist, artwork_name, price , available):
        insert_sql = "INSERT INTO artworks (artist , artwork_name , price , available) VALUES (?,?,?,?)"
        ## Check if artist is in artist database and then check if 
        ## artwork is in database. "Artist not found. Add the artist first"
        with sqlite3.connect(db) as conn : 
            c = conn.cursor()
            c.execute(' SELECT artist FROM artists WHERE artist =(?)',(artist,))
            all_rows = c.fetchall()
            if len(all_rows) == 0:
                print(f" {artist} Not found added. Please add them first. ")
            else :
                conn.execute(insert_sql ,(artist, artwork_name, price , available)) 
                print(f" {artwork_name} Added to the database.") 

        
    def change_availblity(self, artist_search, artwork_search, available):
        read_sql = "SELECT artist , artwork_name FROM artworks WHERE artist = (?) AND artwork_name = (?) "
    
        with sqlite3.connect(db) as conn :
            c = conn.cursor()
            c.execute (read_sql ,(artist_search, artwork_search) )
            all_rows = c.fetchall()

            # Checking if there are any Artwork and returning the proper values.
            if len (all_rows) == 0 :
                print(f'{artist_search} has no Artwork here.')
            else:
                c.execute('Update artworks Set available = (?) WHERE artist  = (?) ', (available, artist_search, ))
                print(f'{artist_search} is currently {available}')


