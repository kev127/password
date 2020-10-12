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
