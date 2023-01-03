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

# print(find_short("bitcoin take over the world maybe who knows perhaps"))
# print(controller('..P...O...'))
# print(sum_no_duplicates([1, 1, 2, 3]))
# print(invert([1,-2,3,-4,5]))
# print(repeat_str('abs'))
# print(add_length('y'))
# print(past(0, 1, 1))
# print(collatz(561))