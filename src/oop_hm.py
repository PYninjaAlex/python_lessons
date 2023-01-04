class SQ:
    def get_sq(self):
        raise NotImplementedError('В дочернем классе должен быть переопределён метод get_sq')

class Rectangle(SQ):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sq(self):
        return self.a * self.b

class Square(SQ):
    def __init__(self, a):
        self.a = a

    def get_sq(self):
        return self.a ** 2

box = [Rectangle(2, 3), Rectangle(4, 5),
       Square(2), Square(6)]

for i in box:
    print(i.get_sq())