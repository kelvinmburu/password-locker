import random
import string
import pyperclip

# Creating class to generate new instance of an user


class User:

    user_list = []

    # Function to highlight properties of a user_list

    def save_user(self):

        User.self_list.append(self)

        # Method to display user list

    @classmethod
    def display_user_list(cls):
        return cls.user_list

    # Create function to delete user user_list

    def delete_user(self):

        User.self_list.remove(self)

# New class to create a new instance of credentials


class Credentials():
    credentials_list = []

    # Add function to verify user credentials
    @classmethod
    def verify_user(cls, username, password):

        a_user = ""

        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user = user.username
                return a_user

    # Add new function that defines user credential attributes

    def __init__(self, account, userName, password):

        self.account = account
        self.userName = userName
        self.password = password

    # Function to store credentials to user list

    def save_details(self):

        Credentials.credentials_list.append(self)

    # Add function for deleting user credentials
