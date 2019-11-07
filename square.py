from shapes import Shape, OutOfBoundShapeError

class Square(Shape):
    def __init__(self, init_x, init_y, init_size):
        Shape.__init__(self, init_x, init_y)
        if self.check_bounds(init_size):
            self.setSize(init_size)
        else:
            raise OutOfBoundShapeError

    
    def check_bounds(self,size):
        if self.getX() + size < self.getCoordX() and self.getY() + size < self.getCoordY():
            return True
        else:
            return False
    
    def setSize(self,new_size):
        self.size = new_size