class Circle:
    def __init__(self,radius):
        self.r=radius

    def area(self):
        circle_area=3.14*self.r**2
        return f"The area of this circle is {circle_area}"

    def circumference(self):
        circle_circumference = 2*3.14*self.r
        return f"The circumference of this circle is {circle_circumference}"

my_circle=Circle(3) 
print(my_circle.area()) 
print(my_circle.circumference())  

class Square:
    def __init__(self,side):
        self.a=side

    def area(self):
        square_area=self.a**2
        return f"The area of this square is {square_area}"

    def perimeter(self):
        square_perimeter = 4*self.a
        return f"The perimeter of this square is {square_perimeter}"

my_square=Square(5) 
print(my_square.area()) 
print(my_square.perimeter()) 

class Rectangle:
    def __init__(self,side_w,side_l):
        self.w=side_w
        self.l=side_l

    def area(self):
        rectangle_area=self.w*self.l
        return f"The area of this rectangle is {rectangle_area}"

    def perimeter(self):
        rectangle_perimeter =2*(self.w+self.l)
        return f"The perimeter of this rectangle is {rectangle_perimeter}"

my_rectangle=Rectangle(7,8) 
print(my_rectangle.area()) 
print(my_rectangle.perimeter()) 

class Sphere:
    def __init__(self,r):
        self.radius=r

    def surface_area(self):
        sphere_surface_area=4*3.14*self.radius**2
        return f"The surface area of this sphere is {sphere_surface_area}"

    def volume(self):
        sphere_volume = 4/3*(3.14*self.radius**3)
        return f"The volume of this sphere is {sphere_volume}"

my_sphere=Sphere(10) 
print(my_sphere.surface_area()) 
print(my_sphere.volume()) 