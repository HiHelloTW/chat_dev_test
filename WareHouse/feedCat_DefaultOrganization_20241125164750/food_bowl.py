'''
This file contains the FoodBowl class responsible for managing the cat's food bowl.
'''
class FoodBowl:
    def __init__(self):
        self.is_filled = False
    def fill(self):
        self.is_filled = True