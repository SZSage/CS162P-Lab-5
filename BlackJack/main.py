from card import *
from deck import *
from bjhand import *
from hand import *


def main():

    print("Welcome to Blackjack\n")
    print("Play Blackjack against the dealer")
    deck = Deck()  # create deck
    deck.shuffle()  # shuffle deck

    playerHand = BJHand()  # create bj hand
    playerHand.addCard(deck.deal())  # add card from deck to hand
    playerHand.addCard(deck.deal())
    print()
    dealerHand = BJHand()
    dealerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())
    print(f"Player's {playerHand}Player's Score: {playerHand.score}\n")  # show player hand and score
    print(f"Dealer's {dealerHand}Dealer's Score: {dealerHand.score}\n")
    anotherCard = input("Do you want another card? Type yes/no: ")  # ask if user wants another card

    while anotherCard == "yes":
        playerHand.addCard(deck.deal())  # add card from deck to player hand
        print(f"Player's {playerHand}Player's score: {playerHand.score}")
        anotherCard = input("Do you want another card? Type yes/no: ")  # ask again
        if anotherCard == "yes":
            dealerHand.addCard(deck.deal())  # if yes, add another card

    if playerHand.score > 21:  # if player score is over 21, bust
        print("You busted. The dealer wins!")
    else:
        print()
        print(f"Dealer's {dealerHand}")  # display dealers hand
        while dealerHand.score < 17:  # if dealers hand < 17
            dealtCard = deck.deal()  # deal card
            print(f"Dealer has dealt: {dealtCard}")  # show dealt card
            dealerHand.addCard(deck.deal())  # add card to dealers hand
            print(f"Dealer's score: {dealerHand.score}\n")  # display dealers score

        if dealerHand.score > 21:  # bust if dealers hand is > 21
            print("The dealer busted. You win!")
        elif playerHand.score > dealerHand.score:
            print("You win!")
        elif playerHand.score < dealerHand.score:
            print("The dealer wins")
        else:
            print("It's a tie.")





if __name__ == '__main__':
    main()
