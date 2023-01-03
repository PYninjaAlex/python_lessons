import re

date1 = '31.12.2022'
date2 = '20.08.2014'
s1 = 'Hello, World!'
s2 = "Today is 03.01.2023, and just recently it was 31.12.2022 last year."

def date(str):

    result = re.findall(r'[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9][0-9][0-9]', str)
    return result

print(date(date1))
print(date(date2))
print(date(s1))
print(date(s2))