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

# Function to copy password to clipboard


def copy_password(account):
    return Credentials.copy_password(account)

    def locker():

        # Display welcome message
         print(" Hello, Welcome to Lock-R, A program built to store user credentials ...\n \n Please enter one of the following to proceed.\n CA ---  Sign in  \n LI ---  Have an account, Log in  \n")
    short_code = input("").lower().strip()

         if short_code == "ca":

        print("Fill in the details below")

        print('*' * 170)
        username = input("User_name: ")
        print('*' * 170)

        while True:
            print(" IP - To input own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()

            if password_Choice == 'ip':
                password = input("Enter Password\n")
                break

            elif password_Choice == 'gp':
                password = generate_Password()
                break

            else:
                print("Wrong password, please try again")