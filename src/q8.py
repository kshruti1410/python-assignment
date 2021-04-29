  
""" value is a empty list """
class squareMap:
    VALUE = []
    for number in range(1, 21):
        VALUE.append(number)
    SQUARED_NUMBER = map(lambda x: x**2, VALUE)
    print(list(SQUARED_NUMBER))