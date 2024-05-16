class Animal:

    def __init__(self, color):
        self.color = color

class Dog(Animal):

    def identify(self):
        print(f'This is a {self.color} dog.')

class Cat(Animal):

    def identify(self):
        print(f'This is a {self.color} cat.')
