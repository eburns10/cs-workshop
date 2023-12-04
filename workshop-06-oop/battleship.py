
class Player:
    def __init__(self, name, private, target):
        self.name = name
        self.private = private
        self.target = target

    def __str__(self):
        return(f"Player {self.name}")
    
class Ship:
    def __init__(self, size, orientation, coordinate):
        self.size = size
        self.orientation = orientation
        self.coordinate = coordinate


    #### Check sink
    def checkSink(self):
        status = "Float"
        if len(self.coordinate) == 0:
            status = "Sunk"

        return(status)
    


class Board:
    emptySpace = "o"
    size = 10

    def __init__(self, type):
        self.board = [[self.emptySpace] * self.size for i in range(0, self.size)]
        self.type = type
        self.ships = []

    def __str__(self):
        strRepresent = ["".join(x) for x in self.board]
        ####tells to join each . in each mini list giving a list of 3 values that are each ...
        strRepresent = "\n".join(strRepresent)
        #### joins each ... with a line break in between to make board
        return(strRepresent)

    def setShips(self, player):
        
        
        sizes = [5,4,3,3,2]

        for i in sizes:

            successfulSet = False
            while not successfulSet:

                startCd = input(f"{player} please give starting coordinates for your ship with size {i} (i.e. 0,2):")
                start = startCd.split(",")
                startRow = start[0]
                startCol = start[1]
                endCd = input(f"{player} please give ending coordinates for your ship with size {i} (i.e. 0,2):")
                end = endCd.split(",")
                endRow = end[0]
                endCol = end[1]
                dir = "%"

                try:
                    startRow = int(startRow)
                    startCol = int(startCol)
                    endRow = int(endRow)
                    endCol = int(endCol)

                    if len(start) != 2 or len(end) != 2:
                        print("Coordinate nomenclature not correct. Try again.\n")
                        continue

                    if startRow >= self.size or startCol >= self.size or endRow >= self.size or endCol >= self.size:
                        print("Coordinates out of bounds. Try again. \n")
                        continue

                    if startRow < 0 or startCol < 0 or endRow < 0 or endCol < 0:
                        print("Coordinates out of bounds. Try again. \n")
                        continue
                
                    if abs(endCol - startCol) != 0 and abs(endRow - startRow) != 0:
                        print("Incorrect ship length. Try again. \n")
                        continue
                    


                    if abs(endCol - startCol) != i - 1 and abs(endRow - startRow) != i - 1:
                        print("Incorrect ship length. Try again. \n")
                        continue


                    high = None
                    low = None
                    constant = None

                    if abs(endCol - startCol) == 0:
                        dir = "|"
                        if endRow - startRow > 0:
                            high = endRow
                            low = startRow
                        else:
                            high = startRow
                            low = endRow

                        constant = endCol

                    if abs(endRow - startRow) == 0:
                        dir = "-"
                        if endCol - startCol > 0:
                            high = endCol
                            low = startCol
                        else:
                            high = startCol
                            low = endCol

                        constant = endRow
                
                   

                    valid = True
                    for j in range(low, high + 1):
                        if dir == "|":
                            if self.board[j][constant] != 'o':
                                print("Space is occupied. Try Again. \n")
                                valid = False
                                continue
                        
                        if dir == "-":
                            if self.board[constant][j] != 'o':
                                print("Space is occupied. Try Again. \n")
                                valid = False
                                continue
                    
                    if not valid:
                        continue


                    length = 0
                    coordinates = []
                    for k in range(low, high + 1):
                        if dir == "|":
                            cList = []
                            self.board[k][constant] = dir
                            cList.append(str(k))
                            cList.append(str(constant))
                            coordinate = ",".join(cList)
                            coordinates.append(coordinate)

                        
                        if dir == "-":
                            cList = []
                            self.board[constant][k] = dir
                            cList.append(str(constant))
                            cList.append(str(k))
                            coordinate = ",".join(cList)
                            coordinates.append(coordinate)
                        
                        length = high - low + 1
                 
                    self.ships.append(Ship(length, dir, coordinates))



                except ValueError:
                    print("Coordinate input was not an integer. Try again. \n")
                    continue
                successfulSet = True
        print(f"You have {len(self.ships)} ships")
        return(self.board)
    

    def checkShips(self):
        over = False
        if len(self.ships) == 0:
            over = True
        return(over)
    
    def checkVictory(self):
        isWin = False
        if len(self.ships) == 0:
            isWin = True
        return(isWin)
    
    def markBoard(self, owner, shooterTarget, coordinate, shot):
        
        row = coordinate[0]
        col = coordinate[1] 
        search = True
        if self.board[row][col] != "o":
            self = self.markShots(row, col, "x")
            shooterTarget = shooterTarget.markShots(row, col, "x")
            print("Hit!")
            for p in self.ships:
                for u in p.coordinate:
                    if u == shot:
                        p.coordinate.remove(u)

                hit = p.checkSink()
                if hit == "Sunk":
                    self.ships.remove(p)
                    print(f"Ship sunk! {owner} has {len(self.ships)} ship(s) remaining \n")
                    return(self.checkVictory())
                
            print(f"{owner} has {len(self.ships)} ship(s) remaining \n")

        else:
            self = self.markShots(row, col, "n")
            shooterTarget = shooterTarget.markShots(row, col, "n")
            print(f"Miss! {owner} has {len(self.ships)} ship(s) remaining \n")

        return(False)
        
    
    def markShots(self, row, col, character):
        self.board[row][col] = character
        return self
    
    def checkNew(self, shotList):
        final = True
        if self.board[int(shotList[0])][int(shotList[1])] != "o":
            print("Target previously attempted. Try again. \n")
            final = False
        return(final)
            

        

    


        
            

    
