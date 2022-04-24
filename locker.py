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
