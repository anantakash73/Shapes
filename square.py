from shapes import Shape, OutOfBoundShapeError, ShapeErrors
from coord_space import check_point_collision as cpc
class Square(Shape):
    def __init__(self, init_x, init_y, init_size):
        Shape.__init__(self, init_x, init_y,"square")
        if self.check_bounds(init_size):
            self.setSize(init_size)
        else:
            raise OutOfBoundShapeError

    
    def check_bounds(self,size):
        if self.getX() + size < self.getCoordX() and self.getY() + size < self.getCoordY():
            return True
        else:
            return False
    

        
    def check_collision(self,new_x,new_y,new_size, shape,shape_type):
        print(shape_type)
        if shape.getType() == 'square':
            # if new x and y coordinate lie within existing square, it's a collision
            points = [(new_x,new_y),(new_x,new_y+new_size),(new_x+new_size,new_y),(new_x+new_size,new_y+new_size)]
            for point in points:
                if cpc(point,shape.getX(),shape.getY(),shape.getSize()):
                    return True
            return False
            # if shape.getX() < new_shape.getX() < (shape.getX() + shape.getSize()):
            #     if (shape.getY() < new_shape.getY() < (shape.getX() + shape.getSize()):

            # if existing square's starting coordinate would lie within new square, also a collision

        elif shape.getType() == 'circle':
            pass
        elif shape.getType() == 'triangle':
            pass
        else:
            raise ShapeErrors

    # def move(self,new_x, new_y):
    #     for cls in Shape.__subclasses__():
    #         #return self.check_collision(new_x,new_y,self.getSize(),cls,cls.getType(cls))
    
    def setSize(self,new_size):
        self.size = new_size

    def getSize(self):
        return self.size



