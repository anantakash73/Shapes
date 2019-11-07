from shapes import Shape, ShapeErrors, OutOfBoundShapeError

class Circle(Shape):
    def __init__(self, start_x, start_y, radius):
        Shape.__init__(self,start_x, start_y)
        if self.check_bounds(radius):
            self.setRadius(radius)
        else:
            raise OutOfBoundShapeError

    def check_bounds(self, radius):
        if self.getX() - radius > 0 and self.getX() < self.getCoordX() and self.getY() - radius > 0 and self.getY() + radius < self.getCoordY():
            return True
        else:
            return False
    
    def setRadius(self,new_radius):
        self.radius = new_radius

    def getRadius(self):
        return self.radius