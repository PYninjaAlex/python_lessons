# n = int(input(' Введите количество произведений '))
# b = []
# sum1 = 0
#
#
# def f1():
#     for i in range(n):
#         a = int(input(' input a '))
#         b.append(a)
#         return b
#
#
# print(f1())
#
#
# def f2(sum1 = 0):
#     for i in b:
#         sum1 += i
#         return sum1
#
#
# print(f2())




# def print_the_answer():
#     print(42)
# print_the_answer()


# def twinkle_twinkle():
#     print('Twinkle, twinkle, little star')
#     print('How I wonder what you are')
#     print('Up above the world so high')
#     print('Like a diamond in the sky')
#     print('Twinkle, twinkle, little star')
#     print('How I wonder what you are')
# def repeat_lyrics():
#     twinkle_twinkle()
#     twinkle_twinkle()
#
# repeat_lyrics()



def c_to_f():
    c = float(input(" Введите температуру в цельсиях "))
    f = (c * 9/5) + 32
    print(f'Температура в Фаренгейтах: {f}')

def f_to_c():
    f = float(input(" Введите температуру в Фаренгейтах "))
    c = (f - 32) * 5/9
    print(f'Температура в Цельсиях: {c}')


# c_to_f()
# f_to_c()

def convert_temp():
    scale = input(" Введите 'c': для Цельсии\nВведите 'f': для Фаренгейта\n ")
    if scale == 'f':
        f = float(input(" Введите температуру в Фаренгейтах "))
        c = (f - 32) * 5 / 9
        print(f'Температура в Цельсиях: {c}')
    elif scale == 'c':
        c = float(input(" Введите температуру в цельсиях "))
        f = (c * 9 / 5) + 32
        print(f'Температура в Фаренгейтах: {f}')
    else:
        print(' Хороших выходных! ')

# convert_temp()

def convert_temp_c_or_f():
    temp = input(' Введите градусы и шкалу (c или f) ')
    temp_int = int(temp[:-1])
    temp_str = temp[-1]
    if temp_str == 'f':
        c = (temp_int - 32) * 5 / 9
        temp_last = str(c) + 'c'
        print(temp_last)

    elif temp_str == 'c':
        f = (temp_int * 9 / 5) + 32
        temp_last = str(f) + 'f'
        print(temp_last)
    else:
        print(' Хороших выходных! ')

# convert_temp_c_or_f()


def twinkle_twinkle():
    print('Twinkle, twinkle, little star')
    print('How I wonder what you are')
    print('Up above the world so high')
    print('Like a diamond in the sky')
    print('Twinkle, twinkle, little star')
    print('How I wonder what you are')
def run_twinkle():
    times = int(input(' Сколько раз вызвать функцию '))
    for i in range(times):
        twinkle_twinkle()

# run_twinkle()

def add(first: int=42,second: float=15):
    print(first + second)

# add(int(input(' Введите число ')), -96)
# add()


def twinkle_twinkle():
    print('Twinkle, twinkle, little star')
    print('How I wonder what you are')
    print('Up above the world so high')
    print('Like a diamond in the sky')
    print('Twinkle, twinkle, little star')
    print('How I wonder what you are')

def repeat_twinkle(times = 1):
    if int(times) > 0:
        for i in range(times):
            twinkle_twinkle()
    else:
        print('Введите цифру')

# repeat_twinkle(4)


def summa(*numbers):
    '''кортеж'''
    print(sum(numbers))

# summa(1,2,6,8,9,5)


def brand(**brands):
    '''словарь'''
    print(brands)

# brand(a = 'apple', b = 'berry')
# print(repeat_twinkle())


def convert_c_f(temp: int, scale: str):
    if scale == 'f':
        c = (temp - 32) * 5 / 9
        return c
    elif scale == 'c':
        f = (temp * 9 / 5) + 32
        return f

a = convert_c_f(-1914,'c')
print(a)




def rec(i):
    if i <= 0:
        return 0
    else:
        print(i)
        i -= 1
        rec(i)

rec(5)