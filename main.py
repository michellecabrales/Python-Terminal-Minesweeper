from board import Board

SIZE = 9
if __name__ == "__main__":
    game = Board(SIZE)
    selection = ()
    while True:
        try:
            row = input("Enter row:")
            col = input("Enter col:")
            row = int(row)
            col = int(col)
            if (row > SIZE or row < 1) or (col > SIZE or col < 1):
                raise ValueError
            break
        except ValueError:
            print("Something went wrong. Please enter a numeric value between 1 and " + str(SIZE) + ":")

    selection = ((row-1), (col-1))
    game.generate_board(SIZE, selection)

    # Game controller
    while True:
        while True:
            try:
                row = input("Enter row:")
                col = input("Enter col:")
                row = int(row)
                col = int(col)
                if (row > SIZE or row < 1) or (col > SIZE or col < 1):
                    raise ValueError
                break
            except ValueError:
                print("Something went wrong. Please enter a numeric value between 1 and " + str(SIZE) + ":")

        game.pick_and_display((row-1, col-1))
