"""
student Name :- Arman Arya
Date :- September 14, 2026
Lab 4:- loops and conditional statements 
"""
print("\n----- example 1: -----")
# multi statement
age = 17
if(age>18):
    print("go to AC/DC concert")
elif age ==18:
    print("go see pink floyd")
else:
    print("go see meatloaf")

print("move on!")

print("\n----- example 2: -----")
annie = 1996
jane = 1999

if annie%4 ==0:
    print("Annie was born in a leap year")
elif jane%4 ==0:
    print("jane was born in a leap year")
else:
    print("None of them were born in a leap year")


print("\n----- example 3: -----")
age = int(input("student's age: "))
lunch = "none"

if age <9:
    lunch = "Milk"
elif age>=10 and age<=14:
    lunch = "sandwich"
elif age>=15 and age<=17:
    lunch= "burger"
else:
    lunch = "outof range" 

print(f"at age {age} the food is {lunch}")

print("\n----- example 5 -----")
for n in range(5,10):
    print(n, end="\t")

print("print 3, 2, 1")
for m in range(3,0,-1):
    print(m, end="\t")

print("\n----- example 5: For loop -----")
dates = [1982, 1980, 1973]
n = len(dates)
for year in dates:
    print(year)

for y in range(n):
    print(f"year {y+1} = {dates[y]}")

print("\n----- example 6-----")
colors = ['red', 'yellow', 'green', 'purple', 'blue']
for i,c in enumerate(colors):
    print(i,c)

print("\n----- example 7: while loop -----")
#use loop to check how many ratings is greater than or equal to 8 for list ratings
ratings = [5,7.5,8,9,6.2,8.8]
count = 0
index = 0
lenratings = len(ratings)
while(index < lenratings):
    if ratings[index] >=8:
        count+= 1

    index += 1
else: 
    print(f"There is/are {count} good-excellent rating/s ")


print("\n----- example 8:functions -----")
# define a function  to add 1 to a number. the number is passed to the function as argument
def add(n):
    updated = n+1
    print(f"{n} added 1 = {updated}")
    return updated

#call the function
m = add(6)
print(f"value of m = {m}")

print("\n----- example 9: functions to pass strings -----")
#define a function to concatenate two strings
def con(a,b):
    return(a + " - " + b)

# call the function
print(con("bayside","NY"))

print("\n----- EXERCISE 1: LOOPS -----")
"""
Given the list animals, create a new list with animals whose names are made of less than or equal to 6 letters
"""
animals = ['lion', 'giraffe', 'gorilla','parrots','crocodile', 'deer', 'swan']

small_animals = []

for animal in animals:
    if len(animal) <= 6:
        small_animals.append(animal)

print(small_animals)


print("\n----- EXERCISE 2:FUNCTIONS -----")
#define a function to find and return the average of grades in the list 'grades'
# average = sum all the grades / length of the list 'grades'
grade = [65, 87, 95, 77, 35]

def calculate_average(grades_total):
    # average = sum all the grades / length of the list
    if len(grades_total) == 0:
        return 0
    return sum(grades_total) / len(grades_total)
# Calling the function
average_grade = calculate_average(grade)
print(f"The average grade is: {average_grade}")