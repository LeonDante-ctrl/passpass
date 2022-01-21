import unittest
from pword import User

class UserTest(unittest.TestCase):
    '''
    A Test class that defines test cases for the User class.
    '''
    def setUp(self):
        '''
        runs before each individual test methods run.
        '''
        self.new_user = User('DanteDante','sdhu34ydhu')

    def test_init(self):
        '''
        check if the object has been initialized correctly
        '''
        self.assertEqual(self.new_user.username,'Danteiusimus')
        self.assertEqual(self.new_user.password,'yernannylovesmeballs')

if __name__ == "__main__":
    unittest.main()