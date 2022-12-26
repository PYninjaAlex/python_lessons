def my_dec2(f):
    def wrapper(b=1):
        result = f(b)
        return result
    return wrapper

def my_decorator(f):
    def wrapper(b=1):
        print('До вызова функции')
        try:
            res = f(b)
        except Exception:
            print('Введены непрвильные данные')
            res = -1
        return res
    return wrapper

@my_dec2
@my_decorator
def f(b):
    a = int(input('Введите данные: '))
    return a



@my_decorator
def f1(b):
    a = float(input('Введите дробные данные: '))
    return a + b

print(f1(12))
print(f())