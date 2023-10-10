##1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.




class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name : {self.name}, Age : {self.age} ")
    
    def get_info(self):
        print(f"Color of dog is {self.coat_color} ")
    

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color,weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def bark(self):
        print(f"{self.name} is Barking!")
    
    def jump(self):
        print(f"{self.name} is Jumping!")

    def details_jrt(self):
        print(f"Hello, I'm {self.name}, I am  {self.age} years old and my weight is {self.weight}")

class BullDog(Dog):
    def __init__(self, name, age, coat_color,weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def guard(self):
        print(f"{self.name} is a good guard dog for the home.")
    
    def run_slow(self):
        print(f"{self.name} runs slowly.")

    def details_bd(self):
        print(f"Hello, I'm {self.name}, I am  {self.age} years old and my weight is {self.weight}")





dog1 = JackRussellTerrier("Sheroo", 6, "White", "23 kg")
dog1.description()
dog1.get_info()
dog1.bark()
dog1.jump()
dog1.details_jrt()

print()

dog2 = BullDog("Moti", 4, "Brown", "25 kg")
dog2.description()
dog2.get_info()
dog2.guard()
dog2.run_slow()
dog2.details_bd()   
