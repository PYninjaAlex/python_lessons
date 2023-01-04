import re

digit_string = '-900 +5 5 0.8'
def check_digit(str):

    result = re.findall(r'([-+01-9])(.|\d+|)(.\d+)', str)
    return result

print(check_digit(digit_string))