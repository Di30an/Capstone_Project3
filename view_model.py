# Takes the db object and calls the methods from that class
# Helps to deal with view and repository

class ViewModel :
    def __init__(self , db):
        self.db = db
    
    def add_Artist(self, Artists):
        self.db.insert()

    def search_Artwork(self, artist_search):
        self.db.search_Artwork(artist_search)
    
    def displayAvailable(self, artist_search):
        self.db.displayAvailable(artist_search)

    def add_new_artwork(self , Artwork):
        self.db.add_new_artwork(Artwork)

    def change_availblity(self):
        self.db.change_availblity()