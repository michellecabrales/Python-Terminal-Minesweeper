import random


class Board:
    def __init__(self, num):
        self.chosen_cells = []
        self.board = []
        self.bombs = []

        # make blank board
        self.board = [[0 for col in range(num)] for row in range(num)]
        for row in self.board:
            print(" ".join('❇️' for cell in row))

    def generate_board(self):
        """
        Generates the content of the board
        args:

        :return:
        """
        # place bombs on board
        for x in range(10):
            while True:
                row = random.randrange(0, num)
                col = random.randrange(0, num)
                self.board[row][col] = "x"
                if not (row, col) in self.bombs:
                    self.bombs.append((row, col))
                    break

        # add numbers to the cells
        for indexRow, row in enumerate(self.board):
            for indexNum, num in enumerate(row):
                if not (indexRow, indexNum) in self.bombs:
                    # flag if bomb is to the right cell
                    if indexNum != (len(row) - 1):
                        if self.board[indexRow][indexNum + 1] == "x":
                            self.board[indexRow][indexNum] += 1
                    # flag if bomb is the left of cell
                    if indexNum != 0:
                        if self.board[indexRow][indexNum - 1] == "x":
                            self.board[indexRow][indexNum] += 1
                    # flag if bomb is on top of cell
                    if indexRow != 0:
                        if self.board[indexRow - 1][indexNum] == "x":
                            self.board[indexRow][indexNum] += 1
                    # flag cell if bomb is below it
                    if indexRow != (len(self.board) - 1):
                        if self.board[indexRow + 1][indexNum] == "x":
                            self.board[indexRow][indexNum] += 1

                    # flag cell if bomb is in upper left corner
                    if indexRow != 0 and indexNum != 0:
                        if self.board[indexRow - 1][indexNum - 1] == "x":
                            self.board[indexRow][indexNum] += 1

                    # flag cell if bomb is upper right
                    if indexRow != 0 and indexNum != (len(row) - 1):
                        if self.board[indexRow-1][indexNum+1] == "x":
                            self.board[indexRow][indexNum] += 1

                    # flag cell if bomb is in lower left corner
                    if indexRow != (len(self.board)-1) and indexNum != 0:
                        if self.board[indexRow + 1][indexNum - 1] == "x":
                            self.board[indexRow][indexNum] += 1

                    # flag if cell has bomb to lower right
                    if indexRow != (len(self.board)-1) and indexNum != (len(row)- 1):
                        if self.board[indexRow + 1][indexNum + 1] == "x":
                            self.board[indexRow][indexNum] += 1

    def pick_and_display(self):
        for row in self.board:
            print(" ".join('❇️' for cell in row))
            # print(" ".join(str(cell) for cell in row))
