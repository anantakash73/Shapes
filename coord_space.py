
#Class implementation of coordinate space
# For simplicity sake, let's restrict our coordinate space to first quadrant
# i.e. only positive values of x and y are accepted
class CoordinateSpace(object):
    class __CoordinateSpace:
        def __init__(self, init_x, init_y):
            self.coord_x = init_x
            self.coord_y = init_y
    instance = None
    def __init__(self,init_x, init_y):
        if not CoordinateSpace.instance:
            if init_x > 0 and init_y > 0:
                CoordinateSpace.instance = CoordinateSpace.__CoordinateSpace(init_x,init_y)
            else:
                # raise error
                raise PositiveCoordSpaceError
        else:
            raise DuplicateCoordSpaceError
            # raise error as there cannot be two coordinate spaces
                

    def getCoordX(self):
        return self.instance.coord_x

    def getCoordY(self):
        return self.instance.coord_y
    
    
    def deleteInstance(self):
        self.instance = None
    


class CoordinateSpaceError(Exception):
    def __init__(self,):
    
        super().__init__()

class DuplicateCoordSpaceError(CoordinateSpaceError):
    def __init__(self):
        self.msg = "There can only be one coordinate space"

class PositiveCoordSpaceError(CoordinateSpaceError):
    def __init__(self):
        self.msg = "X and Y values must be positive"



def check_point_collision(point, x, y, size):
    if point[0] >= x and point[0] <= x + size and point[1] >= y and point[1] <= y + size:
        return True
    return False