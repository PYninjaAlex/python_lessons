# магазин который продает телефоны и ноутбуки одной модели
import os
import time

storage = [
    {
        "name": "Laptop",
        "price": 30000,
        "count": 1
    },
    {
        "name": "Phone",
        "price": 10000,
        "count": 1
    }
]

while True:
    user_choice = input("""Программа МАГАЗИНУС-ТОВАРУС 1.0 
ГЛАВНОЕ МЕНЮ
1 - Посмотеть содержимое склада
2 - Посчитать общую стоимость товаров
3 - Добавить товары
4 - Выход
Вводить сюда $>""")
    if user_choice == "1":
        os.system('cls')
        for i in storage:
            print(f'Товар:{i["name"]}\nЦена за штуку:{i["price"]}\nКоличество:{i["count"]}')
            print("-" * 30)
            time.sleep(0.5)
        input("Нажмите Enter чтобы продолжить")
        time.sleep(0.2)
        os.system('cls')
        time.sleep(0.5)
    elif user_choice == "2":
        total_cost_item = 0
        for i in storage:
            total_cost_item += i["price"] * i["count"]
        print(f"Общая стоимость всех товаров {total_cost_item}")
    elif user_choice == "3":
        user_choice = input("""МЕНЮ ДОБАВЛЕНИЯ ТОВАРОВ\nВыберите что хотите добавить\n1 - ноутбук\n2 - телефон""")
        if user_choice == "1":
            count_new_item = input("Введите количество товаров\nВводить сюда $>")
            if count_new_item.isdigit():
                count_new_item = int(count_new_item)
            else:
                raise "БЫЛА ВВЕДЕНА БУКВА А НАДО ЦИФРУ"

            storage[0]["count"] += count_new_item
            print(
                f"Товары были успешно добавлены\nбыло добавлено:{count_new_item}\nВсего товаров:{storage[0]['count']}")
        elif user_choice == "2":
            count_new_item = int(input("Введите количество товаров\nВводить сюда $>"))
            storage[1]["count"] = storage[1]["count"] + count_new_item
            print(
                f"Товары были успешно добавлены\nбыло добавлено:{count_new_item}\nВсего товаров:{storage[1]['count']}")
    elif user_choice == "4":
        print("Хороших выходных!")
        break
    else:
        print("Ошибка выбора")
