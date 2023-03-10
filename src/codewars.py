import re
from math import floor


def find_short(s):
    sp = s.split()
    smallest = len(sp[0])
    for w in range(1, len(sp)):
        a = len(sp[w])
        if a < smallest:
            smallest = a

    return smallest


def controller(events):
    state = 2  # 0 opening, 1 closing, 2 not moving
    currentOpen = 0
    output = ""
    pause = False
    for i in range(len(events)):
        if events[i] == "P":
            if currentOpen == 0 and 2:
                state = 0
            elif currentOpen == 5 and 2:
                state = 1
            else:
                pause = not pause
        elif events[i] == "O":
            state = 1 - state
        if state == 0 and not pause:
            currentOpen = min(5, currentOpen + 1)
        elif state == 1 and not pause:
            currentOpen = max(0, currentOpen - 1)
        output += str(currentOpen)
    return output


def sum_no_duplicates(l):
    s = set(l)
    es = sum(l) - sum(s)
    return sum(s) - es


def invert(lst):
    output = list()
    if len(lst) == 0:
        return lst
    else:
        for i in lst:
            if i > 0:
                i -= i * 2
                output.append(i)
            else:
                abs_x = abs(i)
                output.append(abs_x)
        return output


def repeat_str(repeat, string):
    return string * repeat


def add_length(str_):
    output = []
    split_str = str_.split()
    for i in split_str:
        output.append(f"{i} {len(i)}")
    return output


def past(h, m, s):
    return ((h * 3600) + (m * 60) + s) * 1000


def collatz(n):
    output_lst = []
    while n > 1:
        output_lst.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    return len(output_lst) + 1


def solution(text, ending):
    l = len(ending)
    if text[:-l] + ending == text:
        return True
    else:
        return False


def powers_of_two_1(n):
    output = []
    for i in range(n + 1):
        output.append(2 ** i)
    return output


def powers_of_two_2(n):
    return [2 ** x for x in range(n + 1)]


def consonant_count(string):
    output = 0
    vowels = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    for i in string:
        if i.upper() in vowels:
            output += 1
    return output


def high(x):
    spl_x = x.lower().split()
    a = 0
    lst = []
    bin = {}
    bin['A'] = 1
    bin['B'] = 2
    bin['C'] = 3
    bin['D'] = 4
    bin['E'] = 5
    bin['F'] = 6
    bin['G'] = 7
    bin['H'] = 8
    bin['I'] = 9
    bin['J'] = 10
    bin['K'] = 11
    bin['L'] = 12
    bin['M'] = 13
    bin['N'] = 14
    bin['O'] = 15
    bin['P'] = 16
    bin['Q'] = 17
    bin['R'] = 18
    bin['S'] = 19
    bin['T'] = 20
    bin['U'] = 21
    bin['V'] = 22
    bin['W'] = 23
    bin['X'] = 24
    bin['Y'] = 25
    bin['Z'] = 26
    for i in spl_x:
        for j in i:
            a += bin[j.upper()]
        lst.append(a)
        a = 0
    output = spl_x[lst.index(max(lst))]
    return output


def min_min_max(arr):
    smallest = min(arr)
    largest = max(arr)
    for i in range(smallest + 1, largest):
        if i not in arr:
            minimumAbsent = i
            break
    return [smallest, minimumAbsent, largest]


def count_consonants(text):
    text_up = text.upper()
    output = set()
    vowels = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    for i in text_up:
        if i in vowels:
            output.add(i)
    return len(output)


def app_lst(count, out, output, s):
    for i in s:
        if len(out) < 3:
            out += i
            count += 1
        if count == 2:
            output.append(out)
            out = ''
            count = 0
    return output


def split_strings(s):
    out = ''
    output = []
    count = 0
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s + '_']
    elif len(s) % 2 == 0:
        return app_lst(count, out, output, s)
    else:
        s += '_'
        return app_lst(count, out, output, s)


def procedure(i):
    multiple = []
    sums = []
    obj = 0
    for j in range(i, 100 + 1):
        if j % i == 0:
            multiple.append(j)
    for k in multiple:
        for object in str(k):
            obj += int(object)
        sums.append(obj)
        obj = 0
    return sum(sums)


def reverse_words(str):
    return " ".join(str.split()[::-1])


def get_sum(a, b):
    output = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a + 1):
            output += i
        return output
    else:
        for i in range(a, b + 1):
            output += i
        return output


def digital_root(n):
    output = 0
    while n > 9:
        for i in str(n):
            output += int(i)
        n = output
        output = 0
    return n


