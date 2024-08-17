import random


class Card:
    sym_lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suit_lst = ['♠', '♣', '♦', '♥']

    def __init__(self, sym, suit):
        self.sym = sym
        self.card_name = str(sym) + suit
        if isinstance(sym, str):
            if sym == 'A':
                self.score = 11
            else:
                self.score = 10
        else:
            self.score = sym


class Players:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def take_card(self, deck):
        new_card = random.choice(deck)
        self.hand.append(new_card)
        # self.score += new_card.score
        deck.remove(new_card)
        if len(self.hand) < 2:
            self.take_card(deck)

    def show_hand(self):
        print(f'\n{self.name}: ', end=' ')
        for i in self.hand:
            print(i.card_name, end=' ')

    def score_count(self):
        score = 0
        A_cnt = 0
        for i in self.hand:
            if i.sym == 'A':
                A_cnt += 1
                continue
            score += i.score
        for _ in range(A_cnt):
            score += 11
            if score > 21:
                score -= 10
        self.score = score
        return score


class Table:
    deck = [Card(sym, suit) for sym in Card.sym_lst for suit in Card.suit_lst]
    croupier = Players("Крупье")
    player = Players('Костя')

    def game(self, player):
        while True:
            player.take_card(Table.deck)
            player.show_hand()
            score = player.score_count()
            print(f'Очки: {score}')
            if score == 21:
                print(f"У {player.name} Black Jack!")
                break
            elif score > 21:
                print(f'У {player.name} Перебор..')
                break
            answer = input("Будете брать еще катру? (y/n) ")
            if answer == 'n':
                break

    def croupier_play(self):
        score = 0
        while score < 17:
            Table.croupier.take_card(Table.deck)
            score = Table.croupier.score_count()
        self.croupier.show_hand()

    def score_check(self, player, croupier=croupier):
        print('\nРезультат:', end=' ')
        print(f'{player.name}: {player.score}. {croupier.name}: {croupier.score}')
        if player.score == croupier.score or (player.score > 21 and croupier.score > 21):
            print('Ничья!')
        elif ((player.score > croupier.score) and player.score <= 21) or (player.score <= 21 and croupier.score >21):
            print(f'{player.name} выиграл!')
        else:
            print(f'{player.name} проиграл!')



game = Table()
game.game(Table.player)
game.croupier_play()
game.score_check(Table.player)


