import unittest
from locker import User
from locker import Credentials

# Section to test class methods


class TestClass(unittest.TestCase):

    # Function to test class methods
    def setUp(self):
        self.new_user = User('Kelvin', 'mburu')

    # Function to test user account

    def test_init(self):
        self.assertEquals(self.new_user.username, 'Kelvin')
        self.assertEquals(self.new_user.password, 'mburu')

    # Function to test user accounts

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
