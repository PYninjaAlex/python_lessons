from src import *


def main():
    '''Вызываем все функции из src.'''
    welcome()
    asking()
    game(player=player, monster=monster, test_player=test_player, test_monster=test_monster)
    finish(monster=monster, player=player)


if __name__ == 'main':
    main()
