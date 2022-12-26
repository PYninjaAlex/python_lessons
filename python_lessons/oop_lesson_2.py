class Location:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check(cls, x):
        return type(x) in (int, float)

    def _set_settings(self, id, number):
        if self.__check(id) and self.__check(number):
            self.__id = id
            self.__number = number
        else:
            raise ValueError('Вы ввели неправильные данные. Введите числа.')

    def get_settings(self):
        return self.__id, self.__number


    def set_coord(self, x, y):
        if self.__check(x) and self.__check(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Вы ввели неправильные данные. Введите числа.')


    def get_coord(self):
        return self.__x, self.__y

loc = Location(5, 6)
loc.set_coord(1, 5)
loc._set_settings(563742491848285, 4124494844)

print(loc.get_coord())
print(loc.get_settings())