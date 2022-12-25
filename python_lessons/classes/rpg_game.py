import random
import time

possible_rarity = ["обычный", "редкий", "легендарный"]

hero_hp = 100
hero_damage = 9
hero_level = 1

monster1_hp = 50
monster1_damage = 10
monster1_lvl = 1
monster1_rarity = random.choice(possible_rarity)

print("Вы встретили монстра и он", monster1_rarity, "уровень", hero_level)

while hero_hp > 0 and monster1_hp > 0:  # будет повторять код до тех  пор пока у героя и у монстра здоровье больльше нуля
    print("Здоровье монстра:", monster1_hp)
    print("Максимальный урон монстра", monster1_damage)
    print("Здоровье героя:", hero_hp)
    print("Максимальный урон героя", hero_damage)

    choice_user = input("Введите действие 1 - Атака, 2 - Уклонение")

    time.sleep(0.7)
    print("Вы берете свой меч... ")
    time.sleep(0.7)
    print("и бросаетесь на монстра... ")
    time.sleep(0.5)

    if choice_user == "1":
        hero_damage_the_fight = random.randint(int(hero_damage / 2), hero_damage)
        monster1_hp = monster1_hp - hero_damage_the_fight
        print("Ваш урон по монстру", hero_damage_the_fight)
        time.sleep(0.4)
        print("У монстра осталось ", monster1_hp, "здоровья")

    time.sleep(0.7)
    print("монстр издает истошный вопль... ")
    time.sleep(0.7)
    print("и и кусает героя... ")
    time.sleep(0.5)

    choice_monster = "1"
    if choice_monster == "1":
        monster_damage_the_fight = random.randint(int(monster1_damage / 2), monster1_damage)
        hero_hp = hero_hp - monster_damage_the_fight
        print("урон монстра", monster_damage_the_fight)
        time.sleep(0.4)
        print("У героя осталось ", hero_hp, "здоровья")