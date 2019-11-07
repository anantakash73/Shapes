from shapes import Shape,OutOfBoundShapeError

class Triangle(Shape):
    def __init__(self, init_x_1,init_y_1,init_x_2,init_y_2,init_x_3,init_y_3):
        Shape.__init__(self,init_x_1,init_y_1,"triangle")
        if self.check_bounds(init_x_1,init_y_1,init_x_2,init_y_2,init_x_3,init_y_3):
            self.setPoints(init_x_1,init_y_1,init_x_2,init_y_2,init_x_3,init_y_3)
        else:
            raise OutOfBoundShapeError
    def check_bounds(self,init_x_1,init_y_1,init_x_2,init_y_2,init_x_3,init_y_3):
        if self.getCoordX() < any([init_x_1,init_x_2,init_x_3]) or 0 > any([init_x_1,init_x_2,init_x_3]):
            return False
        if self.getCoordY() < any([init_y_1,init_y_2,init_y_3]) or 0 > any([init_y_1,init_y_2,init_y_3]):
            return False
        return True

    def setPoints(self,init_x_1,init_y_1,init_x_2,init_y_2,init_x_3,init_y_3):
        self.x_1 = init_x_1
        self.y_1 = init_y_1
        self.x_2 = init_x_2
        self.y_2 = init_y_2
        self.x_3 = init_x_3
        self.y_3 = init_y_3
