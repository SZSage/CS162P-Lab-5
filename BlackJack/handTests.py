from hand import *
# from bjhand import *


def testConstructor():
    h = Hand()
    print(f"Testing constructor. Expect an empty hand: {h}")
    print(f"Expect numCards to be 0: {h.numCards}")
    print(f"Expect isEmpty property to be true: {h.isEmpty}")


def testAddCard():
    hList = Hand()
    h1 = Card(1, 2)
    h2 = Card(3, 4)
    hList.addCard(h1)
    hList.addCard(h2)
    print(f"Testing addCard. Expect hand to have 2 cards: {hList}")
    print(f"Expect numCards to be 2: {hList.numCards}")


def createHand():
    hList = Hand()
    h1 = Card(1, 2)
    h2 = Card(2, 5)
    h3 = Card(4, 3)
    hList.addCard(h1)
    hList.addCard(h2)
    hList.addCard(h3)
    return hList


def testDisCard():
    hList = createHand()
    print(f"Testing current hand. Expect hand to have 3 cards: {hList}")
    h2 = Card(2, 5)
    hList.disCard(h2)
    print(f"Removed 5 of diamonds from hand. Expect hand to have 2 cards: {hList}")


def testGetItem():
    hList = createHand()
    print(f"Testing list access by index. Current list with 3 cards: {hList}")
    h = hList[1]
    print(f"Element at index 1. Expect 5 of diamonds: {h}")


def testHasCard():
    hList = createHand()
    print(f"Current cards in hand: {hList}")

    # if Card(1, 2) in hList:
    #     print("True")
    # else:
    #     print("False")






