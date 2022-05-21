from hand import *
from bjhand import *


def testConstructor():
    h = Hand()
    print(f"Testing constructor. Expect an empty {h}")
    print(f"Expect numCards to be 0: {h.numCards}")
    print(f"Expect isEmpty property to be true: {h.isEmpty}")


def testAddCard():
    hList = Hand()
    h1 = Card(1, 2)
    h2 = Card(3, 4)
    h3 = Card(2, 1)
    hList.addCard(h1)
    hList.addCard(h2)
    hList.addCard(h3)
    print(f"Testing addCard. Expect hand to have 3 cards: {hList}")
    print(f"Expect numCards to be 3: {hList.numCards}")


def createHand():
    hList = Hand()
    h1 = Card(1, 2)
    h2 = Card(2, 4)
    h3 = Card(4, 3)
    hList.addCard(h1)
    hList.addCard(h2)
    hList.addCard(h3)
    return hList


def testDisCard():
    hList = createHand()
    print(f"Testing current hand. Expect hand to have 3 cards: {hList}")
    h2 = Card(2, 4)
    hList.disCard(h2)
    print(f"Removed 2 of spades from hand. Expect hand to have 2 cards: {hList}")


def testGetItem():
    hList = createHand()
    print(f"Testing list access by index. Current list with 3 cards: {hList}")
    h = hList[1]
    print(f"Element at index 1. Expect 5 of diamonds: {h}")


def testHasCard():
    hList = createHand()
    print(f"Current cards in hand: {hList}")
    h1 = Card(1, 2)
    c = hList.hasCard(h1)
    print(f"Testing hasCard with ace of clubs. Expect hasCard to return True: {c}")
    h2 = Card(2, 3)
    d = hList.hasCard(h2)
    print(f"Testing hasCard with 2 of hearts. Expect hasCard to return False: {d}")


def testIndexOf():
    hList = createHand()
    print(f"Current cards in hand: {hList}")
    c = hList.indexOf(5)
    print(f"Testing indexOf 5. Expect return -1: {c}")


def testHasCardWithValue():
    hList = createHand()
    print(f"Current cards in hand: {hList}")
    c = hList.hasCardWithValue(2)
    print(f"Testing hasCardWithValue. Expect return True: {c}")
    c = hList.hasCardWithValue(9)
    print(f"Testing hasCardWithValue. Expect return False: {c}")


def testHasCardWithSuit():
    hList = createHand()
    print(f"Current cards in hand: {hList}")
    c = hList.hasCardWithSuit(2)
    print(f"Testing hasCardWithSuit. Expect return True: {c}")
    c = hList.hasCardWithSuit(3)
    print(f"Testing hasCardWithSuit. Expect return False: {c}")


def testScore():
    hList = BJHand()
    h1 = Card(5, 1)
    h2 = Card(5, 2)
    hList.addCard(h1)
    hList.addCard(h2)
    print(f"Current cards in {hList}")
    print(f"Testing score. Expect score to be 10: {hList.score}")


def testIsAce():
    hList = BJHand()
    h1 = Card(1, 2)
    hList.addCard(h1)
    print(f"Current cards in {hList}")
    print(f"Testing isAce. Expect score to be 1: {hList.score}")










