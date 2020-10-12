import unittest
from user import User

class TestUser(unittest.TestCase):
     
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User('kelvin', 'keya', '@Y0a!yAv')

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.first_name, "kelvin")
        self.assertEqual(self.new_user.last_name, "keya")
        self.assertEqual(self.password.password, "@Y0a!yAv")