def createPlayer(playerNumber, private, target):
    name = input(f"Player {playerNumber}, what is your name: ")
    p = Player(name, private, target)

    return p

def createBoard(type):
    b = Board(type)

    return(b)
    
def promptPlayer(shooter, owner, shooterTarget, ownerBoard, board):
    successfulTurn = False

    while not successfulTurn:
        shot = input(f"{shooter} please pick a target: \n(Please note that you can access your own ships by typing 'private' or your previous shots by typing 'target')\n") 

        shotList = shot.split(",")
        if shot == "private":
            print(shooter.private)
            continue

        if shot == "target":
            print(shooter.target)
            continue

        if len(shotList) != 2:
            print("Invalid syntax, try again \n")
            continue
        
        try:
            shotList = [int(x) for x in shotList]
            if int(shotList[0]) >= board.size or int(shotList[1])  >= board.size:
            
                print("Target out of bounds, try again \n")
                continue
        
            if not shooterTarget.checkNew(shotList):
                continue


            check = ownerBoard.markBoard(owner, shooterTarget, shotList, shot)
            

            if check is not None:
                successfulTurn = True
                return(check)

        except ValueError:
            print("Coordinate input was not an integer. Try again. \n")
    

def main():
    private1 = createBoard("private")
    private2 = createBoard("private")
    target1 = createBoard("target")
    target2 = createBoard("target")
    p1 = createPlayer(1, private1, target1)
    p2 = createPlayer(2, private2, target2)
    
    (p1.private).setShips(p1)
    (p2.private).setShips(p2)


    print(p1)
    print(f"Here is your private board, {p1}: \n{p1.private}")
    print(f"Here is your target board, {p1}: \n{p1.target}")
    print(p2)
    print(f"Here is your private board, {p2}: \n{p2.private}")
    print(f"Here is your target board, {p2}: \n{p2.target}")

    print(f"Welcome to battleship, {p1} and {p2} \n")
    
    gameFinished = False
    while not gameFinished:
        p1Turn = promptPlayer(p1, p2, p1.target, p2.private, p1.private)

        if p1Turn:
            print(f"Game Fininshed. {p1} has won!")
            gameFinished = True
            continue
        
        p2Turn = promptPlayer(p2, p1, p2.target, p1.private,  p2.private)


        if p2Turn:
            print(f"Game Finished. {p2} has won!")
            gameFinished = True
            continue




main()
