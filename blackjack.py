import random
from card import Card
from deck import Deck
from hand import Hand
from chips import Chips

#variables
suits = ('Heats', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
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
            hit(deck, hand)
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

while True:
    print('\nWelcome to blackjack! You should know how to play. Closest to 21 w/o going over wins!\n\
    Dealer will hit till 17. Aces are 1 or 11. Good luck!' )

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    if player_hand.value <= 21:
        while dealer_hand.value <17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)

        if dealer_hand.value> 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand, dealer_hand)

    print("\nPlayer's chip total is", player_chips.total)

    new_game = input("Another hand? y or n ").lower()
    if new_game[0] =='y':
        playing=True
        continue
    else:
        print('Cashing out!')
        break