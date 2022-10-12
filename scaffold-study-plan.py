# Create an appplication to keep track of a list of items
from datetime import datetime

class Item():
    def __init__(self):
        self.dateCreated = datetime.now()

    def description(self):
        print("This item was created on", self.dateCreated.date(), "at", self.dateCreated.ctime())

# Inherit from the item to a class of your choosing
#   For example: movies (don't choose this one), books, music, phones, etc

# Create at least three attributes of your specific item

# Create a method that outputs a description based on your attribute

# Store a list of your items, prompting the user for the data to create each item

# Output data about each of your items