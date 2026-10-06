"""
   Student Name: Arman Arya
   Lab5 :- Review of class, objects, methods and attributes
   september 16, 2026
"""
print("\n ------Example 1: class Circle--------")
class Circle():
    # values that needed to pass to the obeject of class circle
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    # attributes
    pi = 3.14157

    #method
    def circumference(self):
        return 2 * self.pi * self.radius

#create instance object of class
c1 = Circle(2, "red")
print(c1.color)
print(c1.circumference())

print("\n ------Example 2: class Rectangle--------")
import matplotlib.pyplot as plt
class Rectangle:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

    # method to calculate the area
    def area(self):
        return self.height * self.width

    # method to calculate the perimeter
    def perimeter(self):
        return 2 * (self.height + self.width)
    #method to draw the rectangle
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()

# create instance object of class
r1 = Rectangle(2, 3, "olive")
print(f"The perimeter of rectangle with height={r1.height}, width={r1.width} is: {r1.perimeter()}")
r1.drawRectangle()


"""
Car dealership's invertory management system
you are working on a python program to simulate a car dealership's inventory management system. The system aims to model cars and thier attributes accurately.
Task1: create a class to represent each vehicle. Each car should have attributes for maximum speed and mileage.
Task2: update the class with the default color for all vehicles, "white".
Task3: create a class method to assign seating capacity to a vehicle 
Task4: create a class method to display all the properties of an object class --> "The____(color) car has____ seats, with___ miles and a maximum speed of ____"
Task5: create two instance objects of the car. One car will have a max speed of 200kph and milegae of 50000 kmpl with five seating capacity. The other car max speed = 180kph, mileage = 75000kmpl, four-seating. 
"""

# Task 1 & 2: Creating the class with attributes and a default color
class Car:
    color = "white"  # Default color for all cars I assume

    def __init__(self, speed, miles):
        self.max_speed = speed
        self.mileage = miles
        self.seats = 0  # Starts at 0 until assigned


# Task 3: function inside the class to assign seats
def set_seats(car_object, total_seats):
    car_object.seats = total_seats


# Task 4: print the properties
def print_details(car_object):
    print(
        "The "
        + car_object.color
        + " car has "
        + str(car_object.seats)
        + " seats, with "
        + car_object.mileage
        + " and a maximum speed of "
        + car_object.max_speed
    )


# Task 5: Creating the first car, assign seats, and print
car1 = Car("200kph", "50000 kmpl")
set_seats(car1, 5)
print_details(car1)

# Creating the second car, assign seats, and print
car2 = Car("180kph", "75000 kmpl")
set_seats(car2, 4)
print_details(car2)
