
class Shape:

    #Constructor
    def __init__(self, start_x, start_y):
        self.setX(start_x)
        self.setY(start_y)

    #Get X coordinate
    def returnX(self):
        return self.x

    #Get Y coordinate
    def returnY(self):
        return self.y
    
    #Set X coordinate
    def setX(self, new_x):
        self.x = new_x
    
    #Set X coordinate
    def setY(self, new_y):
        self.y = new_y

    #Set new X,Y coordinates
    def move(self, new_x, new_y):
        self.setX(new_x)
        self.setY(new_y)
    
    #abstract methods to be defined by children
    def resize(self,new_size):
        pass

    def rotate(self,angle):
        pass

    def draw_shape(self):
        pass

    
