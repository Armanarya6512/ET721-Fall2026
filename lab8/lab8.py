"""
Name - Arman Arya 
September 30, 2026 - Wednesday
Lab8 :- unit testing 1
"""
import unittest
from calculation import addnumbers, subtractingnumbers, multiplyingnumbers, dividingnumbers


# create a unit-test for addnumbers
class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addnumbers(2,3), 5)
        #test if 2+3 is equal to 5
        self.assertEqual(addnumbers(), 0)
        self.assertEqual(addnumbers(5), 5)

    def test_subtraction(self):
        self.assertEqual(subtractingnumbers(5,6), -1)
        self.assertEqual(subtractingnumbers(3), 3)
        self.assertEqual(subtractingnumbers(7,3), 4)
        self.assertEqual(subtractingnumbers(), 0)

    def test_multiplication(self):
        self.assertEqual(multiplyingnumbers(3,2), 6)
        self.assertEqual(multiplyingnumbers(5), 5)
        self.assertEqual(multiplyingnumbers(), 1)

    def test_division(self):
        self.assertEqual(dividingnumbers(7,2), 3.5)
        self.assertEqual(dividingnumbers(7,3), 2.33, places=3)

    def test_dividebyzero(self):
        self.assertIsNone(dividingnumbers(10,0))

    def test_valueerror(self):
        self.assertIsNone(dividingnumbers(10,"a"))
        self.assertIsNone(dividingnumbers('a',10))

    def test_unexpected_xception(self):
        #test other possible error by mocking 
        with self.assertRaises(Exception):
           # passing none to trigger an exception
            dividingnumbers()

if __name__=="__main__":
    unittest.main()


