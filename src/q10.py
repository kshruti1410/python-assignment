""" Rversing String"""

class Reverselter:
    """ defining class"""
    def __init__(self, value):
        """ Taking list in value argument"""
        for number in range(len(value)-1, -1, -1):
            print(value[number])
VALUE = [11, 12, 13, 14, 15]
Reverselter(VALUE)