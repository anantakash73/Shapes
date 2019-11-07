import unittest
import sys 
import os
sys.path.append(os.path.abspath("/Users/anantakash/Shapes/"))

from square import Square
from coord_space import CoordinateSpace
from shapes import OutOfBoundShapeError
CoordinateSpace(10,20)
class SquareTests(unittest.TestCase):
    #test shape creationg

    def test_creation(self):
        #self.assertEqual(Shape(),)
        
        square = Square(1,2,1)

        self.assertEqual(square.getX(), 1)
        self.assertEqual(square.getY(), 2)
    
    def test_creation_fail(self):
        with self.assertRaises(OutOfBoundShapeError):
            Square(10,20,1)
    # #shape move
    # def test_move(self):
    #     square = Square(3,4,2)
    #     square_2 = Square(1,1,2)
    #     #print(square.check_collision(5,5,2,square_2))

    #     square_2.move(2,2)
    #     # self.assertEqual(square.getX(), 4)
    #     # self.assertEqual(square.getY(), 6)

    #shape resizing
    def test_resize(self):
        pass

    #shape rotation
    def test_rotate(self):
        pass



if __name__ == '__main__':
    unittest.main()

