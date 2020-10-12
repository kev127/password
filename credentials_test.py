import unittest
from credential import Credential

class TestCredentials(unittest.TestCase):

    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credential = Credentials('yahoo','kev127','@Y0a!yAv')

    def test_init(self):
        """
        test_init test case to test if the object is properly initialized
        """
        self.assertEqual(self.new_credential.account, "account")
        self.assertEqual(self.new_credential.user_name, "user_name")
        self.assertEqual(self.new_credential.password, "password")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credential.credential_list = []

    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)



