
from model.artist_model import Artists, Artwork

from view.view_utils import *

from exceptions.artwork_error import *

class View:
    def __init__(self,view_model):
        self.view_model = view_model
    # Do not need to pass any parameters to any of the methods in this class
    def add_Artist(self):
        
        try:
            self.view_model.add_Artist("Andrew" , "andrew@gmail.com")
        except Artwork_Error as e:
            print(str(e))

    def search_Artwork(self):
        artist_search = isName('artist')
        try:
            self.view_model.search_Artwork(artist_search)
        except Artwork_Error as e:
            print(str(e))
    def displayAvailable(self):
        artist_search = isName('artist')
        try:
            self.view_model.displayAvailable(artist_search)
        except Artwork_Error as e:
            print (str(e))
    def add_new_Artwork(self):
        artist = isName('artist')
        artwork_name = isName('artwork')
        price = input_positive_float(f'How much is {artwork_name} worth?')
        available = is_availbilty()

        try:
            self.view_model.add_new_artwork( artist, artwork_name, price , available)
        except Artwork_Error as e:
            print(str(e))
    def change_Availblity(self):
        artist = isName('artist')
        artwork_name = isName('artwork')
        availbilty = is_availbilty()

        try :
            self.view_model.change_availblity(artist, artwork_name, availbilty )
        except Artwork_Error as e:
            print (str(e))
        