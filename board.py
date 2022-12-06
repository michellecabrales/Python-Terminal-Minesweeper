import random


class Board:
    def __init__(self, size):
        self.chosen_cells = []
        self.board = []
        self.bombs = []
        self.open = []
        self.size = size
        # make blank board
        self.board = [[0 for col in range(size)] for row in range(size)]

        ruler = [x + 1 for x in range(size)]
        print("   ", end="")
        print(" ".join(str(x) for x in ruler))
        print("  ------------------")
        for index, row in enumerate(self.board):
            print(str(index+1) + "|", end=" ")
            print(" ".join('☐️' for cell in row))


    def generate_board(self, size, initial_selection):
        """
        Generates the content of the board
        args:
        :return:
        """
        self.open.append(initial_selection)
        # place bombs on board
        for x in range(10):
            while True:
                row = random.randrange(0, size)
                col = random.randrange(0, size)
                # Only add bomb if it has not been already added and it is not the initial selection of the user
                if ((row, col) not in self.bombs) and ((row, col) != initial_selection):
                    self.board[row][col] = "x"
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

        for indexRow, row in enumerate(self.board):
            for indexCol, col in enumerate(row):
                if self.board[indexRow][indexCol] == 0:
                    self.board[indexRow][indexCol] = " "

        self.pick_and_display(initial_selection)

    def pick_and_display(self, selection):

        ruler = [x + 1 for x in range(self.size)]
        ruler_str = " ".join(str(x) for x in ruler)

        # game over scenario
        if self.board[selection[0]][selection[1]] == "x":
            print("GAME OVER")
            print("   ", end="")
            print(ruler_str)
            for ir, row in enumerate(self.board):
                print(str(ir + 1) + "|", end=" ")
                print(" ".join(str(cell) for cell in row))
            exit(0)
        if (selection[0], selection[1]) not in self.open:
            self.open.append((selection[0], selection[1]))

        queue = [selection]
        visited = []
        while len(queue) > 0:
            item = queue[0]

            if item not in visited:
                # go down
                if item[0] < self.size - 1:
                    if self.board[item[0]+1][item[1]] != "x":
                        if ((item[0]+1), item[1]) not in self.open:
                            self.open.append(((item[0]+1), item[1]))
                        if self.board[item[0]+1][item[1]] != " ":
                            visited.append(((item[0]+1), item[1]))
                        else:
                            queue.append(((item[0] + 1), item[1]))
                # go up
                if item[0] > 0:
                    if self.board[item[0]-1][item[1]] != "x":
                        if ((item[0]-1), item[1]) not in self.open:
                            self.open.append(((item[0]-1), item[1]))
                        if self.board[item[0]-1][item[1]] != " ":
                            visited.append(((item[0]-1), item[1]))
                        else:
                            queue.append(((item[0]-1), item[1]))
                if item[1] < self.size - 1:
                    if self.board[item[0]][item[1]+1] != "x":
                        if (item[0], (item[1]+1)) not in self.open:
                            self.open.append((item[0], (item[1]+1)))
                        if self.board[item[0]][item[1] + 1] != " ":
                            visited.append((item[0], (item[1] + 1)))
                        else:
                            queue.append((item[0], (item[1] + 1)))
                if item[1] > 0:
                    if self.board[item[0]][item[1]-1] != "x":
                        if (item[0], (item[1]-1)) not in self.open:
                            self.open.append((item[0], (item[1]-1)))
                        if self.board[item[0]][item[1] - 1] != " ":
                            visited.append((item[0], (item[1] - 1)))
                        else:
                            queue.append((item[0], (item[1] - 1)))
            visited.append(item)
            queue.pop(0)

        print("   ", end="")
        print(ruler_str)
        print("  ------------------")

        for ir, r in enumerate(self.board):
            print(str(ir + 1) + "|", end=" ")
            row_display = ['☐' for cell in r]
            for ic, c in enumerate(r):
                if (ir, ic) in self.open:
                    row_display[ic] = str(c)
            print(" ".join(row_display))

        winning = (self.size * self.size) - 10
        if len(self.open) == winning:
            print("YOU WIN :)")
            exit(0)