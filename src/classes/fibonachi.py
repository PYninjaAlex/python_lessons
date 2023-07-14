def fib(n):
    res = [1, 1]
    yield res[0]
    yield res[1]
    for i in range(2, n):
        res.append(res[i - 2] + res[i - 1])
        yield res[-1]


print([x for x in fib(15)])
