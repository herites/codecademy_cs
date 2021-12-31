from random import randint


class Player:
    def __init__(self, marker="X", name=input("What is your name? ")) -> None:
        self.name = name
        self.marker = marker
        pass

    def place_marker(self):
        row = int(input("In which row do you want to place a marker? "))
        column = int(input("In which column do you want to place a marker? "))
        # print(f"You placed a marker in row {row}, column {column}.")
        return [row, column]


class Computer(Player):
    def __init__(self, name="Computer", marker="O") -> None:
        super().__init__(name)
        self.name = name
        self.marker = marker


class Board:
    def __init__(self) -> None:
        self.play_area = [
            [
                " ",
                " ",
                " ",
            ],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def show(board):
        for i in board.play_area:
            print(i, sep="\n")

    def update(self, marker_loc):
        row = marker_loc[0] - 1
        column = marker_loc[1] - 1
        self.play_area[row][column] = "X"


def main():
    win = False
    board, player1, computer = game_setup()
    board.update(player1.place_marker())
    board.show()


def game_setup():
    board = Board()
    player1 = Player()
    computer = Computer()
    print(
        f"Hello {player1.name}! You will playing with {player1.marker} and you go first."
    )
    print("This is the board you will be playing on:")
    board.show()
    return board, player1, computer


if __name__ == "__main__":
    main()
