# Classes

class Dog:
    def __init__ (self, name, age):
      self.name = name
      self.age = age
  
    def bark(self):
        print("woof!")

roger = Dog("Roger", 8)

print(roger.name)
print(roger.age)

print(roger.bark())

