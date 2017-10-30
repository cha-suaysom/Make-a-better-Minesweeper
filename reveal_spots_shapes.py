import random


class boardSpot(object):
    value = 0
    selected = False
    mine = False
    flag = False 
    option = 1 #1 is normal minesweeper

    def __init__(self):
        self.selected = False
        self.flag = False

    def __str__(self):
        return str(boardSpot.value)

    def isMine(self):
        if boardSpot.value == -1:
            return True
        return False


class boardClass(object):
    def __init__(self, m_boardSize, m_numMines, option = 1):
        self.board = [[boardSpot() for i in range(m_boardSize)] for j in range(m_boardSize)]
        self.boardSize = m_boardSize
        self.numMines = m_numMines
        self.numFlag = 0
        self.selectableSpots = m_boardSize * m_boardSize - m_numMines
        self.option = option
        i = 0
        while i < m_numMines:
            x = random.randint(0, self.boardSize-1)
            y = random.randint(0, self.boardSize-1)
            if not self.board[x][y].mine:
                self.addMine(x, y)
                i += 1
            # else:
            #     i -= 1

    def __str__(self):
        returnString = " "
        divider = "\n---"

        for i in range(0, self.boardSize):
            returnString += " | " + str(i)
            divider += "----"
        divider += "\n"

        returnString += divider
        for y in range(0, self.boardSize):
            returnString += str(y)
            for x in range(0, self.boardSize):
                if self.board[x][y].mine and self.board[x][y].selected:
                    returnString += " |" + str(self.board[x][y].value)
                elif (self.board[x][y].selected and not self.board[x][y].flag):
                    returnString += " | " + str(self.board[x][y].value) #ADD FLAG HERE, case of not revealed, not selected
                elif self.board[x][y].flag:
                    returnString += " | " + "X"
                else:
                    returnString += " |  "
            returnString += " |"
            returnString += divider
        return returnString

    def printReal(self):
        returnString = " "
        divider = "\n---"

        for i in range(0, self.boardSize):
            returnString += " | " + str(i)
            divider += "----"
        divider += "\n"

        returnString += divider
        for y in range(0, self.boardSize):
            returnString += str(y)
            for x in range(0, self.boardSize):
                if (self.board[x][y].value == -1):
                    returnString += " |" + str(self.board[x][y].value)
                else:
                    returnString += " | " + str(self.board[x][y].value)

            returnString += " |"
            returnString += divider
        return returnString

    def addMine(self, x, y):
        self.board[x][y].value = -1
        self.board[x][y].mine = True
        neighborList = self.getNeighbors(x,y,self.option)

        for neighbor in neighborList:
            spot = self.board[neighbor[0]][neighbor[1]]
            if (not spot.mine):
                spot.value += 1

    def makeMove(self, x, y):
        if (self.board[x][y].selected == True):
            print(" ")
            print("Already selected. Please select a new spot")
            print(" ")
        else:
            self.board[x][y].selected = True
            self.selectableSpots -= 1
            if self.board[x][y].value == -1:
                return False

    def makeSafeMove(self,x,y):
        if (self.board[x][y].selected == True):
            # print(" ")
            # print("Already selected. Please select a new spot")
            # print(" ")
            return 0
        else:
            if self.board[x][y].value == -1:
                return 0
            self.board[x][y].selected = True
            self.selectableSpots -= 1
            return 1
            # if self.board[x][y].value == 0:
            #     for i in range(x-1, x+2):
            #         if i >= 0 and i < self.boardSize:
            #             if y-1 >= 0 and not self.board[i][y-1].selected:
            #                 self.makeMove(i, y-1)
            #             if y+1 < self.boardSize and not self.board[i][y+1].selected:
            #                 self.makeMove(i, y+1)
            #     if x-1 >= 0 and not self.board[x-1][y].selected:
            #         self.makeMove(x-1, y)
            #     if x+1 < self.boardSize and not self.board[x+1][y].selected:
            #         self.makeMove(x+1, y)
            #     return True
            # else:
            #     return True


    def getSurInfo(self,x,y):
        p = 0
        q = 0
        r = 0
        j = 1
        q = self.board[x][y].value
        neighborList = self.getNeighbors(x,y,self.option)
        #print(neighborList)
        for neighbor in neighborList:
            spot = self.board[neighbor[0]][neighbor[1]]
            if (spot.flag == True):
                r += 1
            if (spot.selected == True):
                p += 1

        return [p,q,r,x,y]

    def getNeighbors(self,x,y,option = 1):
        if (option == 1):
            j = 1
            listToReturn = []
            for colIndex in range(x-j,x+j+1):
                for rowIndex in range(y-j,y+j+1):
                    if ((0 <= colIndex) and (colIndex < self.boardSize)):
                        if ((0 <= rowIndex) and (rowIndex < self.boardSize)):
                            if ((x,y) != (colIndex,rowIndex)):
                                listToReturn.append([colIndex,rowIndex])
            return listToReturn

        if (option == 2):
            j = 1
            listToReturn = []
            for colIndex in range(x-j,x+j+1):
                for rowIndex in range(y-j,y+j+1):
                    if ((0 <= colIndex) and (colIndex < self.boardSize)):
                        if ((0 <= rowIndex) and (rowIndex < self.boardSize)):
                            if ((x,y) != (colIndex,rowIndex)):
                                if (abs(x-colIndex) + abs(y-rowIndex) <= 1):
                                    listToReturn.append([colIndex,rowIndex])
            return listToReturn

        if (option == 3):
            j = 2
            listToReturn = []
            for colIndex in range(x-j,x+j+1):
                for rowIndex in range(y-j,y+j+1):
                    if ((0 <= colIndex) and (colIndex < self.boardSize)):
                        if ((0 <= rowIndex) and (rowIndex < self.boardSize)):
                            if ((x,y) != (colIndex,rowIndex)):
                                listToReturn.append([colIndex,rowIndex])
            return listToReturn

        if (option == 4):
            j = 2
            listToReturn = []
            for colIndex in range(x-j,x+j+1):
                for rowIndex in range(y-j,y+j+1):
                    if ((0 <= colIndex) and (colIndex < self.boardSize)):
                        if ((0 <= rowIndex) and (rowIndex < self.boardSize)):
                            if ((x,y) != (colIndex,rowIndex)):
                                if (abs(x-colIndex) + abs(y-rowIndex) <= 2):
                                    listToReturn.append([colIndex,rowIndex])
            return listToReturn

        return []


    def AIPlay(self):
        while (self.numFlag <= self.numMines):
            #print(self)
            numFlagBefore = self.numFlag
            for x in range(0, self.boardSize):
                for y in range(0, self.boardSize):
                    #do flag stuff here
                    spotsRevealed = self.clickKnown(x,y)
            #print("Numflag now is ", doFlag)
            for x in range(0, self.boardSize):
                for y in range(0, self.boardSize):
                    #do flag stuff here
                    spotsRevealed = self.clickKnown(x,y)
            change = self.numFlag - numFlagBefore
            if ((change == 0) and (spotsRevealed == 0)): 
                if (self.numFlag < self.numMines): 
                    #print("The game is not solvable without guessing with " +  str(self.numFlag) + " flags out of " + str(self.numMines) + " mines")
                    return 0
                    break
                else:
                    #print("Game won!!")
                    return 1
                    break
            #Keep track of flag it self



    def clickKnown(self,x,y):
        spotsRevealed = 0
        neighborList = self.getNeighbors(x,y,self.option)
        #print(x,y,neighborList)
        if (self.board[x][y].selected == True):
            [p,q,r,x,y] = self.getSurInfo(x,y)
            if (q == r):
                #print("Do q==r")
                #print(neighborList)
                for neighbor in neighborList:
                    spot = self.board[neighbor[0]][neighbor[1]]
                    if (spot.flag == False):
                        if (spot.selected == False):
                            spotsRevealed += 1
                            self.makeMove(neighbor[0], neighbor[1])
                #print([p,q,r,x,y], self.numFlag)
                #print("Reveal " + str(spotsRevealed) + " spots")
                #print(self)
            if (p+q == len(neighborList)):
                #print("Do p+q == neighborSize")
                #print(neighborList)
                for neighbor in neighborList:
                    spot = self.board[neighbor[0]][neighbor[1]]
                    if (spot.flag == False):
                        if (spot.selected == False):
                            spot.flag = True
                            self.numFlag += 1
                #print([p,q,r,x,y], self.numFlag)
                #print(self)
        return spotsRevealed


    def hitMine(self, x, y):
        return self.board[x][y].value == -1

    def isWinner(self):
        return self.selectableSpots == 0

