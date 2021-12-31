from random import randint


class Player:
    def __init__(self, marker="X", name=input("What is your name? ")) -> None:
        self.name = name
        self.marker = marker

    def place_marker(self, board):
        row = int(input("In which row do you want to place a marker? "))
        column = int(input("In which column do you want to place a marker? "))
        board.update(row, column, self.marker)
        print(f"{self.marker} was placed in row {row}, column {column} by {self.name}")
        board.show()


class Computer(Player):
    def __init__(self, name="Computer", marker="O") -> None:
        super().__init__(name)
        self.name = name
        self.marker = marker

    def place_marker(self, board):
        row = randint(1, 3)
        column = randint(1, 3)
        board.update(row, column, self.marker)
        print(f"{self.marker} was placed in row {row}, column {column} by {self.name}")
        board.show()


class Board:
    def __init__(self) -> None:
        self.play_area = [[" " for col in range(0, 3)] for row in range(0, 3)]

    def show(board):
        for i in board.play_area:
            print(i, sep="\n")

    def update(self, row, column, marker):
        row_index = row - 1
        column_index = column - 1
        self.play_area[row_index][column_index] = marker


def main():
    win = False
    board, player1, computer = game_setup()
    player1.place_marker(board)
    computer.place_marker(board)


def game_setup():
    board = Board()
    player1 = Player()
    computer = Computer()
    print(f"Hello {player1.name}! You will be {player1.marker} and you will go first.")
    print("This is the board you will be playing on:")
    board.show()
    return board, player1, computer


if __name__ == "__main__":
    main()
