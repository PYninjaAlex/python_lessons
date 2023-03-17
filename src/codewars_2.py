import math


def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif len(phrase) <= 3 or len(phrase[:size]) <= 3:
        return phrase[:size] + '...'
    else:
        return phrase[:size - 3] + '...'


def mango(quantity, price):
    return (quantity - quantity // 3) * price


def unique_in_order(sequence):
    output = []
    if len(sequence) == 0:
        return output
    elif len(sequence) == 1:
        output.append(sequence[0])
        return output
    else:
        for i in range(len(sequence)):
            if i == 0:
                output.append(sequence[i])
            elif i == len(sequence) - 1:
                if sequence[i] != sequence[i - 1]:
                    output.append(sequence[i])
            else:
                if sequence[i - 1] != sequence[i] and sequence[i + 1]:
                    output.append(sequence[i])
        return output


def is_square(n: int) -> True or False:
    if n >= 0:
        if n == 0:
            return True
        elif math.sqrt(n) == int(math.sqrt(n)):
            return True
        else:
            return False
    else:
        return False


def likes(names: list) -> str:
    if not names:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) >= 4:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


def alias_gen(f_name: str, l_name: str) -> str:
    if f_name[0].isdigit() or l_name[0].isdigit():
        return 'Your name must start with a letter from A - Z.'
    else:
        '''f_name and s_name are uploaded dicts in cata
            that why there is the syntax_error here.'''
        return FIRST_NAME[f_name[0].upper()] + ' ' + SURNAME[l_name[0].upper()]


def sum_of_integers_in_string(s: str) -> int:
    var_str = ''
    output_array = []
    for i in s:
        if i.isdigit():
            var_str += i
        else:
            var_str += '_'

    var_list = var_str.split('_')
    for i in range(len(var_list)):
        if var_list[i] != '':
            output_array.append(var_list[i])

    return sum(list(map(int, output_array)))


def multiplication_table(size: int) -> list[list[int]]:
    output = []
    var = []
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            var.append(i * j)
        output.extend([var])
        var = []
    return output


def strings_construction(A: str, B: str) -> int:
    testing = {}
    if set(A) == set(B):
        return len(B) // len(A)
    a_list = [x for x in A]
    for i in B:
        if i in a_list and i not in testing:
            testing[i] = A.count(i)
        elif i in testing:
            testing[i] += 1
    return min(testing.values()) if testing else 0


def mygcd(x: int, y: int) -> int:
    return math.gcd(x, y)


def second_symbol(s: str, symbol: str) -> int:
    s_list = [x for x in s]
    if s_list.count(symbol) == 1 or not s.count(symbol):
        return -1
    else:
        s_list.remove(symbol)
        return s_list.index(symbol) + 1


def is_merge(s: str, part1: str, part2: str) -> bool:
    for i in s:
        if i in part1 or i in part2:
            continue
        else:
            return False
    return True


def product_array(numbers: list[int]) -> list[int]:
    output = []
    for i in range(len(numbers)):
        var = 1
        for j in range(len(numbers)):
            if j == i:
                continue
            var *= numbers[j]
        output.append(var)
    return output


def computer_to_phone(numbers: str) -> str:
    output = ""
    key_dict = {
        "7": "1",
        "8": "2",
        "9": "3",
        "1": "7",
        "2": "8",
        "3": "9",
    }
    for i in numbers:
        if i not in key_dict:
            output += i
        else:
            output += key_dict[i]
    return output


def hyper_fact(num: int) -> int:
    if num != 1:
        return (num ** num * hyper_fact(num - 1)) % 1000000007
    return 1


def div_con(x: list[int, str]) -> int:
    num = 0
    for i in x:
        if type(i) == str:
            num -= int(i)
        else:
            num += i
    return num

# print(trim("Hello, world!", 8))
# print(mango(9, 5))
# print(unique_in_order("ABBCcA"))
# print(is_square(26))
# print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
# print(sum_of_integers_in_string("2 + 3 = "))
# print(multiplication_table(3))
# print(strings_construction("zzz","zzzzzzzzzzz"))
# print(my-gcd(30, 12))
# print(second_symbol('Hello world!!!', 'l'))
# print(is_merge('codewars', 'code', 'wars'))
# print(product_array([12, 20]))
# print(computer_to_phone('1234567890'))
# print(hyper_fact(5))
