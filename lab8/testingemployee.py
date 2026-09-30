import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    # test template, instant of the class
    def setUp(self):
        self.emp_1 = Employee("Arman", "Arya", 50000)
        self.emp_2 = Employee("John", "Doe", 60000)

    # test if email format is working properly
    def test_emailemployee(self):
        self.assertEqual(self.emp_1.emailemployee, "aarya@email.com")
        self.assertEqual(self.emp_2.emailemployee, "jdoe@email.com")

    # test full name 
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Arman Arya")
        self.assertEqual(self.emp_2.fullname, "John Doe")

    # test raise 
    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.salary, 52500)
        self.assertEqual(self.emp_2.salary, 63000)

if __name__ == "__main__":
    unittest.main()