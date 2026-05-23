class Animal:
    def __init__(self):
        self.name = "Timmy"

    def speak(self):
        print(f"{self.name} can speak")


class Dog(Animal):
    def __init__(self,breed):
        #init from animal comes to dog 
        super().__init__()
        self.breed = breed
    
    def speak(self):
        #speak method from animal comes to dog class
        super().speak()
        print(f"{self.name} says Woof! , and it is a {self.breed}")

#But animal does not inherit any exclusive Dog method or attribute
#Anim = Animal("Timmy")
#Anim.speak()
#Anim.speak1() will throw an e3rror 

#Dog class inherits all attributs and methods of Animal class
Doggo = Dog("Timmy")
Doggo.speak()