import unittest
import sys 
import os
sys.path.append(os.path.abspath("/Users/anantakash/Shapes/"))

from triangle import Triangle
from coord_space import CoordinateSpace
class RectangleTests(unittest.TestCase):
    #test shape creationg
    def test_creation(self):
        #self.assertEqual(Shape(),)
        CoordinateSpace(10,20)
        triangle = Triangle(0,0,0,5,5,0)

        self.assertEqual(triangle.getX(), 0)
        self.assertEqual(triangle.getY(), 1)
    # #shape move
    # def test_move(self):
    #     shape = Shape(3,4)
    #     shape.move(4,6)
    #     self.assertEqual(shape.returnX(), 4)
    #     self.assertEqual(shape.returnY(), 6)

    #shape resizing
    def test_resize(self):
        pass

    #shape rotation
    def test_rotate(self):
        pass



if __name__ == '__main__':
    unittest.main()

