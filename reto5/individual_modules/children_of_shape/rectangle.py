from .shape import Shape
from .shape import Point,Line
class Rectangle(Shape):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        return self.lines[0].length*self.lines[1].length
    def compute_perimeter(self):
        return 2*(self.lines[0].length+self.lines[1].length)
class Square(Rectangle):
    def __init__(self,lines,points):
        super().__init__(lines,points)
    def inner_angles(self):
        return 90
    def compute_area(self):
        return self.lines[0].length**2
    def compute_perimeter(self):
        return 4*self.lines[0].length
    
print("rectangle")
point1=Point(0,0)
point2=Point(0,2)
point3=Point(3,2)
point4=Point(3,0)
line1=Line(point1,point2)
line2=Line(point2,point3)
line3=Line(point3,point4)
line4=Line(point4,point1)
rectangle=Rectangle([line1,line2,line3,line4],[point1,point2,point3,point4])
print("vertices,edges,inner_angles,area,perimeter")
print(rectangle.vertices())
print(rectangle.edges())
print(rectangle.inner_angles())
print(rectangle.compute_area())
print(rectangle.compute_perimeter())

