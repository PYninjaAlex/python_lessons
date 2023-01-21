import random
import time
import os

count = 0
monster_names = ('Dragon', 'Ork', 'The Dead', "Puss in boots", "Shrek")
chance = 1 #random.randint(1, 2)


class Creature:
    def __init__(self, name, hp_player, power_attack_player, heal_player, armor_player):
        self.name = name
        self.hp = hp_player
        self.power_attack = power_attack_player
        self.heal = heal_player
        self.armor = armor_player

    def get_damage(self, enemy):
        self.hp -= enemy.power_attack

    def attack(self, enemy):
        enemy.hp -= self.power_attack

    def healing(self, count, test):
        if count != 2 and player.hp != test:
            player.hp += 10
            print(f'Количество здоровья после лечения: {player.hp}')
        else:
            print("Почему вы меня не послушали? Вы что думали что максивальное здоровье увеличится? В следующий раз будешь лучше меня слушать!")


class Hero(Creature):
    pass


class Monster(Creature):
    pass


name_player = input("What's your name? ")

player = Hero(name_player, random.randint(80, 100), 10, 10, 5)
monster = Monster(monster_names[random.randint(0, len(monster_names) - 1)], random.randint(80, 110), 10, 0, 3)
test = player.hp

print(f'Имя вашего героя: {player.name}')
print(f'Имя монстра: {monster.name}')
time.sleep(1)

while player.hp > 0 and monster.hp > 0:
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
            choice = int(input("Что вы хотите сделать?\t\n1.Атакавать\n2.Лечиться (не стоит лечиться если у вас и так полное здоровье и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))
        except Exception:
            print("Введите число!")
            choice = int(input(
                "Что вы хотите сделать?\t\n1.Атакавать\n2.Лечиться (не стоит лечиться если у вас и так полное здоровье и ещё нельзя лечиться более двух раз имей ввиду говорю один раз!)\n"))

        if choice == 1:
            print(f'Количество здоровья до удара: {monster.hp}')
            print("Мы атакуем!")
            player.attack(monster)
            time.sleep(1)
            print(f'Количество здоровья после удара: {monster.hp}')
            time.sleep(2)
            os.system("cls")
        elif choice == 2:
            print(f"Количество здоровья до лечения: {player.hp}")
            print("Мы лечимся!")
            time.sleep(1)
            player.healing(count, test)
            count += 1
            time.sleep(2)
            os.system("cls")