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

     def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class
    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credential = Credentials('Gmail','LeonDante','4fhGifd74')
    def test_init(self):
        """
        check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'Leon_Dante')
        self.assertEqual(self.new_credential.password,'fsdjis73')    

if __name__ == "__main__":
    unittest.main()