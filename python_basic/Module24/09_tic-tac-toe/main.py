class Cell:

    def __init__(self, number, occupation):
        self.number = number
        self.occupation = occupation


class Board:
    board = [Cell(i, i) for i in range(1, 10)]

    def game(self, pl1, pl2):
        while True:
            if pl2.winner_check():
                break
            pl1.cell_occupation()
            if pl1.winner_check():
                break
            pl2.cell_occupation()


class Player:
    def __init__(self, name, sym):
        self.name = name
        self.sym = sym

    def cell_occupation(self):
        num = int(input(f'Ход: {self.name}. Введите номер клетки: '))
        for cell in Board.board:
            if cell.occupation == num:
                cell.occupation = self.sym
                break
        else:
            print('Такой клетки нет или она занята')
            self.cell_occupation()

    def winner_check(self):
        line1 = [cell.occupation for cell in Board.board[0:3]]
        line2 = [cell.occupation for cell in Board.board[3:6]]
        line3 = [cell.occupation for cell in Board.board[6:9]]
        coln1 = [cell.occupation for cell in Board.board[::3]]
        coln2 = [cell.occupation for cell in Board.board[1::3]]
        coln3 = [cell.occupation for cell in Board.board[2::3]]
        diag1 = [cell.occupation for cell in Board.board[::4]]
        diag2 = [cell.occupation for cell in Board.board[2::2]]
        print(f'\n[{line1[0]}][{line1[1]}][{line1[2]}]')
        print(f'[{line2[0]}][{line2[1]}][{line2[2]}]')
        print(f'[{line3[0]}][{line3[1]}][{line3[2]}]')
        if line1.count(self.sym) == 3\
                or line2.count(self.sym) == 3 \
                or line3.count(self.sym) == 3 \
                or coln1.count(self.sym) == 3 \
                or coln2.count(self.sym) == 3 \
                or coln3.count(self.sym) == 3 \
                or diag1.count(self.sym) == 3 \
                or diag2.count(self.sym) == 3:
            print(f'\nВ этой нелегкой схватке победил: {self.name}!')
            return True


print('Клетки обознаяенные цифрами - не заняты')
pl1 = Player('Лелик', 'x')
pl2 = Player('Болик', 'o')
board = Board()
board.game(pl1, pl2)