def find_short(s):
    sp = s.split()
    smallest = len(sp[0])
    for w in range(1, len(sp)):
        a = len(sp[w])
        if a < smallest:
            smallest = a

    return smallest




def controller(events):
    state = 2 # 0 opening, 1 closing, 2 not moving
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
            state = 1-state
        if state == 0 and not pause:
            currentOpen = min(5, currentOpen+1)
        elif state == 1 and not pause:
            currentOpen = max(0, currentOpen-1)
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
    for i in range(n+1):
        output.append(2 ** i)
    return output

def powers_of_two_2(n):
    return [2 ** x for x in range(n+1)]

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
    for i in range(smallest+1, largest):
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

def split_strings(s):
    out = ''
    output = []
    count = 0
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s + '_']
    elif len(s) % 2 == 0:
        for i in s:
            if len(out) < 3:
                out += i
                count += 1
            if count == 2:
                output.append(out)
                out = ''
                count = 0
        return output
    else:
        s += '_'
        for i in s:
            if len(out) < 3:
                out += i
                count += 1
            if count == 2:
                output.append(out)
                out = ''
                count = 0
        return output


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