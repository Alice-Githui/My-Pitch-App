import unittest
from app.models import User,Comment,Pitch
from app import db

class UserModelTest(unittest:TestCase):

    def setUp(self):
        self.new_user=User(password='banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

class PitchTest(unittest:TestCase):
    '''
    Test to check the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        set up method that runs every time our app is instantiated
        '''
        self.new_pitch=Pitch(1234, 'Good Grades', 'Predict student grades', 12, 'Creative', 'Great Concept', '1', '2')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

if __name__ == '__main__':
    unittest.main()

    