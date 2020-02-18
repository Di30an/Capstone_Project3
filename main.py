
#from view import *

from sql_databse.database import SQLArtworkDB
from model.artist_model import *
from view_model import ViewModel
from view.view import View

def main():
    # Creates database object. 
    artwork_db = SQLArtworkDB()
    # Creates an ViewModel object with SQLArtworkDB as its attribute. 
    # Keeps the view seperate from the database. 
    artist_view_model = ViewModel(artwork_db)
    # Creates an object with ViewModel as its attribute
    # This class creates objects to be inserted into the database
    # and also creates views for the user. 
    artist_view = View(artist_view_model)
    #Menu loop
    menu = True
    while menu:
        # Prints out a display for the user to see. 
        print('\n Database Menu : \n '
        '1 : Add new Artist \n'
        '2 : Search Artwork by Artist \n'
        '3 : Display Available Artwork By Artist \n'
        '4 : Add New Artwork by Artist \n'
        '5 : Change Availbilty by Artwork \n'
        '6 : Type Quit to Exit the program \n')

        menuChoice = input("Please enter a number. ")
        # Went for a simple Menu layout. If I can get this to run I would like to try and use a GUI. 

        if menuChoice == '1':
           artist_view.add_Artist()
        if menuChoice == '2':
            artist_view.search_Artwork()
        if menuChoice == '3':
            artist_view.displayAvailable()
        if menuChoice == '4':
            artist_view.add_new_Artwork()
        if menuChoice == '5':
            artist_view.change_Availblity()
        if menuChoice == '6' :
            menu = False
        else :
            print("Please enter a valid option")
   

main()


