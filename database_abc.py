""" 
Creating an abstract class to interface with the SQL databse. 
This should all for an easy swap to peewee. 
"""

import abc
# Artist is an object with Artist and Email as artributes
# Artwork is an object with artist, artwork_name, 
class ArtistDB(abc.ABC):
    @abc.abstractmethod
    def add_Artist(self, artist, email):
        pass
    @abc.abstractmethod
    def search_Artwork(self, artist_search):
        pass
    @abc.abstractmethod
    def displayAvailable(self, artist_search):
        pass
    @abc.abstractmethod
    def add_new_artwork(self , artist):
        pass
    @abc.abstractmethod
    def change_availblity(self):
        pass