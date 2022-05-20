from hand import *


class BJHand(Hand):
<<<<<<< HEAD
    def __init__(self):
        super().__init__()
=======

    def __init__(self):
        super().__init__()
        self._cards = []
>>>>>>> aa4bd62e1076372b02b6a645265338bac1efe8c8

    @property
    def theScore(self):
        theScore = 0
        for c in self._cards:
            if c.isFaceCard():
                theScore += 10
            else:
                theScore += c.value
<<<<<<< HEAD
        if self.hasAce() and theScore <= 11:
            theScore += 10
        return theScore

    def isBusted(self):
        if self.theScore > 21:
            return True

    def hasAce(self):
        self.hasCardWithValue(1)
=======
                return theScore
>>>>>>> aa4bd62e1076372b02b6a645265338bac1efe8c8





