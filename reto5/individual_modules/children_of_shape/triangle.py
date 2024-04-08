from .shape import Shape
from math import sqrt
from .shape import Point,Line
class Triangle(Shape):
    def __init__(self,lines,points):
        super().__init__(lines,points)
        self.isTriangle=self.compute_triangle()
    def compute_triangle(self):
        if self.lines[0].length+self.lines[1].length>self.lines[2].length and self.lines[0].length+self.lines[2].length>self.lines[1].length and self.lines[1].length+self.lines[2].length>self.lines[0].length:
            return True
        return False
    def inner_angles(self):
        return 180
    def compute_area(self):
        return 0.5*abs((self.points[0].x*(self.points[1].y-self.points[2].y)+self.points[1].x*(self.points[2].y-self.points[0].y)+self.points[2].x*(self.points[0].y-self.points[1].y)))
    def compute_perimeter(self):
        return self.lines[0].length+self.lines[1].length+self.lines[2].length
class Equilateral(Triangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 60
    def compute_area(self):
        return (sqrt(3)/4)*self.lines[0].length**2
    def compute_perimeter(self):
        return 3*self.lines[0].length
class Isosceles(Triangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        return 0.5*self.lines[0].length*sqrt(self.lines[1].length**2-(self.lines[0].length/2)**2)
    def compute_perimeter(self):
        return self.lines[0].length+self.lines[1].length*2
class Scalene(Triangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        s=self.compute_perimeter()/2
        return sqrt(s*(s-self.lines[0].length)*(s-self.lines[1].length)*(s-self.lines[2].length))
    def compute_perimeter(self):
        return self.lines[0].length+self.lines[1].length+self.lines[2].length
class TriRectangle(Triangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        return 0.5*self.lines[0].length*self.lines[1].length
    def compute_perimeter(self):
        return self.lines[0].length+self.lines[1].length+self.lines[2].length
    
point = Point(0,0)
point2 = Point(1,0)
point3 = Point(0,1)
line = Line(point,point2)
line2 = Line(point2,point3)
line3 = Line(point3,point)
triangle = Triangle([line,line2,line3],[point,point2,point3])
print(triangle.vertices())
print(triangle.edges())
print(triangle.inner_angles())
print(triangle.compute_area())
print(triangle.compute_perimeter())
