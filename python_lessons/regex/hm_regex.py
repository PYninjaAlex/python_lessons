import re

date1 = '31.12.2022'
date2 = '20.08.2014'
s1 = 'Hello, World!'

def date(str):

    result = re.findall(r'[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9][0-9][0-9]', str)
    return result

print(date(date1))
print(date(date2))
print(date(s1))