import random
import time
import os
from dataclasses import dataclass

count_player = 0  # Проверка попыток лечения игрока
count_monster = 0  # Проверка попыток лечения монстра
monster_names = (
    'Dragon', 'Ork', 'The Dead', "Puss in boots", "Shrek")  # Кортеж который содержит в себе все ииена монстров


@dataclass
class Creature:
    '''Родительский класс сушество.'''
    name: str
    hp: int
    power_attack: int
    heal_player: int

    def attack(self, enemy, player):
        '''Персонаж атакует.'''
        print(f'Количество здоровья {enemy.name} до удара: {enemy.hp}')
        print(f"{player.name} атакует!")
        enemy.hp -= self.power_attack
        time.sleep(2)
        print(f'Количество здоровья {enemy.name} после удара: {enemy.hp}')
        time.sleep(3)
        os.system("cls")

    def healing(self, count, test, hero, player):
        '''Персонаж лечится.'''
        if count <= 2 and hero.hp != test:
            print(f'Количество здоровья {hero.name} до лечения: {hero.hp}')
            if hero.name == player.name:
                print(f"Вы лечитесь!")
            else:
                print(f'{hero.name} решает полечиться!')
            time.sleep(3)
            hero.hp += 10
            print(f'Количество здоровья {hero.name} после лечения: {hero.hp}')
        elif hero.hp == test:
            print(
                "Почему", hero.name,
                "меня не послушали? Вы что думали что максивальное здоровье увеличится? В следующий раз будешь лучше меня слушать!")
        else:
            print("Попытки лечения кончились! Лечиться больше нельзя!")
        if hero.name == player.name:
            global count_player
            if count_player <= 2:
                count_player += 1
        else:
            global count_monster
            if count_monster <= 2:
                count_monster += 1

        time.sleep(4)
        os.system("cls")


class Hero(Creature):
    '''Дочерний класс нашего героя.
        В разработке...'''
    pass


class Monster(Creature):
    '''Дочерний класс монстра.
        В разработке...'''
    pass

def welcome():
    '''Функция добро пожаловать.'''
    print("Добро пожаловать в игру!")
    time.sleep(1)
    print(f"Сегодня, {name_player}, тебе придётся сразиться с {monster.name}!\nЖелаю тебе удачи!")
    time.sleep(2)
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(0.5)
    print("К бою!")
    time.sleep(1)

name_player = input("Как тебя зовут? ")  # Имя героя
player = Hero(name_player, random.randint(40, 50), 10, 10)  # Создаём игрока
monster = Monster(monster_names[random.randint(0, len(monster_names) - 1)], random.randint(40, 60), 10,
                  0)  # Создаём монстра

test_player = player.hp  # Начальное здоровье игрока или маскимальное здоровье игрока
test_monster = monster.hp  # Начальное здоровье монстра или маскимальное здоровье монстра


def asking():
    '''Принимаем главную информацию.
        И выводим её.'''
    os.system('cls')
    print(f'Имя вашего героя: {player.name}')
    print(f'Имя монстра: {monster.name}')
    time.sleep(2)


def game(player, monster, test_player, test_monster):
    '''Запук игры.'''
    while player.hp > 0 and monster.hp > 0:  # Пока кто-то не умер.
        chance = random.randint(1, 2)  # Шанс это жребий.

        def chance_func():
            '''Основная функиция игры.
                Делаем проверку на жребий.'''
            if chance == 1:
                print("Вы будете вытягивать жребий...")
                time.sleep(0.5)
                print("1...")
                time.sleep(0.5)
                print("2...")
                time.sleep(0.5)
                print("3...")
                print("Вы вытянули жребий! Поздравляю вы играете первым!")
                '''Обрабатываем ошибки.'''
                try:
                    choice = int(input(  # Выбор игрока
                        "Что вы хотите сделать?\t\n1.Атакавать\n2.Лечиться (не стоит лечиться если у вас и так полное здоровье и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
                except Exception:
                    print("Введите число!")
                    choice = int(input(
                        "Что вы хотите сделать?\t\n1.Атакавать\n2.Лечиться (не стоит лечиться если у вас и так полное здоровье и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
                '''Переходим к проверке выбора.'''
                if choice == 1:
                    player.attack(monster, player)
                elif choice == 2:
                    player.healing(count_player, test_player, player, player)
                # Опять обрабатываем ошибки.
                else:
                    print("Варианта только два!")
                    choice = int(input(
                        "Что вы хотите сделать?\t\n1.Атакавать\n2.Лечиться (не стоит лечиться если у вас и так полное здоровье и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
                    if choice == 1:
                        player.attack(monster, player)
                    elif choice == 2:
                        player.healing(count_player, test_player, player, player)

            else:
                print("Вы будете вытягивать жребий...")
                time.sleep(0.5)
                print("1...")
                time.sleep(0.5)
                print("2...")
                time.sleep(0.5)
                print("3...")
                print(f"Вы не вытянули жребий. Ход: {monster.name}")
                choice = random.randint(1, 2)  # Для монстра выбор случайный!
                if choice == 1:
                    monster.attack(player, monster)
                else:
                    monster.healing(count_monster, test_monster, monster, player)

        chance_func()


'''Обрабатываем полледние данные и выводим результат игры.'''


def finish(monster, player):
    '''Завершение игры.'''
    if monster.hp <= 0 and player.hp <= 0:
        print("Поздравляю вы выиграли!")

    elif monster.hp <= 0:
        print("Поздравляю вы выиграли!")

    else:
        print("Вы проиграли. В следующий раз повезёт!")


welcome()
asking()
game(player, monster, test_player, test_monster)
finish(monster, player)
