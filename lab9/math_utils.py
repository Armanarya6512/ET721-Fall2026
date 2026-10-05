"""
Name: Arman Arya 
Lab9: unit testing using pytest
Date: October,05, 2026
"""
# exercise 1 
def multiply(a, b):
    
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# exercise 2
# Actions that validates a password: 8+ characters, contains at least one digit
def validate_password(password):
    if len(password) < 8:
        return False
    return any(char.isdigit() for char in password)

# exercise 3
# create a function to check if the number is even
def is_even(n):
    return n % 2 == 0  and n != 0
