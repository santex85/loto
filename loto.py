import random


class Player:
    card: list = None

    def __init__(self, player: bool = False, cpu: bool = False):
        self.player: bool = player
        self.cpu: bool = cpu


class Bag:
    def __init__(self):
        self.kegs: list = list(range(1, 91))


class Card:

    def __init__(self):
        self.__row: int = 3
        self.__col: int = 9
        self.card: list = []

    def __str__(self):
        return str(self.card)

    def get_card(self):

        # генерирует матрицу для карточки
        for i in range(self.__row):
            self.card.append([0] * self.__col)

        numbers = list(range(1, 91))  # номера для карточки
        for i in range(self.__row):
            for j in range(self.__col):
                number = random.choice(numbers)  # выбираем номера в карточку
                self.card[i][j] = number  # вставляем номера в карточку
                numbers.remove(number)  # удаляем номера из списка

        # отсортировать строку в карточке
        for i in self.card:
            while len(set(i)) > 6:
                i[random.randint(0, 8)] = ' '

        return self.card

    @staticmethod
    def print_card(card: list):
        print('----------------------')
        for row in card:  # делаем перебор всех строк матрицы A
            for elem in row:  # перебираем все элементы в строке
                print(elem, end=' ')
            print()
        print('----------------------')

    @staticmethod
    def check_card(card: list):
        c = 0
        for row in card:
            for i in row:
                if '-' == i:
                    c += 1
                    continue
        if c == 15:
            return True


class Game:
    def __init__(self, kind_game: int):
        self.kind_game: int = kind_game

    @staticmethod
    def __cpu_vs_player(card: list):

        human = Player(player=True)
        cpu = Player(cpu=True)

        human.card = Card().get_card()
        cpu.card = Card().get_card()

        kegs = Bag().kegs

        while kegs:
            keg = random.choice(kegs)
            kegs.remove(keg)
            print(f'Новый бочонок: {keg} (осталось {len(kegs)})')
            print(f'Ваша карточка:')
            card.print_card(human.card)
            print(f'Карточка компьютера:')
            card.print_card(cpu.card)
            answer = input('Зачеркнуть цифру? (y/n):>')

            if answer.lower() == 'y':
                line = 3  # линии карточки для проверки
                for i in human.card:
                    if keg in i:
                        i[i.index(keg)] = '-'
                    else:
                        line -= 1
                    if not line:
                        exit('Вы проиграли')

            if answer.lower() == 'n':
                for i in human.card:
                    if keg in i:
                        exit('Вы проиграли!')

            for i in cpu.card:
                if keg in i:
                    i[i.index(keg)] = '-'

            if card.check_card(human.card):
                exit('Вы победили!')
            if card.check_card(cpu.card):
                exit('Компьютер победил!')

    @staticmethod
    def __player_vs_player(card: list):
        kegs = Bag().kegs
        human1 = Player(player=True)
        human2 = Player(player=True)

        human1.card = Card().get_card()
        human2.card = Card().get_card()

        while kegs:
            keg = random.choice(kegs)
            kegs.remove(keg)
            print(f'Новый бочонок: {keg} (осталось {len(kegs)})')
            print(f'Карточка игрока1:')
            card.print_card(human1.card)

            answer1 = input('Игрок1 зачеркнуть цифру? (y/n):>')

            if answer1.lower() == 'y':
                line = 3
                for i in human1.card:
                    if keg in i:
                        i[i.index(keg)] = '-'
                    else:
                        line -= 1
                    if not line:
                        exit('Проиграл игрок1')

            if answer1.lower() == 'n':
                for i in human1.card:
                    if keg in i:
                        exit('Проиграл игрок1')

            print(f'Карточка игрока2:')
            card.print_card(human2.card)
            answer2 = input('Игрок2 зачеркнуть цифру? (y/n):>')

            if answer2.lower() == 'y':
                line = 3
                for i in human2.card:
                    if keg in i:
                        i[i.index(keg)] = '-'
                    else:
                        line -= 1
                    if not line:
                        exit('Проиграл игрок2')
            if answer2.lower() == 'n':
                for i in human2.card:
                    if keg in i:
                        exit('Проиграл игрок2')

            if card.check_card(human1.card):
                exit('Вы победили!')
            if card.check_card(human2.card):
                exit('Компьютер победил!')

    @staticmethod
    def __cpu_vs_cpu(card: list):
        cpu1 = Player(cpu=True)
        cpu2 = Player(cpu=True)

        cpu1.card = Card().get_card()
        cpu2.card = Card().get_card()

        kegs = Bag().kegs

        while kegs:
            keg = random.choice(kegs)
            kegs.remove(keg)
            print(f'Новый бочонок: {keg} (осталось {len(kegs)})')
            print(f'Карточка cpu1:')
            card.print_card(cpu1.card)
            print(f'Карточка cpu2:')
            card.print_card(cpu2.card)

            for i in cpu1.card:
                if keg in i:
                    i[i.index(keg)] = '-'

            for i in cpu2.card:
                if keg in i:
                    i[i.index(keg)] = '-'

            if card.check_card(cpu1.card):
                exit('Cpu1 победил!')
            if card.check_card(cpu2.card):
                exit('Cpu2 победил!')

    def start(self):
        card = Card()
        kegs = Bag().kegs

        if self.kind_game == 1:
            self.__cpu_vs_player(card)

        if self.kind_game == 2:
            self.__player_vs_player(card)

        if self.kind_game == 3:
            self.__cpu_vs_cpu(card)


if '__main__' == __name__:
    players = int(input("""Выберете кто будет играть:
     1. Пользователь-Компьютер
     2. Пользователь-Пользователь
     3. Компьютер-Компьютер
     >: """))
    if players == 1:
        print('Игра "Человек-Компьютер". Начинаем!')
        print()
        game = Game(players)
        game.start()
    elif players == 2:
        print('Игра "Человек-Человек". Начинаем!')
        game = Game(players)
        game.start()
    elif players == 3:
        print('Игра "Компьютер-Компьютер". Начинаем!')
        game = Game(players)
        game.start()