from random import randint


#play game
def playGame():
    boardSize = int(input("Choose the Width of the board: "))
    numMines = int(input("Choose the number of mines: "))
    gameOver = False
    winner = False
    Board = boardClass(boardSize, numMines)
    #print(Board)
    for i in range(boardSize*boardSize/2):
        x = randint(0, boardSize-1)
        y = randint(0, boardSize-1)
        Board.makeSafeMove(x,y)
    print(Board)
    print(Board.printReal())

    while not gameOver:
        aiOrNot = int(input("You want AI?: "))
        if (aiOrNot == 1):
            Board.AIPlay()
            print(Board)
            gameOver = Board.hitMine(x, y)
            #print("Value of gameover is", gameOver)
            if Board.isWinner() and gameOver == False:
                print("(x,y) is" + str(x) + " " + str(y))
                gameOver = True
                winner = True
        elif (aiOrNot == 0):
            print(Board)
            print("Make your move:")
            x = int(input("x: "))
            y = int(input("y: "))
            Board.makeMove(x, y)
            gameOver = Board.hitMine(x, y)
            if Board.isWinner() and gameOver == False:
                gameOver = True
                winner = True
        else:
            print("Please input y or n")

    print(Board)
    print(Board.printReal())
    if winner:
        print("Congratulations, You Win!")
    else:
        print("You hit a mine, Game Over!")

def analysis(boardSize, numMines, numGames, numReveal,option = 1,show=False):    
    gameWon = 0
    for i in range(numGames):
        Board = boardClass(boardSize, numMines,option)

        numShow = 0
        while (numShow < numReveal):
            x = randint(0, boardSize-1)
            y = randint(0, boardSize-1)
            # print(numShow)
            numShow += Board.makeSafeMove(x,y)        
        if (show):
            print("Starting Board")
            print(Board)
            print("Real board")
            print(Board.printReal())
        gameWon += Board.AIPlay()

        if (show):
            print("Finished Board")
            print(Board)


        #Think about ultimate solver
    #print("Won " + str(gameWon) + " out of " + str(numGames) + " games")
    return gameWon
availableOptions = 4
gameWonAll = []
for option in range(1,availableOptions+1):
    gameWonList = []
    for i in range(1,40):
        boardSize = 10
        #numMines = 30
        numMines = i
        numGames = 100
        numReveal = int(boardSize*boardSize/2)
        # print("boardSize is " + str(boardSize))
        # print("numMines is " + str(numMines))
        # print("numGames is " + str(numGames))
        # print("numReveal is " + str(numReveal))
        show = False

        gameWonList.append(analysis(boardSize, numMines, numGames, numReveal,option, show))
    print(gameWonList)
    gameWonAll.append(gameWonList)
#playGame()