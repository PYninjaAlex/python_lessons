class PR:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть переопределён метод get_pr')
class Rectangle(PR):

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)

class Square(PR):

    def __init__(self, a):
        self.a = a
    def get_pr(self):
        return 4 * self.a

class Triangle(PR):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c

box = [Rectangle(1, 2), Rectangle(1, 3),
       Square(10), Square(20),
       Triangle(1, 2, 3), Triangle(4, 5, 6)]

for i in box:
    print(i.get_pr())

# print(r1.get_rect_pr(), r2.get_rect_pr())
# print(s1.get_sq_pr(), s2.get_sq_pr())