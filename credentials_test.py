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

    def test_save_multiple_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("gmail","joan33","00oe!rt") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

     def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("gmail","joan33","00oe!rt")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_display_credentials(self):
        """
        method that returns a list of saved credentials
        """
        self.assertEqual(Credential.display_credential(), Credential.credential_list)

if __name__ == '__main__':
    unittest.main()



