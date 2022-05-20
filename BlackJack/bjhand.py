from hand import *


class BJHand(Hand):
    def __init__(self):
        super().__init__()

    @property
    def theScore(self):
        theScore = 0
        for c in self._cards:
            if c.isFaceCard():
                theScore += 10
            else:
                theScore += c.value
        if self.hasAce() and theScore <= 11:
            theScore += 10
        return theScore

    def isBusted(self):
        if self.theScore > 21:
            return True

    def hasAce(self):
        self.hasCardWithValue(1)






