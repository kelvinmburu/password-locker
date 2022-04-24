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
