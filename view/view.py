
from model.artist_model import Artists, Artwork

from view.view_utils import *

from exceptions.artwork_error import *

class View:
    def __init__(self,view_model):
        self.view_model = view_model
    # Do not need to pass any parameters to any of the methods in this class
    def add_Artist(self):

        artist = Artists("Andrew", "Ad@.com")
        try:
            self.view_model.add_Artist(artist)
        except Artwork_Error as e:
            print(str(e))

       