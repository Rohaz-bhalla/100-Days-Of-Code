class Avengers:
    def captain_america(self, type_, strength):
        self.type = type_
        self.strength = strength

#Inefficient. You are repeating the code already written in the parent class. If Avengers changes, you have to change Thor too.
class Thor(Avengers):
    def __init__(self, type_, strength, level):
        self.type = type_
        self.strength = strength
        self.level = level

#Better. You are explicitly telling the Avengers class to do its job. However, you have to hard-code the name Avengers, which makes the code less flexible.
class Iron_man(Avengers):
    def __init__(self, type_, strength, level):
        Avengers.__init__(self, type_, strength) # Parent class main level nhi hai we have to mention explicitly
        self.level = level

#The Standard. super() automatically finds the parent class and calls its constructor. It’s clean, avoids repetition, and is the "Pythonic" way to handle inheritance.
class Black_panther(Avengers):
    def __init__(self, type_, strength, level):
        super().__init__(type_, strength) 
#We use super() as a "bridge" to send data from the child class up to the parent class so the parent can do the work it already knows how to do.
        self.level = level
