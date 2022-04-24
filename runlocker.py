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
                password = generate_random_password()
                break

            else:
                print("Wrong password, please try again")

        # Function to configure new user account

        save_user(create_user(username, password))
        print("*"*85)
        print(
            f"Dear {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*85)

    # User log in to Lock-Password

    elif short_code == "li":

        print(" ")
        print("*"*50)
        print("Enter Lock-P Username and Password to Log in:")
        print('*' * 50)
        print(" ")

        # Function to verify user login

        username = input("Username: ")
        password = input("password: ")
        login = login_user(username, password)

        if login_user == login:
            print(f"Hello {username}.Welcome back to Lock-P!")
            print('\n')

    while True:
        print("Use these codes:\n CC - New Credential \n VC - Display Credentials \n EC - look for existing credential \n GP - Generate A randomn password \n Del - Delete credential \n EX - Logout \n")
        short_code = input().lower().strip()

        # Function to ADD any new credential

        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Application name:  (e.g 'Instagram')")
            account = input().lower()
            print("Your Account username")
            userName = input()

            while True:
                print(
                    " TP - To type your own password: \n GP - To let Lock-P generate random Password for you")
                password_Choice = input().lower().strip()

                if password_Choice == 'tp':
                    password = input("Enter Your Own Password \n")
                    break

                elif password_Choice == 'gp':
                    password = generate_random_password()
                    break

                else:
                    print("Invalid password please try again")

                # Function to save new user credentials
                save_credentials(create_new_credential(
                    account, userName, password))
                print('\n')
                print(
                    f"Account Credential for:  {account} -  UserName:  {userName}  -  Password:  {password}  created and saved succesfully!")
                print('\n')

        # Function to view user credentials
        elif short_code == "vc":

            if display_accounts_details():
                print("Here's your list of saved Credentials: ")

                print('*' * 35)
                print('_' * 35)

                for account in display_accounts_details():
                    print(
                        f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_' * 35)
                print('*' * 35)

            else:
                print("No existing credential found...")

        # Elif function to check for existing credential in the application

        elif short_code == "ec":
            print("Enter the Application Name you want to search for")
            search_name = input().lower()

            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(
                    f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)

            else:
                print("That Credential does not exist")
                print('\n')
