from random import randrange
class Game:

    def __init__(self):
        self.board = Board()
        self.Human = (Player('X'))
        self.Gene = (Player('O'))
        counter = 1

        while(self.Winner(self.board) == False):
            # Loops turns until the game is won
            # Odd turns are Human, even are Gene
            if(counter%2 == 0):
                self.turn(self.Gene)
            else:
                self.turn(self.Human)
            counter += 1

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

    def Winner(self, b):
        # Checks for and returns the winner
        board = b.getBoard()

        Horizonal_1 = ((board[0] == board[1])and(board[0] == board[2]) and board[0] != ' ')
        Horizonal_2 = ((board[3] == board[4])and(board[3] == board[5]) and board[3] != ' ')
        Horizonal_3 = ((board[6] == board[7])and(board[6] == board[8]) and board[6] != ' ')
        Horizonal = Horizonal_1 or Horizonal_2 or Horizonal_3

        Vertical_1 = ((board[0] == board[3]) and (board[0] == board[6]) and board[6] != ' ')
        Vertical_2 = ((board[1] == board[4]) and (board[1] == board[7]) and board[7] != ' ')
        Vertical_3 = ((board[2] == board[5]) and (board[2] == board[8]) and board[8] != ' ')
        Vertical = Vertical_1 or Vertical_2 or Vertical_3

        Diagonal_1 = ((board[0] == board[4]) and (board[4] == board[8]) and board[8] != ' ')
        Diagonal_2 = ((board[4] == board[2]) and (board[4] == board[2]) and board[2] != ' ')
        Diagonal = Diagonal_1 or Diagonal_2
        return (Horizonal or Vertical or Diagonal)

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
        return str(self.getChar())

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
            self.board[n] = plyr
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
    j = Game()
