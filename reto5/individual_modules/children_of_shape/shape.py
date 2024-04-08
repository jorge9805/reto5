
from math import sqrt
class Point:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    def compute_distance(self,point):
        return sqrt((point.x-self.x)**2+(point.y-self.y)**2)
      
class Line:
    def __init__(self,start:Point,end:Point):
        self.start=start
        self.end=end
        self.length=start.compute_distance(end)    
class Shape:
    def __init__(self,lines,points):
        self.lines=lines
        self.points=points
        self.is_regular=self.compute_regular()
    def compute_regular(self):
        for i in range(len(self.lines)-1):
            if self.lines[i].length!=self.lines[i+1].length:
                return False
        return True
    def vertices(self):
        return len(self.points)
    def edges(self):
        return len(self.lines)
    def inner_angles(self):
        raise NotImplementedError("Subclass must implement this method")
    def compute_area(self):
        raise NotImplementedError("Subclass must implement this method")
    def compute_perimeter(self):
        raise NotImplementedError("Subclass must implement this method")