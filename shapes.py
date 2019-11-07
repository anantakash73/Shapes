from coord_space import CoordinateSpace

class Shape(CoordinateSpace):

    #Constructor
    def __init__(self, start_x, start_y,shape_type):
        if start_x < self.getCoordX() and start_y < self.getCoordY():
            self.setX(start_x)  
            self.setY(start_y)
            self.setType(shape_type)
        else:
            raise OutOfBoundShapeError
    #Get X coordinate
    def getX(self):
        return self.x


    #Get Y coordinate
    def getY(self):
        return self.y
    
    #Set X coordinate
    def setX(self, new_x):
        self.x = new_x
    
    #Set X coordinate
    def setY(self, new_y):
        self.y = new_y
    
    def setType(self,shape_type):
        self.shape_type = shape_type
    
    def getType(self):
        return self.shape_type

    #Set new X,Y coordinates
    def move(self, new_x, new_y):
        self.setX(new_x)
        self.setY(new_y)

    def check_collision(self, shape):
        pass
    

    #abstract methods to be defined by children
    def resize(self,new_size):
        pass

    def rotate(self,angle):
        pass

    def draw_shape(self):
        pass

    def check_bounds(self):
        pass


class ShapeErrors(Exception):
    def __init__(self):
        self.msg = "An error occured in Shapes"

class OutOfBoundShapeError(ShapeErrors):
    def __init__(self):
        self.msg = "Shape cannot be created outside of coordinate space"
