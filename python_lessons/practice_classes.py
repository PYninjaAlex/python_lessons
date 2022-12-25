class Point3D:
    '''класс для представления координат точек на плоскости'''
    x = 1
    y = 1
    z = 1

pt1 = Point3D()
pt2 = Point3D()
pt3 = Point3D()
# print(pt1.x, pt1.y, pt1.z)
# print(pt2.x, pt2.y, pt2.z)
# print(pt3.x, pt3.y, pt3.z)

def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n >= 5 and n < 10:
        return n * 95
    else:
        return n * 90

print(sale_hotdogs(100))


def is_isogram(string):
    string = string.lower()
    l = []
    s = ''
    if string != '':
        l.append(string[0])

    for i in string[1:]:

        if i not in l:
            l.append(i)
        else:
            return False

    s = ''.join(l)
    if s == string:
        return True

print(is_isogram('isIsogram '))