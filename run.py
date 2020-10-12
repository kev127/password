#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

def create_user(fname, user_name, password ):
    """
    Function to create a new user
    """
    new_user = User(fname, user_name, password )
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