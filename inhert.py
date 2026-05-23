class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} can speak")


class Dog(Animal):
    def speak1(self):
        print(f"{self.name} says Woof!")

#But animal does not inherit any exclusive Dog method or attribute
Anim = Animal("Timmy")
Anim.speak()
#Anim.speak1() will throw an error 

#Dog class inherits all attributs and methods of Animal class
Doggo = Dog("Tommy")
Doggo.speak()
Doggo.speak1()