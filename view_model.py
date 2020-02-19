# Takes the db object and calls the methods from that class
# Helps to deal with view and repository

class ViewModel :
    def __init__(self , db):
        self.db = db
    
    def add_Artist(self, artists, email):
        self.db.add_Artist(artists, email)

    def search_Artwork(self, artist_search):
        self.db.search_Artwork(artist_search)
    
    def displayAvailable(self, artist_search):
        self.db.displayAvailable(artist_search)

    def add_new_artwork(self , artist, artwork_name, price , available):
        self.db.add_new_artwork( artist, artwork_name, price , available)

    def change_availblity(self,artist, artwork_name, availbilty ):
        self.db.change_availblity(artist, artwork_name, availbilty )