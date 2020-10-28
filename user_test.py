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
        self.assertEqual(self.new_user.user_name,"kev127")
        self.assertEqual(self.password.password, "@Y0a!yAv")
        self.assertEqual(self.new_user.confirm_password,"@Y0a!yAv")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.user_list = []

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user_details()
        self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
    unittest.main()
