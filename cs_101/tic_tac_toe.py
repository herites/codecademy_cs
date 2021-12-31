from random import randint


class Player:
    def __init__(self, marker="X", name=input("What is your name? ")) -> None:
        self.name = name
        self.marker = marker

    def get_marker_loc(self, board):
        while True:
            self.row = int(input("In which row do you want to place a marker? "))
            self.column = int(input("In which column do you want to place a marker? "))
            if not board.check_if_valid(self.row, self.column):
                print("Invalid location, try again.")
            else:
                break

    def place_marker(self, board):

        board.update(self.row, self.column, self.marker)
        print(
            f"{self.marker} was placed in row {self.row}, column {self.column} by {self.name}."
        )
        board.show()

    def play_turn(self, board):
        print(f"This is turn {board.turn}, {self.name} acts.")
        board.turn += 1
        self.get_marker_loc(board)
        self.place_marker(board)
        board.check_win(self.marker)
        if board.won == True:
            print(f"{self.name} wins!")


class Computer(Player):
    def __init__(self, name="Computer", marker="O") -> None:
        super().__init__()
        self.name = name
        self.marker = marker

    def get_marker_loc(self, board):
        while True:
            self.row = randint(1, 3)
            self.column = randint(1, 3)
            if board.check_if_valid(self.row, self.column):
                break


class Board:
    turn = 1
    won = False

    def __init__(self) -> None:
        self.play_area = [[" " for col in range(0, 3)] for row in range(0, 3)]

    def show(board):
        for i in board.play_area:
            print(i, sep="\n")

    def update(self, row, column, marker):
        self.play_area[row - 1][column - 1] = marker

    def check_if_valid(self, row, column):
        return True if self.play_area[row - 1][column - 1] == " " else False

    def check_win(self, marker):
        self.row_win(marker)
        self.column_win(marker)
        self.left_to_right_diagonal_win(marker)
        self.right_to_left_diagonal_win(marker)

    def row_win(self, marker):
        for row in self.play_area:
            if row.count(marker) == 3:
                self.won = True

    def column_win(self, marker):
        cols = []
        col_index = 0
        for row in self.play_area:
            cols.append([row[col_index] for row in self.play_area])
            if col_index < len(row):
                col_index += 1
        for i in cols:
            if i.count(marker) == 3:
                self.won = True

    def left_to_right_diagonal_win(self, marker):
        diagonal = [row[index] for index, row in enumerate(self.play_area)]
        if diagonal.count(marker) == 3:
            self.won = True

    def right_to_left_diagonal_win(self, marker):
        col_index = len(self.play_area[-1]) - 1
        diagonal = []
        for row in self.play_area:
            diagonal.append(row[col_index])
            if col_index > 0:
                col_index -= 1
        if diagonal.count(marker) == 3:
            self.won = True


def main():
    board, player1, computer = game_setup()
    while board.turn <= 9:
        player1.play_turn(board)
        if board.won == True:
            break
        computer.play_turn(board)
        if board.won == True:
            break
        if board.turn == 9:
            print("Board is full, nobody wins.")


def game_setup():
    board = Board()
    player1 = Player()
    computer = Computer()
    print(
        f"""
Welcome to Tic-Tac-Toe {player1.name}!
You will play against a very stupid computer, try not to lose!
Error checking is currently not implemented for user input, do not go out of bounds.
Valid marker positions are integers between 1 and 3.
You will be {player1.marker} and you will go first.
This is the board you will be playing on:"""
    )
    board.show()
    return board, player1, computer


if __name__ == "__main__":
    main()
