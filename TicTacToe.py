from random import randrange
class Game:

    def __init__(self):
        self.board = Board()
        self.Human = (Player('X'))
        self.Gene = (Player('O'))
        counter = 1

        while(self.Winner() == None):
            # Loops turns until the game is won
            # Odd turns are Human, even are Gene
            if(counter%2 == 0):
                self.turn(self.Gene)
            else:
                self.turn(self.Human)
            counter += 1

        return self.Winner()

    def turn(self, plyr):
        # runs a turn for a player
        if(plyr == self.Human):
            print(self.board)
            targetSpot = int(input("You would like to play in spot: "))
            tempArray = self.board.getBoard()
            if(tempArray[targetSpot] != ' '):
                #prevents player from making same turn
                while(True):
                    targetSpot = int(input("That was the wrong answer try again:"))
                    if(tempArray[targetSpot] == ' '):
                        break

        # basic turn for Gene
        else:
            #gets Random number and checks to see if it is already used
            irand = randrange(9)
            tempArray = self.board.getBoard()
            if(tempArray[irand] != ' '):
                while(True):
                    irand = irand + 1
                    if(tempArray[irand] != ' '):
                        return
                    else:
                        targetSpot = irand
                        break
                    if(irand >= 10):
                        irand = 0
            else:
                print(irand)
                targetSpot = irand
        self.board.setPiece(targetSpot, plyr)

    def Winner(self):
        # Checks for and returns the winner
        return None

class Player:

    def __init__(self, n):
        self.setChar(n)

    def setChar(self, n):
        self.char = n

    def getChar(self):
        out = self.char
        return out

    def __str__(self):
        # Will output this return if you try to print the class
        return str.getChar()

class Board:

    def __init__(self):
        self.board = [None]*9
        self.setBlankBoard()

    def setBlankBoard(self):
        # Set every tile to None except for the center (which is Gene)
        default = [' ']*9
        default[4] = 'O'
        self.board = default

    def getBoard(self):
        out = self.board
        return out

    def setPiece(self, n, plyr):
        if((self.board[n] != 'X')and(self.board[n] != 'O')):
            self.board[n] = plyr.getChar()
        else:
            self.submitPlacement(int(input('Impossible move. Where would you like to place: '), plyr))

    def __str__(self):
        # Needed for outputting the Board
        # Front end developer's work here!
        """ Must return a string """

        out = ''
        for i in range(9):
            out += str(self.board[i])
            if(((i+1)%3 == 0)and(i != 0)):
                out += '\n-----\n'
            else:
                out += '|'
        return out

if __name__ == '__main__':
    print(Game())
