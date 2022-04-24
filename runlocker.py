#!/usr/bin/env python3.8

from locker import User, Credentials


# Add graphics support

def graphics():
    print("              ___          ____       ______     _      _               _______                   ")
    print("              |  |       /     \    /   ____|   |  |  /  /              |   _   \                 ")
    print("              |  |      |   --   |  |   |       |  | /  /     _____     |  |_|   |                ")
    print("              |  |      |  |  |  |  |   |       |  |\  \     |_____|    |   _  _ /                 ")
    print("              |  |_____ |   --   |  |   |____   |  | \  \               |  |                      ")
    print("              |_______|  \______/    \______|   |_ |  \__\              | _|                      ")


print("                                                                                                      ")

graphics()

# Function to to create user account


def create_user(username, password):

    new_user = User(username, password)
    return new_user

# Function to save user account


def save_user(user):
    user.save_user()

# Function to display user account information


def display_user():
    return User.display_user()


# Function to create login user account

def login_user(username, password):
    check_user = Credentials.verify_user(username, password)
    return check_user

# Function to create user credential


def save_credentials(credentials):
    credentials.save_details()

# Function to display credentials for all user_list


def display_account_details():

    return Credentials.display_credentials()

# Function to delete a saved credentials


def delete_credential(credentials):
    credentials.delete_credentials()


# Function to display user account credentials

def find_credential(account):

    return Credentials.find_credential(account)

# Function to assess if a credential is available


def check_credential(account):

    return Credentials.if_credential_exist(account)

# Random password generation


def generate_random_password():
    auto_generated_password = Credentials.generate_random_password()
    return auto_generated_password
