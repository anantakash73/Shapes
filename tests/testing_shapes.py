import unittest
import sys 
import os
sys.path.append(os.path.abspath("/Users/anantakash/Shapes/"))

from shapes import *

class ShapeTests(unittest.TestCase):
    #test shape creationg
    def test_creation(self):
        #self.assertEqual(Shape(),)
        shape = Shape(1,2)
        
        self.assertEqual(shape.returnX(), 1)
        self.assertEqual(shape.returnY(), 2)
    #shape move
    def test_move(self):
        shape = Shape(3,4)
        shape.move(4,6)
        self.assertEqual(shape.returnX(), 4)
        self.assertEqual(shape.returnY(), 6)

    #shape resizing
    def test_resize(self):
        pass

    #shape rotation
    def test_rotate(self):
        pass



if __name__ == '__main__':
    unittest.main()

