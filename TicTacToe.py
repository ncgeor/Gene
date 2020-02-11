class Game:

    def __init__(self):
        pass

    def turn(self, board, plyr):
        # runs a turn for a player
        pass

    def hasWinner(self):
        # Checks for and returns the winner
        pass

class Player:

    def __init__(self, n):
        self.setChar(n)

    def setChar(self, n):
        self.char = n

    def getChar(self):
        return self.char


class Board:

    def __str__(self):
        # Needed for outputting the Board
        # Front end developer's work here!
        """ Must return a string """
        pass
