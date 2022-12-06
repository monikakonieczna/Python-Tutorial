"""
Class feature:
    Single file per class OR multiple classes can be contained in one file
    python_programming: derived/child class can use attributes and methods of parent class
    Multiple inheritance: derived/child class can inherit attributes and methods from more than one class
    Polymorphism: derived/child classes can override class methods of parent class
    _init_ method: sets attributes for an object at object creation; is aa constructor
        is not required BUT is generally used to set default state of object when it is created
        is the first method for a class
    self variable: represents an instance of a class
        self-referencing variable
        used to reference the object that is constructed by the init method
"""
import random


class Person:
    def __init__(self, firstname, lastname, health, status):
        """initialize attributes to be used in/available for all \
        class methods in this class, and for class objects created \
        by this class"""

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        """All people introduce themselves"""
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1, 3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))


James = Person("James", "Bond", 95, status=True)
Indiana = Person("Indiana", "Jones", 100, status=False)
John = Person("John", "Smith", 33, status=True)

print("{} is my friend? {}".format(James.firstname, James.status))
print("{} is my friend? {}".format(Indiana.firstname, Indiana.status))

James.introduce()
Indiana.introduce()
John.introduce()

James.status_change()
Indiana.status_change()
John.status_change()


class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have you stuff!".format(other.firstname))
        if other.status:
            other.status = False


Ratcliffe = Enemy('rock', 'Governor', 'Ratcliffe', 75, status=False)
Freddy = Enemy('stick', 'Freddy', 'Krueger', 80, status=False)

Freddy.hurt(Indiana)
Ratcliffe.insult(John)
Freddy.steal(James)
Freddy.introduce()
