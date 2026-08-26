class Person:
    def __init__(self, name, age, course, gender):
        self.name = name
        self.age = age
        self.course = course
        self.gender = gender
    def talks(self,words):
        print(f"{self.name} talks and says {words}")


person1 = Person("Ancy Niya",18,"Software develpment","Female")
print(type(person1))
print(person1.name)
print(person1.age)
print(person1.course)
print(person1.gender)

person1.talks("OOP is just too easy")

print("-------------------------------")

person2 = Person("Tara tacy",22,"Nursing","Female")
print(type(person2))
print(person2.name)
print(person2.age)
print(person2.course)
print(person2.gender)

person2.talks("OOP is just too easy")


class Animal:
    def _init_(self,name,type):
        self.name = name
        self.type = type

    def make_sound(self):
        print(f"(self.name) makes some sound")


class Dog(Animal):
    def __init__(self,name,type,age):
        super().__init__(name,type)
        self.age = age







