def my_dec(f):
    def wrapper(num):
        try:
            res = f(num)
            for j in res:



# @my_dec
def func(num):
    lst = []
    for i in range(1, num+1):
        lst.append(input(f'Введите имя {i}: '))
    return lst

print(func(2))
