class Card:
    """ This class represents a playing card.
        A card has 2 attributes, value and suit.  value is an int between 1 and 13.  suit is an int between 1 and 4.
        It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""
    __values = ["", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Ten", "Jack", "Queen", "King"]
    __suits = ["", "Clubs", "Diamonds", "Hearts", "Spades"]

    # region constructor
    def __init__(self, value=0, suit=0):
        self.__value = value
        self.__suit = suit

    # endregion

    # region property getters and setters
    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    @suit.setter
    def suit(self, suit):
        if isinstance(suit, int) and 1 <= suit <= 4:
            self.__suit = suit
        else:
            raise ValueError(f"Suit must be an integer between 1-4 {type(suit)} {suit}")

    @value.setter
    def value(self, value):
        if isinstance(value, int) and 1 <= value <= 13:
            self.__value = value
        else:
            raise ValueError(f"Suit must be an integer between 1-13 {type(value)} {value}")

    # endregion

    # region card report

    def isAce(self):
        return self.__value == 1

    def isClub(self):
        return self.__suit == 1

    def isDiamond(self):
        return self.__suit == 2

    def isHeart(self):
        return self.__suit == 3

    def isSpade(self):
        return self.__suit == 4

    def isFaceCard(self):
        return self.__value in (11, 12, 13)

    # endregion

    def hasMatchingSuit(self, other):
        if isinstance(other, Card):
            return self.__suit == other.suit
        else:
            return False

    def hasMatchingValue(self, other):
        if isinstance(other, Card):
            return self.__value == other.value
        else:
            return False

    def __str__(self):
        return f'Card({Card.__values[self.__value]} of {Card.__suits[self.__suit]})'

    def __eq__(self, other):
        """ This "magic method" is called when you check the equality of 2 cards.  if card1 == card2 for example.
            2 cards are equal if they're both cards and if their attributes have the same values"""
        if isinstance(other, Card):
            return self.__suit == other.suit and self.__value == other.value
        else:
            return False