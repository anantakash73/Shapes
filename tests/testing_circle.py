import unittest
import sys 
import os
sys.path.append(os.path.abspath("/Users/anantakash/Shapes/"))

from circle import Circle
from coord_space import CoordinateSpace
class CircleTests(unittest.TestCase):
    #test shape creationg
    def test_creation(self):
        #self.assertEqual(Shape(),)
        CoordinateSpace(10,20)
        circle = Circle(3,4,1)

        self.assertEqual(circle.getX(), 3)
        self.assertEqual(circle.getY(), 4)
        self.assertEqual(circle.getRadius(),1)
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

