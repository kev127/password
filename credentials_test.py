import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credentials = Credentials("yahoo", "kev127", "@Y0a!yAv")

    def test_init(self):
        """
        test_init test case to test if the object is properly initialized
        """
        self.assertEqual(self.new_credentials.account,"yahoo")
        self.assertEqual(self.new_credentials.userName,"kev127")
        self.assertEqual(self.new_credentials.password,"@Y0a!yAv")
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

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
        self.new_credentials.save_details()
        test_credential = Credentials("gmail","joan33","00oe!rt") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credentials.save_details()
        test_credential = Credentials("gmail","joan33","00oe!rt")
        test_credential.save_details()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_display_credentials(self):
        """
        method that returns a list of saved credentials
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()



