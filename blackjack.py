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

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('[h]it or [s]tand?').lower()

        if x[0] == 'h':
            hit(deck,hand)
        elif x[0] =='s':
            print('Player stands, Dealer is playing')
            playing = False
        else:
            print('try again')
            continue
        break

def show_some(player, dealer):
    print("\nDealer's hand:")
    print("<card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's hand:", *player.cards, sep='\n')

def show_all(player, dealer):
    print("\nDealer's hand:", *dealer.cards, sep='\n')
    print("Dealer's hand =",dealer.value)
    print("\nPlayer's hand:", *player.cards, sep='\n')
    print("Player's hand =",player.value)

def player_busts(player,dealer,chips):
    print('Player busts!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer busts!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()

def push(player, dealer):
    print("Push, you tied")

