class Person:
    def __init__(self, height, hair_color, age, name):
        self.height = height
        self.hair_color = hair_color
        self.age = age
        self.name = name

    def __str__(self):
        return f'{man.height}, {man.hair_color}, {man.age}, {man.name}'

    def speaking_man(self, words: str):
        print(words)

    def laughing_man(self):
        print('ha-ha-ha')

man = Person(182,'white', '16', 'Vova')

man.speaking_man(f'{man.name}:Hi! How are you?')
print(str(man))
man.laughing_man()


class Animal:
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner

    def speak(self):
        print('Argh!')

    def introduce_yourself(self):
        print('My name is', self.name, 'and I am a pet.')


class Cat(Animal):
    def __init__(self, color, name, age, breed):
        self.color = color

    def up_pow(self):
        print(' Кот поднял лапу ')

    def slepy_cat(self,sleepy_or_playing: str):
        if sleepy_or_playing == 'sleepy':
            print('sleepy cat')
        else:
            print('playing')


class Dog(Animal):
    pass


dog_1 = Dog('Rex', 3, 'овчарка', man)
dog_1.owner
