import sqlite3
from database_abc import ArtistDB
from model.artist_model import Artists , Artwork
from .config import db_path
from utils.validation import ensure_positive_float

db = db_path

class SQLArtworkDB(ArtistDB):
    def __init__(self):
        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS artists ("artist"	TEXT NOT NULL,"artwork"	TEXT')
            conn.execute('CREATE TABLE "artwork" ( "artist" TEXT, "artwork_name" TEXT, "price"	INTEGER,	"available"	TEXT)')

    def add_Artist(self, Artists):

        insert_sql = "INSERT INTO artists (artist , email_address) VALUES (?,?)"
        with sqlite3.connect(db) as conn :
            c = conn.cursor()
            c.execute(' SELECT * FROM artists WHERE artist =(?)',(Artists.name))
            all_rows = c.fetchall()
            if len(all_rows) == 0:
                conn.execute(insert_sql ,(Artists.name, Artists.email) ) 
                print(f" {Artists.name} Added to the database.")
            else :
                print ("Already in the database. ")
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
        read_sql = "SELECT artist , artwork_name FROM artworks WHERE artist = (?) AND available = 'Available' "

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



    def add_new_artwork(self , Artwork):
        insert_sql = "INSERT INTO artworks (artist , artwork_name , price , available) VALUES (?,?,?,?)"
        ## Check if artist is in artist database and then check if 
        ## artwork is in database. "Artist not found. Add the artist first"
        with sqlite3.connect(db) as conn : 
            c = conn.cursor()
            c.execute(' SELECT artwork_name FROM artworks WHERE artist =(?)',(Artwork.artist_,))
            all_rows = c.fetchall()
            if len(all_rows) == 0:
                print(f" {Artwork.artist_name} Not found added. Please add them first. ")
            else :
                conn.execute(insert_sql ,(Artwork.artist_name, Artwork.artwork_name,Artwork.price, Artwork.availablity) ) 
                print(f" {Artwork.artwork_name} Added to the database.") 

        
    def change_availblity(self):
        pass


