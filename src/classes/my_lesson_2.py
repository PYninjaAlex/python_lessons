guess_number = int(input("Загадай число от 1 до 500, а я буду отгадывать! "))

"""
150 ты 

наш диапозон от 1 до 500 

копм выбирает среднее число 250 выдает его

дальше мы спрашиваем у пользователя 
1 - ты загадал это число 
2- загаданное число больше
3 - загаданное число меньше 

если пользователь ответил правду 
то продолжаем поиск по алгоритму 

если пользователь соврал 
то мы ему скажем не ври врунишка 
и повторим вопрос 

"""

def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            question = int(input(f"Это то число? -> {guess}\n1 - если это то число\n2 - если заданное число больше\n3 - заданное число меньше\n\t"))
            if guess == item and question != 1:
                print("Ах ты врунишка! ГОВОРИ ПРАВДУ!")
            else:
                print(f"Правильный ответ -> {guess}")
                break
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

my_list = [x for x in range(1, 501)]

binary_search(list=my_list, item=guess_number)