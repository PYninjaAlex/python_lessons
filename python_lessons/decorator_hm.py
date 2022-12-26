def my_dec(f):
    def wrapper(num=0):
        output = 'Nothing wrong'
        try:
            res = f(num)
            for j in res:
                for k in j:
                    if k.isdigit():
                        output = 'Error'
                        raise ValueError('Введены неправильные данные. Введите буквы.')

        finally:
            print(output)
        return res
    return wrapper

@my_dec
def func(num):
    lst = []
    for i in range(1, num+1):
        lst.append(input(f'Введите имя {i}: '))
    return lst

print(func(2))
