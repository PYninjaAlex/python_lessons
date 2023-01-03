import re

def my_search():
    s1 = 'I will load it in a minute.'
    s2 = 'I will publicate it in a minute.'

    result1 = re.search('load', s1)
    result2 = re.search('load', s2)
    try:
        print(result1.group(0))
        print(result2.group(0))
    except Exception:
        print('По такому шаблону фраза не нашлась.')

def my_search_2():
    s = 'Язык программирования Python - самый крутой язык программирования из всех языков программирования'
    s2 = 'cd ../.. | grep "privet"'
    s3 = r'c:\\Users\\'
    s4 = 'Анна Алла Абба Анла'

    res = re.findall(r'А[а-я][нл]а', s4)

    print(res)