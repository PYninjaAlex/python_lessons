import re

def date():
    s = '31.12.2022'
    result = re.findall(r'[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9]', s)
    return result

print(date())