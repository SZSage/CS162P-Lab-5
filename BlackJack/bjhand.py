from hand import *


class BJHand(Hand):

    def __init__(self):
        super().__init__()
        self._cards = []

    @property
    def theScore(self):
        theScore = 0
        for c in self._cards:
            if c.isFaceCard():
                theScore += 10
            else:
                theScore += c.value
                return theScore





