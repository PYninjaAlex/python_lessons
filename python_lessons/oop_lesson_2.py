class Location:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __set_settings__(self, id, number):
        self.__id = id
        self.__number = number

    def get_settings(self):
        return self.__id, self.__number

    def set_coord(self, x, y):
        self.__x = x
        self.__y = y

    def get_coord(self):
        return self.__x, self.__y

loc = Location(5, 6)
loc.set_coord(1, 5)
loc.__set_settings__(563742491848285, 4124494844)

print(loc.get_coord())
print(loc.get_settings())