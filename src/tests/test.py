import sys
import os

from unittest.mock import patch
import unittest 


PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if PATH not in sys.path:
    sys.path.append(PATH)

import gm_resources

# Note, these tests might be seperated into different classes in the future.

class test(unittest.TestCase):
    '''@classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass'''

    def test_retrieveFile(self):
        with patch("gm_resources.requests.get") as mocked_get:
            mocked_get.return_value = "Hello World"
            rtnVal = gm_resources.retrieveFile("https://www.example.com", "Hello")
            self.assertEqual(rtnVal, "Hello World")
        pass



if __name__ == '__main__':
    unittest.main()