import re


def test(email):
    if re.fullmatch(r"\w+\@\w+\.\w+", email):
        return True
    else:
        return False


def test_2(email):
    test_1 = False
    test_2_ = False
    for i in email:
        if i == "@":
            test_1 = True
        elif i == ".":
            test_2_ = True
    
    if test_2_ and test_1:
        return True
    else:
        return False              


variable = input("Введите email: ")
print(test(variable))
