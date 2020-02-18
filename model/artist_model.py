"""
Forming an object to interact with the database. This represents the artist
table.
"""

class Artists():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__ (self):
        return f'{self.name}, {self.email}'
        

class Artwork ():
    def __init__(self, artist_name , artwork_name, price, availablity):
        self.artist_name = artist_name
        self.artwork_name = artwork_name
        self.price = price 
        self.availablity = availablity