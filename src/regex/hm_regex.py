import re

data = '''Today is 03.01.2023, and just recently it was 31.12.2022 last year.
    20.08.2014 31.12.2022 45.03.2004 12.15.1998 10.08.1005 00.11.2009
'''

def date(str):

    result = re.findall(r'(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.([12][09][0-9][0-9])', str)
    return result

print(date(data))