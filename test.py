import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        """
        method to run before each test case
        """
        self.new_user = User("Collins", "Nyakoe", "12345")

    def test_init(self):
        """
        test if the object is initialized properly
        """ 
        self.assertEqual(self.new_user.user_name, "Collins")

        self.assertEqual(self.new_user.password, "12345")

    def test_save_user(self):
        """
        test if the user object is saved into the user list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    if __name__ == '__main__':
        unittest.main()

