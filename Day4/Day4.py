import numpy as np

class Board:

    def __init__(self):
        self.board = np.zeros((5,5), dtype = int)
        self.marked = np.zeros((5,5))
    
    def createBoard(self, lines):
        for i in range(0, 5):
            boardLine = [int(number) for number in lines[i].split(' ') if number != '']
            self.board[i] = boardLine
    
    def markNumber(self, number):
        if number in self.board:
            indices = np.where(self.board == number)
            self.marked[indices[0], indices[1]] = 1
    
    def checkWin(self):
        return self.marked.all(axis = 0).any() or self.marked.all(axis = 1).any()

    def calculateScore(self, number):
        return (self.board * (self.marked == 0)).sum() * number


def findWinningBoard(numbers, boards):
    for number in numbers:
        for i in range(len(boards)):
            boards[i].markNumber(number)
            if boards[i].checkWin():
                print(f"Board {i + 1} won!")
                print("Marked positions:")
                print(boards[i].marked)
                return i, number

def findLastWinningBoard(numbers, boards):
    winningBoards = []
    winningNumber = 0
    for number in numbers:
        for i in range(len(boards)):
            if i not in winningBoards:
                boards[i].markNumber(number)
                if boards[i].checkWin():
                    winningBoards.append(i)
                    print(f"Board {i + 1} won")
                    winningNumber = number
    return winningBoards[-1], winningNumber
                    


with open('Day4/day4Inputs.txt', 'r') as f:
    dayFourInputs = [line.strip() for line in f.readlines()]
print(dayFourInputs)

numbersCalled = [int(number) for number in dayFourInputs[0].split(",")]
print(numbersCalled)

numberOfBoards = (len(dayFourInputs) - 1) // 6
print(numberOfBoards)

boards = dict()
for i in range(0, numberOfBoards):
    boards[i] = Board()
    boards[i].createBoard(dayFourInputs[(2 + i * 6):(2 + 5 + (i + 1) * 6)])
    print(f"Board {i + 1}")
    print(boards[i].board)
    print()


winningIndex, winningNumber = findWinningBoard(numbersCalled, boards)
lastWinningBoard, lastWinningNumber = findLastWinningBoard(numbersCalled, boards)
print(f"Last winning board is {lastWinningBoard + 1}")
print(f"First winning Number is {winningNumber}")
print(f"Last winning Number is {lastWinningNumber}")
print("Score of first winning board =", boards[winningIndex].calculateScore(winningNumber))
print("Score of last winning board =", boards[lastWinningBoard].calculateScore(lastWinningNumber))