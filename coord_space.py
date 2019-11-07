
#Class implementation of coordinate space
# For simplicity sake, let's restrict our coordinate space to first quadrant
# i.e. only positive values of x and y are accepted
class CoordinateSpace:
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
            # raise error as there cannot be two coordinate spaces
                raise DuplicateCoordSpaceError

    def getCoordX(self):
        return self.instance.coord_x

    def getCoordY(self):
        return self.instance.coord_y  


class CoordinateSpaceError(Exception):
    def __init__(self,):
    
        super().__init__()

class DuplicateCoordSpaceError(CoordinateSpaceError):
    def __init__(self):
        self.msg = "There can only be one coordinate space"

class PositiveCoordSpaceError(CoordinateSpaceError):
    def __init__(self):
        self.msg = "X and Y values must be positive"
        