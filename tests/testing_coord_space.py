import sys 
import os
sys.path.append(os.path.abspath("/Users/anantakash/Shapes/"))
import unittest
from coord_space import CoordinateSpace,DuplicateCoordSpaceError

class SpaceTests(unittest.TestCase):
    
    #test space creation
    def test_creation(self):
        coord_space = CoordinateSpace(5,10)
        self.assertEqual(coord_space.getCoordX(),5)
        self.assertEqual(coord_space.getCoordY(),10)
    
    # def test_duplicate(self):
    #     coord_space = CoordinateSpace(5,10)
    #     try:
    #         with self.assertRaises(CoordinateSpace(6,11),DuplicateCoordSpaceError) as context:
    #             print(context.msg)
    #     except Exception as e:
    #         print(e.msg)
    #         # err_msg = 'There can be only one coordinate space'
    #         # print(e.msg)
    #         # self.assertEqual(e.msg,err_msg)

if __name__ == '__main__':
    unittest.main()
