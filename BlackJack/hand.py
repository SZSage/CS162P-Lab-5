from card import *


class Hand:
    def __init__(self):
        """Creates a hand of potential cards"""
        self._cards = []  # empty list, # _ for protected

    @property
    def isEmpty(self):
        """returns true if hand is empty"""
        return len(self._cards) == 0

    @property
    def numCards(self):
        """returns number of cards in hand"""
        return len(self._cards)

    def addCard(self, card):
        """add cards to the hand(list)"""
        self._cards.append(card)

    def disCard(self, index):
        """removes specific card from hand and returns it"""
        c = self._cards.remove(index)
        return c

    def hasCard(self, card):
        if isinstance(card, int):
            return self._cards in Hand
        else:
            return False

    def hasMatchingSuit(self, other):
        if isinstance(other, Card):
            return self._cards == other.suit
        else:
            return False

    def hasMatchingValue(self, other):
        if isinstance(other, Card):
            return self._cards == other.value
        else:
            return False

    def __getitem__(self, card):
        if isinstance(card, int):
            return self._cards[card]
        else:
            raise TypeError(f"Index must be an int {type(card)} {card}")

    def __str__(self):
        """String representation of cards in hand"""
        output = f"Hand: "
        for c in self._cards:
            output += f"[{c})] "
        output += "]\n"
        return output

