import sys 
import os
sys.path.append(os.path.abspath("/Users/anantakash/Shapes/"))
import unittest
from coord_space import CoordinateSpace,DuplicateCoordSpaceError,PositiveCoordSpaceError

class SpaceTests(unittest.TestCase):
    
    #test space creation
    def test_creation(self):
        coord_space = CoordinateSpace(5,10)
        self.assertEqual(coord_space.getCoordX(),5)
        self.assertEqual(coord_space.getCoordY(),10)
    

    def test_duplicate(self):
        with self.assertRaises(DuplicateCoordSpaceError):
            CoordinateSpace(5,11)
    


if __name__ == '__main__':
    unittest.main()
