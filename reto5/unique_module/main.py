from shape_package.shape import Point,Line,Equilateral,Square,Shape


def main():
    print("equilateral triangle")
    point1=Point(0,0)
    point2=Point(3,0)
    point3=Point(1.5,3)
    line1=Line(point1,point2)
    line2=Line(point2,point3)
    line3=Line(point3,point1)
    equilateral=Equilateral([line1,line2,line3],[point1,point2,point3])
    print("vertices,edges,isTriangle,inner_angles,area,perimeter")
    print(equilateral.vertices())
    print(equilateral.edges())
    print(equilateral.isTriangle)
    print(equilateral.inner_angles())
    print(equilateral.compute_area())
    print(equilateral.compute_perimeter())

    print("square")
    point1=Point(0,0)
    point2=Point(3,0)
    point3=Point(3,3)
    point4=Point(0,3)
    line1=Line(point1,point2)
    line2=Line(point2,point3)
    line3=Line(point3,point4)
    line4=Line(point4,point1)
    square=Square([line1,line2,line3,line4],[point1,point2,point3,point4])
    print("vertices,edges,inner_angles,area,perimeter")
    print(square.vertices())
    print(square.edges())
    print(square.inner_angles())
    print(square.compute_area())
    print(square.compute_perimeter())

if __name__ == "__main__":
    main()