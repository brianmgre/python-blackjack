import random
from card import Card
from deck import Deck
from hand import Hand
from chips import Chips

#variables
suits = ('Heats', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eigth', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True

def take_bet(chips):
        while True:
            try:
                chips.bet = int(input('Place your bet: '))
            except ValueError:
                print('Your bet must be a number')
            else:
                if chips.bet > chips.total:
                    print("You don't have enough chips", chips.total)
                else:
                    break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()




# test_deck = Deck()
# print(test_deck)

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
test_player.value

for card in test_player.cards:
    print(card)