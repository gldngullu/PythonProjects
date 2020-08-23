from random import randint
import numpy as np
#
# print(3+number)


class SameGame(object):
    w, h = 20, 10
    letters = 'A', 'B', 'C', 'D', 'E', 'F'
    totalScore = 0
    count = 0
    numberOfLetters = 0
    gameMatrix = [['A', 'A'],[ 'A', 'A']]

    def createGameMatrix(self):
        tempGameMatrix  = [[[self.letters[randint(0, self.numberOfLetters-1)]] for x in range(self.w)] for y in range(self.h)]
        return tempGameMatrix

    def printGameMatrix(self):
        for i in range(len(self.gameMatrix)):
            print(str(i), end="\t")
            for j in range(len(self.gameMatrix[i])):
                s = ",".join(self.gameMatrix[i][j]).replace(",", " ")
                print(s, end="\t")
            print()

    def hasEmptyColumn(self):
        emptyColumnIndex = -1
        for i in range(0, self.w, 1):
            if self.gameMatrix[self.h - 1][i] == " ":
                emptyColumnIndex = i
        if emptyColumnIndex != -1:
            for i in range(emptyColumnIndex, self.w-2, 1):
                for j in range(0, self.h, 1):
                    self.gameMatrix[i][j] = self.gameMatrix[i+1][j]
            for k in range(0, self.h-1, 1):
                self.gameMatrix[k][self.w-1] = " "


    def gameStep(self, rowPosition, columnPosition):

        letterChosen = self.gameMatrix[rowPosition][columnPosition]

        for i in range(rowPosition, 0, -1):
            self.gameMatrix[i][columnPosition] = self.gameMatrix[i-1][columnPosition]
            self.gameMatrix[i - 1][columnPosition] = ' '

        if self.gameMatrix[rowPosition][columnPosition] == letterChosen:
            self.count += 1
            self.gameStep(rowPosition, columnPosition)

        if columnPosition + 1 < self.w:
            if self.gameMatrix[rowPosition][columnPosition+1] == letterChosen:
                self.count += 1
                self.gameStep(rowPosition, columnPosition + 1)

        if columnPosition - 1 >= 0:
            if self.gameMatrix[rowPosition][columnPosition - 1] == letterChosen:
                self.count += 1
                self.gameStep(rowPosition, columnPosition - 1)

        if rowPosition+1 < self.h:
            if self.gameMatrix[rowPosition + 1][columnPosition] == letterChosen:
                self.count += 1
                self.gameStep(rowPosition + 1, columnPosition)

    def hasNeighbour(self, rowPosition, columnPosition):
        if rowPosition < self.h-1:
            if self.gameMatrix[rowPosition][columnPosition] == self.gameMatrix[rowPosition + 1][columnPosition]:
                return True
        if rowPosition > 0:
            if self.gameMatrix[rowPosition][columnPosition] == self.gameMatrix[rowPosition -1][columnPosition]:
                return True
        if columnPosition < self.w-1:
            if self.gameMatrix[rowPosition][columnPosition] == self.gameMatrix[rowPosition][columnPosition + 1]:
                return True
        if columnPosition > 0:
            if self.gameMatrix[rowPosition][columnPosition] == self.gameMatrix[rowPosition][columnPosition - 1]:
                return True
        return False

    def isGameEnded(self):
        for i in range(0, self.h-1, 1):
            for j in range(0, self.w, 1):
                if self.gameMatrix[i][j] != " ":
                    if self.gameMatrix[i][j] == self.gameMatrix[i+1][j]:
                        return False
                    if j != self.w-1:
                        if self.gameMatrix[i][j] == self.gameMatrix[i][j+1]:
                            return False
        return True

    def countRemainingTiles(self):
        numOfRemainingTiles = 0
        flag  = True
        for i in range(0, self.w, 1):
            if self.gameMatrix[self.h-1][i] != " ":
                flag = False
        if flag:
            return 0
        for i in range(0, self.h, 1):
            for j in range(0, self.w, 1):
                if self.gameMatrix[i][j] != " ":
                    numOfRemainingTiles += 1
        return numOfRemainingTiles

    def getUserChoice(self):
        isTheEnd = self.isGameEnded()
        if isTheEnd:
            return
        print("Enter -1 for both values to exit the game.")
        print("Your current score is ", self.totalScore);
        positionAtColumns = eval(input("Enter the position in columns: "))
        positionAtRows = eval(input("Enter the position in rows: "))
        if positionAtColumns == -1 and positionAtRows == -1:
            self.endGame()
            exit()
        if self.hasNeighbour(positionAtRows, positionAtColumns):
            self.count += 1
            self.gameStep(positionAtRows, positionAtColumns)
        self.hasEmptyColumn()
        self.printGameMatrix()
        if self.count is not 0:
            self.totalScore += (self.count-2)**2
        self.count = 0
        self.getUserChoice()

    def startGame(self):
        self.numberOfLetters = eval(input("Enter the number of letters to be used(Between 3 and 6): "))
        self.gameMatrix = self.createGameMatrix()
        self.printGameMatrix()
        self.getUserChoice()
        self.endGame()

    def endGame(self):
        print("The game has ended.")
        remainingTiles = self.countRemainingTiles()
        self.totalScore -= remainingTiles
        if remainingTiles == 0:
            self.totalScore *= 5
        print("Your total score was", self.totalScore, "!")

# ------------------end class


newGame = SameGame()
newGame.startGame()
