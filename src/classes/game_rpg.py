class Character:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Player(Character):
    # def __init__(self, name, x, y):
    #     """
    #     Класс, представляющий игрока.
    #
    #     Args:
    #         name (str): Имя игрока.
    #         x (int): Координата X игрока на карте.
    #         y (int): Координата Y игрока на карте.
    #     """
    pass


class Enemy(Character):
    # def __init__(self, name, x, y):
    #     """
    #     Класс, представляющий врага.
    #
    #     Args:
    #         name (str): Имя врага.
    #         x (int): Координата X врага на карте.
    #         y (int): Координата Y врага на карте.
    #     """
    pass


class Map:
    def __init__(self, width, height):
        """
        Класс, представляющий карту.

        Args:
            width (int): Ширина карты.
            height (int): Высота карты.
        """
        self.width = width
        self.height = height

        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        # Генерируем двумерный список, представляющий тайлы на карте


class Game:
    def __init__(self):
        self.player = Player("Player", 0, 0)
        self.enemy = Enemy("Ork", 1, 1)
        self.game_map = Map(5, 5)
        self.hp = 100

    def start_battle(self):
        """
        Функция, вызываемая при начале битвы.
        """
        print("Началась битва! Вы встретили врага!")

    def display_map(self):
        """
        Функция для отображения карты с игроком и врагом.

        Args:
            enemy (Enemy): Объект врага.
            player (Player): Объект игрока.
            game_map (Map): Объект карты.
        """
        is_battle = False  # Флаг для определения, началась ли битва
        for y in range(self.game_map.height):
            for x in range(self.game_map.width):
                if self.player.x == self.enemy.x and self.player.y == self.enemy.y and self.player.x == x and self.player.y == y:
                    print("@", end=" ")  # Отображение игрока и врага на одной позиции
                    is_battle = True
                elif self.player.x == x and self.player.y == y:
                    print("P", end=" ")  # Отображение игрока
                elif self.enemy.x == x and self.enemy.y == y:
                    print("E", end=" ")  # Отображение врага
                elif self.game_map.tiles[y][x] is None:
                    print("-", end=" ")  # Отображение пустого тайла
                else:
                    print("X", end=" ")  # Отображение других объектов на карте
            print()
        if is_battle:
            self.start_battle()

    def move_player(self, player, dx, dy):
        """
        Функция для перемещения игрока на карте.

        Args:
            player (Player): Объект игрока.
            dx (int): Смещение по оси X.
            dy (int): Смещение по оси Y.
        """
        player.x += dx
        player.y += dy

    def can_move(self, player, dx, dy):
        """
        Функция для проверки возможности перемещения игрока на карте.

        Args:
            player (Player): Объект игрока.
            game_map (Map): Объект карты.
            dx (int): Смещение по оси X.
            dy (int): Смещение по оси Y.

        Returns:
            bool: True, если игрок может переместиться, иначе False.
        """
        new_x = player.x + dx
        new_y = player.y + dy
        if new_x < 0 or new_x >= self.game_map.width or new_y < 0 or new_y >= self.game_map.height:
            return False  # Проверка выхода за пределы карты
        if self.game_map.tiles[new_y][new_x] is not None:
            return False  # Проверка наличия препятствия на новой позиции
        return True

    def start_game(self):

        while True:
            self.display_map()

            action = input("Введите действие (w - вверх, a - влево, s - вниз, d - вправо): ")
            if action == "w" and self.can_move(self.player, 0, -1):
                self.move_player(self.player, 0, -1)
            elif action == "a" and self.can_move(self.player, -1, 0):
                self.move_player(self.player, -1, 0)
            elif action == "s" and self.can_move(self.player, 0, 1):
                self.move_player(self.player, 0, 1)
            elif action == "d" and self.can_move(self.player, 1, 0):
                self.move_player(self.player, 1, 0)
            else:
                print("Недопустимое действие.")

            print()


if __name__ == "__main__":
    game = Game()
    game.start_game()
