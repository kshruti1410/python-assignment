""" Reversing String"""

class ReverseIter:
    """ defining class"""
    def __init__(self, lis):
        self.lis = lis[::-1]
        self.i=0

    def __iter__ (self):
        return self

    def __next__ (self):
        if self.i < len(self.lis):
            i=self.i
            self.i +=1
            return self.lis[i]
        else:
            raise StopIteration()

    def next(self):
        return self.__next__()
