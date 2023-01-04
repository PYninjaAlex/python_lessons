import re

digit_string = '-900 +5 5 90.8 -12.34'

def check_digit(str):

    result = re.findall(r'([-+]?\d+)(\.\d+|\d+)|(\d+)', str)
    return result

print(check_digit(digit_string))