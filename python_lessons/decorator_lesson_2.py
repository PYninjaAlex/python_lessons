import time
count = 0

def cash(func):
    dct = {}
    def wrapper(n):
        if n in dct.keys():
            res = dct[n]
        else:
            res = dct[n] = func(n)
        return res
    return wrapper


def login(func):
    def wrapper(n):
        print(f'{func.__name__} was called with {n} in time {time.process_time()}')
        return func(n)
    return wrapper
def timer(func):
    def wrapper(n):
        start = time.process_time()
        res = func(n)
        end = time.process_time()
        print(f'start: {start};\n end: {end};\n different: {end - start}')
    return wrapper

def counter(func):
    def wrapper(n):
        global count
        count += 1
        res = func(n)
        return res
    return wrapper

@cash
#@login
@counter
def fiba(n):
    if n < 2:
        return 1
    return fiba(n - 1) + fiba(n - 2)

@timer
def starter(n):
    fiba(n)


print(fiba(7))
print(count)
# starter(35)