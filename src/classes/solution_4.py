import re


def booknames_test(books: str) -> str:
    output = ''
    books_list = books.split('\n')
    data = [x.strip() for x in books_list]
    for i in data:
        if re.search(' ', i):
            continue
        else:
            output += f'{i} '
    return output

print(booknames_test('''Муму
                     Евгений Онегин
                     Сияние
                     Мастер и Маргарита
                     Пиковая дама
                     Колобок'''))    
    