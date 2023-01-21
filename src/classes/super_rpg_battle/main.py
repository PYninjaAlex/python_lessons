import random
import time
import os

count_player = 0
count_monster = 0
monster_names = ('Dragon', 'Ork', 'The Dead', "Puss in boots", "Shrek")


class Creature:
    def __init__(self, name, hp_player, power_attack_player, heal_player):
        self.name = name
        self.hp = hp_player
        self.power_attack = power_attack_player
        self.heal = heal_player

    def attack(self, enemy):
        enemy.hp -= self.power_attack

    def healing(self, count, test, player):
        if count != 2 and player.hp != test:
            print(f'Количество здоровья до лечения: {player.hp}')
            player.hp += 10
            print(f'Количество здоровья после лечения: {player.hp}')
        elif count != 2:
            print(
                "Почему ",player.name, "меня не послушали? Вы что думали что максивальное здоровье увеличится? В следующий раз будешь лучше меня слушать!")
        else:
            print("Попытки лечения кончились! Лечиться больше нельзя!")


class Hero(Creature):
    pass


class Monster(Creature):
    pass


name_player = input("Как тебя зовут? ")

player = Hero(name_player, random.randint(40, 50), 10, 10)
monster = Monster(monster_names[random.randint(0, len(monster_names) - 1)], random.randint(40, 60), 10, 0)
test_player = player.hp
test_monster = monster.hp

print(f'Имя вашего героя: {player.name}')
print(f'Имя монстра: {monster.name}')
time.sleep(2)

while player.hp > 0 and monster.hp > 0:
    chance = random.randint(1, 2)
    if chance == 1:
        print("Вы будете вытягивать жребий...")
        time.sleep(0.5)
        print("1...")
        time.sleep(0.5)
        print("2...")
        time.sleep(0.5)
        print("3...")
        print("Вы вытянули жребий! Поздравляю вы играете первым!")
        try:
            choice = int(input(
                "Что вы хотите сделать?\t\n1.Атакавать\n2.Лечиться (не стоит лечиться если у вас и так полное здоровье и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
        except Exception:
            print("Введите число!")
            choice = int(input(
                "Что вы хотите сделать?\t\n1.Атакавать\n2.Лечиться (не стоит лечиться если у вас и так полное здоровье и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))

        if choice == 1:
            print(f'Количество здоровья до удара: {monster.hp}')
            print("Мы атакуем!")
            player.attack(monster)
            time.sleep(2)
            print(f'Количество здоровья после удара: {monster.hp}')
            time.sleep(2)
            os.system("cls")
        elif choice == 2:
            print(f"Количество здоровья до лечения: {player.hp}")
            print("Мы лечимся!")
            time.sleep(2)
            player.healing(count_player, test_player, player)
            if count_player <= 2:
                count_player += 1
            time.sleep(4)
            os.system("cls")
        else:
            print("Варианта только два!")
            choice = int(input(
                "Что вы хотите сделать?\t\n1.Атакавать\n2.Лечиться (не стоит лечиться если у вас и так полное здоровье и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
            if choice == 1:
                print(f'Количество здоровья до удара: {monster.hp}')
                print("Мы атакуем!")
                player.attack(monster)
                time.sleep(2)
                print(f'Количество здоровья после удара: {monster.hp}')
                time.sleep(4)
                os.system("cls")
            elif choice == 2:
                print(f"Количество здоровья до лечения: {player.hp}")
                print("Мы лечимся!")
                time.sleep(2)
                player.healing(count_player, test_player, player)
                count_player += 1
                time.sleep(4)
                os.system("cls")
    else:
        print("Вы будете вытягивать жребий...")
        time.sleep(0.5)
        print("1...")
        time.sleep(0.5)
        print("2...")
        time.sleep(0.5)
        print("3...")
        print(f"Вы не вытянули жребий. Вы проиграли. ход: {monster.name}")
        choice = random.randint(1, 2)
        if choice == 1:
            print("Монстер решает атаковать.")
            print(f'Ваше здоровье до удара монстра: {player.hp}')
            print("Монстер атакует!")
            monster.attack(player)
            time.sleep(2)
            print(f'Ваше здоровье после удара: {player.hp}')
            time.sleep(4)
            os.system('cls')
        else:
            print("Монстер решает полечиться.")
            monster.healing(count_monster, test_monster, monster)
            count_monster += 1
            time.sleep(4)
            os.system('cls')

if monster.hp <= 0 and player.hp <= 0:
    print("Поздравляю вы выиграли!")

elif monster.hp <= 0:
    print("Поздравляю вы выиграли!")

else:
    print("Вы проиграли. В следующий раз повезёт!")