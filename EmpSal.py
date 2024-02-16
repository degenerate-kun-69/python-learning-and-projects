class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  
        self._increment = 0  

    @property
    #salary property
    def salary(self):
        return self._salary

    @property
    #increment property
    def increment(self):
        return self._increment

    @increment.setter
    #setter method for increment
    def increment(self, value):
        if value < 0:
            raise ValueError("Increment should be a non-negative value.")
        self._increment = value
        self._salary += value


employee1 = Employee("Joe", 50000)#create object for employee class by passing name and salary to constructor
print(f"{employee1.name}'s salary: Rs.{employee1.salary}")
print(f"{employee1.name}'s increment: Rs.{employee1.increment}")

#invoke increment method
employee1.increment = 5000

print(f"After increment, {employee1.name}'s salary: Rs.{employee1.salary}")
print(f"After increment, {employee1.name}'s increment: Rs.{employee1.increment}")
