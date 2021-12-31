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
            f"{self.marker} was placed in row {self.row}, column {self.column} by {self.name}"
        )
        board.show()

    def play_turn(self, board):
        self.get_marker_loc(board)
        self.place_marker(board)


class Computer(Player):
    def __init__(self, name="Computer", marker="O") -> None:
        super().__init__(name)
        self.name = name
        self.marker = marker

    def get_marker_loc(self, board):
        while True:
            self.row = randint(1, 3)
            self.column = randint(1, 3)
            if board.check_if_valid(self.row, self.column):
                break


class Board:
    def __init__(self) -> None:
        self.play_area = [[" " for col in range(0, 3)] for row in range(0, 3)]

    def show(board):
        for i in board.play_area:
            print(i, sep="\n")

    def update(self, row, column, marker):
        self.play_area[row - 1][column - 1] = marker

    def check_if_valid(self, row, column):
        return True if self.play_area[row - 1][column - 1] == " " else False


def main():
    win = False
    board, player1, computer = game_setup()
    player1.play_turn(board)
    computer.play_turn(board)


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
