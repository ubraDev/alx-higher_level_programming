#!/usr/bin/python3
class Base:
    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        # If id is provided, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        else:
            # Increment the private attribute __nb_objects and assign it to id
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
