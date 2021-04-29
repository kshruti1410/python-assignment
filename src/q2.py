""" abc is a by default abrstract class present """

from abc import ABC, abstractmethod

class Person(ABC):

    """ inherit ABC class """

    @abstractmethod
    def get_gender(self):
        """ skipping the function """
        pass


class Female(Person):

    """ this class return gender of a person """

    def get_gender(self):
        """ self is by default argument """

        print("Person is Female")


class Male(Person):

    """ this class return gender of a person """

    def get_gender(self):
        """ self is by default argument """

        print("Person is Male")


try:
    PARENT = Person()
except TypeError:
    print(TypeError)
finally:

    print("Female class method")
    FEMALE = Female()
    FEMALE.get_gender()

    print("Male class method")
    MALE = Male()
    MALE.get_gender()