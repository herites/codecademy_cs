from random import randint


class Player:
    def __init__(self, marker="X", name=input("What is your name? ")) -> None:
        self.name = name
        self.marker = marker

    def place_marker(self):
        row = int(input("In which row do you want to place a marker? "))
        column = int(input("In which column do you want to place a marker? "))
        return [row, column, self.marker]


class Computer(Player):
    def __init__(self, name="Computer", marker="O") -> None:
        super().__init__(name)
        self.name = name
        self.marker = marker


class Board:
    def __init__(self) -> None:
        self.play_area = [[" " for col in range(0, 3)] for row in range(0, 3)]

    def show(board):
        for i in board.play_area:
            print(i, sep="\n")

    def update(self, marker):
        row = marker[0] - 1
        column = marker[1] - 1
        marker_type = marker[2]
        self.play_area[row][column] = marker_type
        print(f"{marker_type} was placed in row {marker[0]}, column {marker[1]}")


def main():
    win = False
    board, player1, computer = game_setup()
    board.update(player1.place_marker())
    board.show()


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
