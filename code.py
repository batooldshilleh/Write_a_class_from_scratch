# Write the class Point as outlined in the instructions
import math
class Point():
    def __init__ (self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def reflect(self,axis):
        if axis == 'y':
            self.x = -(self.x)
        else:
            self.y = -(self.y)


pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())
