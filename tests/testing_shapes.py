import unittest
import sys 
import os
sys.path.append(os.path.abspath("/Users/anantakash/Shapes/"))

from shapes import *

class ShapeTests(unittest.TestCase):
    #test shape creationg
    def test_creation(self):
        #self.assertEqual(Shape(),)
        pass
    #shape move
    def test_move(self):
        pass

    #shape resizing
    def test_resize(self):
        pass

    #shape rotation
    def test_rotate(self):
        pass

    #shape return values
    def test_return_values(self):
        pass


if __name__ == '__main__':
    unittest.main()

