class Game:

    def __init__(self):
        pass

    def turn(self, board, plyr):
        # runs a turn for a player
        print(board)
        targetSpot = input("You would like to play in spot: ")

    def hasWinner(self):
        # Checks for and returns the winner
        pass

    def playSpot(self, n, board):
        # n is an int where the player would like to play
        # check to see if it's free and place it
        # returns True if placed, False if it cannot
        pass


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
        self.board = [[None]*3]*3
        self.setBlankBoard()

    def setBlankBoard(self):
        # Set every tile to None except for the center (which is Gene)
        default = [[None]*3]*3
        default[0][0] = 'O'
        self.board = default

    def getBoard(self):
        out = self.board
        return out

    def __str__(self):
        # Needed for outputting the Board
        # Front end developer's work here!
        """ Must return a string """

        out = ''

        for i in range(3):
            for j in range(3):
                if(self.board[i][j] == None):
                    out += 'X'
                else:
                    out += str(self.board[i][j])
                if(j != 2):
                    out += '|'
            out += '\n-----\n'
        return out

if __name__ == '__main__':
    j = Board()
    print(j)
