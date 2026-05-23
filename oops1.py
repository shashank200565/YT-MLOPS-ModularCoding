#initiate a class
class Employee:
    #special method - constructor
    def __init__(self):
        print("object called so constructor will hit")
        self.id = 123
        self.salary = 50000
        self.designation = "Data Engineer"
    #making a method
    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")

#creating an object/instance of the class
sam = Employee()

print(sam.salary)
#printing a attribute
print(sam.id)
print(sam.designation)
#calling a method
sam.travel("Bangalore")

print(type(sam))