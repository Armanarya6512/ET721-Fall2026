class Employee:
    raise_amt= 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    # @property decorator indicates that the methods will behave like an attribute
    
    @property
    def emailemployee(self):
        return f"{self.first[0].lower()}{self.last.lower()}@email.com"

    @property
    def fullname (self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

# local testing of the class
e = Employee("Arman", "Arya", 50000)
print(e.emailemployee) # armanarya@email.com
print(f"Current salary = {e.salary}")
e.apply_raise()
print(f" After raising the New salary = {e.salary}") # 52500