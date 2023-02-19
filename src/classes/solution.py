def cesar(text: str, step: int) -> str:
    alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    up_text = text.upper()
    output = ''
    for i in up_text:
        mesto = alfavit.find(i)
        new_mesto = mesto + step
        if i in alfavit:
            output += alfavit[new_mesto]
        else:
            output += i
    return output


def decode(text: str, step: int) -> str:
    alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    up_text = text.upper()
    output = ''
    for i in up_text:
        mesto = alfavit.find(i)
        new_mesto = mesto - step
        if i in alfavit:
            output += alfavit[new_mesto]
        else:
            output += i
    return output


print(cesar('якобы', 3))
print(decode('ВНСДЮ', 3))
