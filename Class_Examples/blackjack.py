# Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables: 
# boolean in_play, strings player_message and dealer_message
in_play = False
player_message = ""
dealer_message = ""

# define globals for cards:
# tuples for suits and ranks
# dictionary of values
SUITS = ('C','S','H','D')
RANKS = ('A','2','3','4','5','6','7',
         '8','9','10','J','Q','K')
VALUES = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
          '8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card:", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    # pos is top left corner of card
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0]*RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1]*SUITS.index(self.suit))
        canvas.draw_image(card_images,
                          card_loc,
                          CARD_SIZE,
                          [pos[0] + CARD_CENTER[0],pos[1]+CARD_CENTER[1]],
                          CARD_SIZE)



# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        s = ''
        for card in self.cards:
            s += str(card) + ' '
        return s
    
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        v = 0
        for card in self.cards:
            v += VALUES[card.rank]
        for card in self.cards:
            if card.rank == 'A':
                if v + 10 <= 21:
                    v += 10
        return v
        
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas,
                      (pos[0] + CARD_SIZE[0]*self.cards.index(card),
                       pos[1]))
            


# define deck class 
class Deck:
    def __init__(self):
        self.cards = []	# create a Deck object
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.cards.append(Card(SUITS[i], RANKS[j]))
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)    
        

    def deal_card(self):
        return self.cards.pop(-1)
    
    def __str__(self):
        s = ""
        for card in self.cards:
            s += str(card) + " "
        return s
    
#define event handlers for buttons

#count deal in the middle of a round as a forfeit
#initialize deck
#initialize hands
#add cards to hands

def deal():
    global dealer_message, player_message, in_play
    global deck, player_hand, dealer_hand
    if in_play:
        dealer_message = "You forfeit, dealer wins."
        # update score if you have a score variable
        in_play = False

    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    
    player_message = "Hit or stand?"
    in_play = True

# if the hand is in play, deal a card to player's hand
# if busted, update message and in_play status
def hit():
    global player_message, player_hand, dealer_message, in_play
    
    if not in_play:
        player_message = "Please deal first!"
        return
    else:
        player_hand.add_card(deck.deal_card())
        
    player_val = player_hand.get_value()
    
    if player_val > 21:
        # Update Score
        player_message = "Busted! Deal again?"
        dealer_message = "Dealer Wins!"
        in_play = False
        
# if hand is in play, repeatedly hit dealer until 
# his hand has value 17 or more
# update message and in_play
def stand():
    global dealer_hand, player_message, dealer_message, in_play
    
    if not in_play:
        player_message = "Please deal first!"
        return
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        dealer_val = dealer_hand.get_value()
        
        if dealer_val > 21:
            # Update Score
            player_message = "Player Wins!"
            dealer_message = "Busted! Deal again?"
            in_play = False
        elif dealer_val >= player_hand.get_value():
            # Update Score
            player_message = "Deal again?"
            dealer_message = "Dealer Wins!"
            in_play = False
        else:
            # Update Score
            player_message = "Player Wins!"
            dealer_message = "Deal again?"
            in_play = False
            
        
# draw handler    
def draw(canvas):
    canvas.draw_text("Player's Hand", [50,375],20,"white")
    player_hand.draw(canvas,[50,400])
    canvas.draw_text("Dealer's Hand", [50,175],20,"white")
    dealer_hand.draw(canvas,[50,200])
    canvas.draw_text("BLACKJACK", [50,100],40,"white")
    canvas.draw_text(dealer_message, [300,175],20, "white")
    canvas.draw_text(player_message, [300,375],20, "white")
    #draw score if you have a score variable
    if in_play:
        canvas.draw_image(card_back,
                          CARD_BACK_CENTER,
                          CARD_BACK_SIZE,
                          [50 + CARD_BACK_CENTER[0],
                           200 + CARD_BACK_CENTER[1]],
                            CARD_BACK_SIZE)

# initialize frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and callbacks
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
