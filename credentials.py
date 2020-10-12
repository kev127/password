class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []

    def __init__(self, user_name, account, password,):
        self.user_name = user_name
        self.account = account
        self.password = password

    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.credentials_list

    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
