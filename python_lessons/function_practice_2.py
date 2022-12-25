import string
def square_num(num):
    num_last = num ** 2
    return num_last

# a = square_num(-12)
# print(a)


def summa(*num):
    res = 0
    for i in num:
        res += i
    return res

a = summa(100,100)
# print(a)

def test_dnk(dnk: str) -> str:
    for s in dnk:
        if s not in 'ATCG':
            return False
    else:
        return True

a = test_dnk('TTCGATGCUTUU')
# print(a)


def dnk_kw(dnk):
    nukl_dnk = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for nukl in dnk:
        if nukl == 'A':
            nukl_dnk['A'] += 1
        elif nukl == 'T':
            nukl_dnk['T'] += 1
        elif nukl == 'C':
            nukl_dnk['C'] += 1
        elif nukl == 'G':
            nukl_dnk['G'] += 1
    return nukl_dnk

a = dnk_kw('AATTCGG')
# print(a)



def count_of_symbols(s):
    last_dict = {}
    for c in s:
        last_dict[c] = last_dict.get(c, 0) + 1
    return last_dict

a = count_of_symbols('Mad Hatter')
# print(a)



def count_of_words(text):
    dict_of_w = {}
    text = text.translate(text.maketrans('', '', string.punctuation))
    for word in text.split():
        dict_of_w[word] = dict_of_w.get(word, 0) + 1
    return dict_of_w

a = count_of_words('bla-  -bla,  bla, - rar ,rar')
# print(a)

alice = "«Would you tell me, please, which way I ought to go from here?»" \
        " «That depends a good deal on where you want to get to,» said the Cat. «I don't much care where,» " \
        "said Alice. «Then it doesn't matter which way you go,» said the Cat. «-so long as I get somewhere,»" \
        " Alice added as an explanation. «Oh, you're sure to do that,» said the Cat, «if you only walk long " \
        "enough.»"


name = 'Alice'
age = 12
hobies = ['reading','writing']
# print(type(age))

class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = super().__str__()

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


murzik = Cat('orange', 'Murzik', 4, 'Британский вислоухий')
print(murzik.color)
murzik.speak()
murzik.introduce_yourself()
murzik.up_pow()
murzik.slepy_cat('playing')

print(murzik.name)

dog_1 = Dog('Шарик', 2, 'Корги')
dog_2  = Dog('Пупсик', 2, 'Белонка')
dog_3 = Dog('Рекс', 2, 'Овчарка')
dog_1.speak()
dog_2.introduce_yourself()