import re

my_str = "users[i] users[1] users[2] users[10]"

data = 'Today is 03.01.2023, and just recently it was 31.12.2022 last year?'
data2 = 'C:\\Users\\Document\\'

str_email = '''abs123@gmail.com
        dfe456@apple.com'''
def spec_symbols(str):

    result_1 = re.findall(r'(0[1-9]|[12][\d]|3[01])\.(0[1-9]|1[0-2])\.([12][09][\d][\d])', str)
    result_2 = re.findall(r'users\[[0-9]\]', str)
    result_3 = re.findall(r'[\D]', str)
    result_4 = re.findall(r'year?', str)
    result_5 = re.findall(r'C:\\Users\\', str)
    return result_1, result_2, result_3, result_4, result_5

def chech_email(email):

    res = re.findall(r'\w+@\w+\.\w+', email)
    return res


def check_phone_number():
    s_numbers = '''+7-912-345-67-89
    8-912-345-67-89'''
    result = re.findall(r'(\+7|8)-(9\d{2})-(\d{3})-(\d{2})-(\d{2})', s_numbers)
    print(result)


print(spec_symbols(data2))
print(spec_symbols(data))
print(spec_symbols(my_str))
print(chech_email(str_email))
check_phone_number()