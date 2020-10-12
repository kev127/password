import unittest
from user import User

class TestUser(unittest.TestCase):
     
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User('kelvin', 'keya', '@Y0a!yAv')