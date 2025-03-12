class Bird():
    def fly(self):
        print('I can fly')

class Duck(Bird):
    # Violation of LSP
    # def fly(self):
    #     print('I can quack')
    pass

class Eagle(Bird):
    pass

d = Duck()
d.fly()

# Correct LSP
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented in subclasses")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



# The main issue with this implementation is that it violates LSP by introducing 
# a property in the Square class that is inconsistent with the base class Rectangle. 
# A Rectangle typically has independent width and height properties. By setting both to
# the same value in the Square class, we're imposing a constraint that isn't inherent to 
# all rectangles.

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Violation of LSP
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented in subclasses")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = self.height = side