#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

def create_user(fname, username, password ):
    """
    Function to create a new user
    """
    new_user = User(fname, username, password )
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user_details()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def create_credential(account,userName,password):
    """
    Function to create new user credentials
    """
    new_credential = Credential(account,username,password)
    return new_credential

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()

def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def main():

    print("welcome to password locker 2020")
    print('\n')
    print("Select a short code to guide you:To create a new user type'New':To login to an account'Login':To display user type:'Display' or 'Quit' to exit")
    short_code = input().lower()
    print('\n')

    if short_code == 'New':
        print('New User')
        created_user == input()
        print("create password")
        created_user_password == input()
        print("Welcome what account would you like to add?")
        account == input()

        else:
            print("Login")
            print("user")
            entered_user = input()
            print("enter password")
            entered_password = input()
        else:
            print(f"welcome to your account")
            print('\n')
    elif short_code == 'Login':
        print("welcome")
        print("Enter user")
        default_user = input()
        print("enter password")
        default_user_password = input()
        print('\n')

        else:
            print("Login success")
            print('\n')
    elif short_code == 'Display':
        print("Here is your user accounts")
        print('\n')
        for user in display_user():
            print(f"{user_name} {account} has an account for {account}")
            print('\n')

            else:
                print('\n')
                print("You don't seem to have any existing accounts")
                print('\n')







