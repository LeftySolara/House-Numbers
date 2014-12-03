# Simple die class
# Simulates rolling of one die with any number of sides

from random import randint

class Die(object):
    """Represents one die object"""

    def __init__(self,sides=6):
        self.__sides = sides

    def __str__(self):
        return "A {} sided die".format(str(self.__sides))
        
    def roll(self):
        self.__last_roll = randint(1,self.__sides)
        return self.__last_roll