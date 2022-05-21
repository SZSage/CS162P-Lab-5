from hand import *


class BJHand(Hand):
    def __init__(self):
        super().__init__()

    @property
    def theScore(self):
        """Calculates the score"""
        theScore = 0
        for c in self._cards:
            if c.isFaceCard():
                theScore += 10
            else:
                theScore += c.value
        if self.hasAce() and theScore <= 11:
            theScore += 10
        return theScore

    # def displayCards(self):
    #     if self._dealer:
    #         print("hidden")
    #         print(self._cards[1])
    #     else:
    #         for card in self._cards:
    #             print(card)
    #         print(f"Value: {self.theScore}")

    def isBusted(self):
        """bust if score is over 21"""
        if self.theScore > 21:
            return True

    def hasAce(self):
        """card with value 1"""
        self.hasCardWithValue(1)








