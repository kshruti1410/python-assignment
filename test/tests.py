import unittest
from io import StringIO
from unittest.mock import patch
from src.q1 import sql_query
from src.q6 import gen_number
from src.Reverse_iter import ReverseIter
from src.q5 import binary_search
from src.q8 import SQUARED_NUMBER
from src.q2 import Male, Female
from src.q3 import sortlist
from src.q4 import Array3D
from src.q7 import extract_name
from src.q9 import dirtree
from src.q11 import read_html

class TestFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_Person(self):
        expected = "Person is Male\n"
        with patch("sys.stdout",new = StringIO()) as fake_out:
            actual = Male.get_gender(self)
            self.assertEqual(fake_out.getvalue(), expected)

        expected = "Person is Female\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            actual = Female.get_gender(self)
            self.assertEqual(fake_out.getvalue(), expected)
        with self.assertRaises(Exception) as exception_context:
            Person()
        self.assertTrue("err")

    def test_q8(self):
        expected = [i * i for i in range(1, 21)]
        actual = SQUARED_NUMBER()
        self.assertEqual(expected, actual)

    def test_reverse_iteration(self):
        expected = 9
        actual = ReverseIter([7, 8, 9]).next()
        self.assertEqual(expected, actual)

    def test_q5(self):
        expected = 4
        actual = binary_search([12, 24, 32, 39, 45, 50, 54], 45)
        self.assertEqual(expected, actual)

    def test_divisibility(self):
        expected=[0,35,70,105]
        actual= list(gen_number())
        self.assertEqual(expected,actual)

    def test_sortlist(self):
        expected = [12,24,35,88,120,155]
        actual=sortlist()
        self.assertEqual(expected,actual)

    def test_Array3D(self):
        expected =[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
        actual = Array3D()
        self.assertEqual(expected,actual)

    def test_extract_name(self):
        expected='datagrokr'
        actual = extract_name('shruti@datagrokr.com')
        self.assertEqual(expected,actual)

    @patch('src.q9.dirtree')
    def test_dir_tree(self,MockDirTree):
        directory = MockDirTree
        directory.dirtree.return_value = []
        actual = directory.dirtree("C:\Program Files\MySQL")
        expected=[]
        self.assertEqual(expected,actual)

    @patch('src.q1.sql_query')
    def test_generator_mysql(self, MockDatabase):
        database = MockDatabase()
        database.fetch.return_value = ''
        actual = database.fetch("SELECT * FROM northwind.sales_data")
        expected = ''
        self.assertEqual(expected, actual)

    def test_read_html(self):
        expected = ['The Godfather', 'Goodfellas', 'Pulp Fiction', 'The Usual Suspects', 'Apocalypse Now', 'Trainspotting', 'Fight Club', "Schindler's List", 'Boogie Nights', 'Reservoir Dogs', 'The Shawshank Redemption', 'Jaws', 'Taxi Driver', 'L.A. Confidential', 'Back to the Future', 'The Godfather: Part II', 'Fargo', 'The Dark Knight', 'The Matrix', 'Magnolia', 'Scarface', 'The Royal Tenenbaums', 'Donnie Darko', 'Platoon', 'Heat', 'American Beauty', 'The Big Lebowski', 'Raging Bull', 'Un prophète', 'The Departed', "There's Something About Mary", 'Léon', 'Cidade de Deus', 'Once Upon a Time in America', 'Lock, Stock and Two Smoking Barrels', 'The Truman Show', 'Toy Story', 'Alien', 'Rushmore', 'Se7en', 'Good Will Hunting', 'Aliens', 'The Exorcist', "One Flew Over the Cuckoo's Nest", 'Chinatown', 'Casino', 'True Romance', 'Sin City', 'Gladiator', 'Raiders of the Lost Ark', "Miller's Crossing", 'Being John Malkovich', 'Die Hard', 'Casablanca', 'Kick-Ass', 'The Prestige', 'Inglourious Basterds', 'Evil Dead II', 'Jurassic Park', 'Batman Begins', 'The Green Mile', 'The French Connection', 'Unforgiven', 'Drive', 'The Shining', 'The Evil Dead', 'Forrest Gump', 'The Thing', 'Citizen Kane', 'Blue Velvet', 'The Wicker Man', 'Eternal Sunshine of the Spotless Mind', 'The Princess Bride', 'A Clockwork Orange', 'Go', 'Stand by Me', 'The Lord of the Rings: The Return of the King', 'Terminator 2: Judgment Day', 'Toy Story 2', 'Saving Private Ryan', 'Desperado', 'Indiana Jones and the Last Crusade', 'Saw', 'My Left Foot: The Story of Christy Brown', 'Bowling for Columbine', 'Man on Fire', 'Almost Famous', 'High Fidelity', 'Django Unchained', '12 Angry Men', 'Memento', 'Rain Man', 'Minority Report', 'Goldfinger', 'The Social Network', 'American Psycho', 'Men in Black', 'No Country for Old Men', 'Airplane!', 'There Will Be Blood']
        actual=read_html()
        self.assertEqual(expected,actual)

    def tearDown(self):
        print("Testing completed")

if __name__ == '__main__':
    unittest.main()
