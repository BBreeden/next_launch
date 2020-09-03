import launch
import unittest

class TestLaunchObject(unittest.TestCase):
    def test_img_url(self):
        ''' Test the img url to ensure it has a valid address '''
        l = launch.Launch()

        key = 'http'
        container = l.img_url
        self.assertIn(key, container)

    def test_net_string(self):
        ''' Test the NET string to ensure it contains a date. '''
        l = launch.Launch()

        key = '2020'
        container = l.net
        self.assertIn(key, container)

if __name__ == '__main__': 
    unittest.main()