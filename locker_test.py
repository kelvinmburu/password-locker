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


class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_credential = Credentials('Gmail', 'Kelvin', 'mburu')

        def test_init(self):

            self.assertEqual(self.new_credential.account, 'Gmail')
            self.assertEqual(self.new_credential.userName, 'Kelvin')
            self.assertEqual(self.new_credential.password, 'mburu')

    # Test function for credential user list validation

    def save_credential_test(self):

        self.new_credential = self.details()
        self.assertEqual(len(Credentials.credentials_list), 1)

    # Clear credentials after test case running

    def test_save_many_credentials(self):
        self.new_credential.save.details()
        test_credential = Credentials("KM", "Kevo", "maumau700")
        test_credential.save.details()
        self.assertEqual(len(Credentials.credentials_list), 2)

    # Test to delete a credential

    def test_delete_credential(self):

        self.new_credential.save_details()
        test_credential = Credentials("KM", "Kevo", "maumau700")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    # Test to a find a user credential

    def test_find_credential(self):

        self.new_credential.save_details()
        test_credential = Credentials("KM", "Kevo", "maumau700")
        test_credential.save_details()

        the_credential = Credentials.find_credential("KM")

        self.assertEqual(the_credential.account, test_credential.account)

    # Test to get Boolean value of user credentials

    def test_credential_exists(self):

        self.new_credential.save_details()
        the_credential = Credentials("KM", "Kevo", "maumau700")
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("KM")
        self.assertTrue(credential_is_found)

    # Test to dislay when a credential is found
    def test_credential_all_saved_credentials(self):

        self.assertTrue(Credentials.display_credentials(),
                        Credentials.credentials_list)


if __name__ == "__main__":
    unittest.main()
