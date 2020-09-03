import launch
import unittest

class TestLaunchObject(unittest.TestCase):
    def test_img_url(self):
        ''' Test the img url to ensure it has a valid address. '''
        l = launch.Launch()
        self.assertIn('http', l.img_url)

    def test_net_string(self):
        ''' Test the NET string to ensure it contains a date. '''
        l = launch.Launch()
        self.assertIn('2020', l.net)
    
    def test_mission(self):
        ''' Ensure the mission name is a string. '''
        l = launch.Launch()
        self.assertIsInstance(l.mission, str)
    
    def test_mission_length(self):
        ''' Ensure the mission string is long enough to make sense. '''
        l = launch.Launch()
        self.assertGreater(len(l.mission), 3)

if __name__ == '__main__': 
    unittest.main()