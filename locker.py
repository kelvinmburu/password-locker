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

    def delete_credentials(self):

        Credentials.credentials_list.remove(self)

    # Function to search for user credentials using app name

    @classmethod
    def find_credential(cls, account):

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    # Function to copy password to clipboard using pyperclip

    @classmethod
    def copy_password(cls, account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    # Function to evaluate if user credentials exist in the app

    @classmethod
    def if_credential_exist(cls, account):

        for credential in cls.credentials_list:
            if credential.account == account:
                return True
            return False

    # Function to show all saved password credentials

    @classmethod
    def display_credentials(cls):

        return cls.credentials_list
