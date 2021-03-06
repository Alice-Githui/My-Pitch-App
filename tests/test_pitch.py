import unittest
from app.models import Pitch
from app import db

class PitchTest(unittest.TestCase):
    '''
    Test to check the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        set up method that runs every time our app is instantiated
        '''
        self.new_pitch=Pitch(pitch_id=1234,pitch_title='Good Grades', pitch_description='Predict student grades', pitch_user_id=12, pitch_category='Creative', pitch_comment='Great Concept', pitch_upvote=0, pitch_downvote=0)

    def tearDown(self):
        Pitch.query.delete()
               

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_id, 1234)
        self.assertEquals(self.new_pitch.pitch_title, 'Good Grades')
        self.assertEquals(self.new_pitch.pitch_description,'Predict student grades')
        self.assertEquals(self.new.pitch.pitch_user_id, 123)
        self.assertEquals(self.new_pitch.pitch_category,'Business')
        self.assertEquals(self.new_pitch.pitch_comment,'Great')
        self.assertEquals(self.new_pitch.pitch_upvote, 0)
        self.assertEquals(self.new_pitch.pitch_downvote, 0)

if __name__ =='__main__':
    unittest.main()