def find_uniq(arr):
    i = arr[0]
    for j in range(1, len(arr)):
        if i == arr[j]:
            continue
        if i not in arr[1:]:
            return i
        else:
            n = arr[j]
            break
    return n


def find_smallest(numbers, to_return):
    if to_return == 'index':
        return numbers.index(min(numbers))
    else:
        return min(numbers)


def arr_check(arr):
    for i in arr:
        if type(i) is not list:
            return False
    return


def explode(arr):
    if type(arr[0]) == int and type(arr[1]) == int:
        return [arr] * (arr[0] + arr[1])
    elif type(arr[0]) == int or type(arr[1]) == int:
        return [arr] * arr[0] if type(arr[0]) == int else [arr] * arr[1]
    else:
        return 'Void!'


def date_checker(date):
    return True if re.findall(r'\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}', date) else False


def litres(time):
    output = 0
    for i in range(floor(time)):
        output += 0.5
    return floor(output)


def reverse_letter(string):
    return ''.join([x for x in string if x in re.sub("[^A-Za-z]", "", string)])[::-1]


def cakes(recipe, available):
    pre_output = set()
    output = []
    list_recipe = list(recipe.keys())
    list_awailable = list(available.keys())
    if [x for x in list_recipe if x not in list_awailable] != []:
        return 0
    elif len(list_awailable) < len(list_recipe):
        return 0
    else:
        for i in list_awailable:
            if i in list_recipe:
                if available[i] // recipe[i] != 0:
                    pre_output.add(available[i] // recipe[i])
                else:
                    return 0
            else:
                continue
        for x in pre_output:
            if output == []:
                output.append(x)
            if x not in output and x < max(output):
                output.append(x)
        return min(output)


# def sum_arrays(arrays, shift):
#     output = []
#     var_list = []
#     variable = 0
#     if shift == 0:
#         for i in arrays:
#             for j in i:
#                 variable += j
#                 var_list.append(variable)
#                 variable = 0
#         half = len(var_list) // 2
#         first_half = var_list[:half]
#         second_half = var_list[half:]
#         for i in range(half):
#             output.append(first_half[i] + second_half[i])
#     else:
#         for i in range(shift):
#             output.append(arrays[0][i])
#         for i in arrays:
#             count = 0
#             for j in i:
#                 if count != shift:
#                     count += 1
#                     continue
#                 variable += j
#                 var_list.append(variable)
#                 variable = 0
#         half = len(var_list) // 2
#         first_half = var_list[:half]
#         second_half = var_list[half:]
#         for i in range(half):
#             output.append(first_half[i] + second_half[i])
#                 for j in i:
#                     variable += j
#                     var_list.append(variable)
#                     variable = 0
#             half = len(var_list) // 2
#             first_half = var_list[:half]
#             second_half = var_list[half:]
#         for i in range(half):
#             output.append(first_half[i] + second_half[i])
#     return output


# print(find_short("bitcoin take over the world maybe who knows perhaps"))
# print(controller('..P...O...'))
# print(sum_no_duplicates([1, 1, 2, 3]))
# print(invert([1,-2,3,-4,5]))
# print(repeat_str('abs'))
# print(add_length('y'))
# print(past(0, 1, 1))
# print(collatz(561))
# print(solution('abc', 'bc'))
# print(powers_of_two_1(4))
# print(powers_of_two_2(4))
# print(consonant_count('Hello, world!'))
# print(high('man i need a taxi up to ubud'))
# print(min_min_max([23, 4, 5, 80, 70, 68 ]))
# print(count_consonants('Count my unique consonants!!'))
# print(split_strings('asdfads'))
# print(procedure(25))
# print(reverse_words("hello world!"))
# print(get_sum(-50, 0))
# print(digital_root(493193))
# print(find_uniq([1, 0, 0, 0]))
# print(find_smallest([5,4,3,2,1],"value"))
# print(arr_check([[1], [2], [3]]))
# print(explode([9, 3]))
# print(date_checker('01-09-2016 01:20'))
# print(litres(11.8))
# print(reverse_letter("hello@world!)"))
# print(cakes(recipe={'crumbles': 24, 'sugar': 89, 'nuts': 63},
#             available={'sugar': 9449, 'flour': 5102, 'cocoa': 9582, 'butter': 1443, 'crumbles': 6454, 'eggs': 245,
#                        'chocolate': 8204, 'pears': 8096, 'cream': 3821, 'milk': 9915}))