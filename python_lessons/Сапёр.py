import random
print("""
закрытая ячейка у нас будет обозначаться 🎁  или 0 
мина  💥  или !
заминировано ❌  или Х
пустая 🟧 или -
""")
mine_mark = "💥"
planted = "❌"
empty = "🟧"
unknown = "🎁"

field = list(empty * 25)
user_field = list(empty * 25)

# 10 раз генерирует случайное число и
for i in range(10):
    random_index = random.randint(0, len(field)-1)
    while field[random_index] == "💥":
        random_index = random.randint(0, len(field) - 1)
    else:
        field[random_index] = "💥"
# print(field)
# print(user_field)
for i in range(5):
    for j in range(5):
        print(user_field[j+i], end=" ")
    print()