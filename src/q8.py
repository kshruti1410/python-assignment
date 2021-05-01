  
""" value is a empty list """
def SQUARED_NUMBER():
    VALUE = []
    for number in range(1, 21):
        VALUE.append(number)
    SQUARED_NUMBER = map(lambda x: x**2, VALUE)
    return (list(SQUARED_NUMBER))