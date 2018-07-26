# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                         [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []
        
    def __str__(self):
        # return a string representation of a hand
        self.string = ""
        for i in range(len(self.hand)):
            self.string += self.hand[i].__str__() + " "
        return "Hand contains " + self.string
    
    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        ace_involved = False        
        for card in self.hand:
            value += VALUES[card.get_rank()]
            if(card.get_rank() == "A"):
                ace_involved = True
        if(value <= 11 and ace_involved):
            value += 10
        return value
    
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += 80
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []        
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))        
        
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)
        
    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop(-1)
    
    def __str__(self):
        # return a string representing the deck
        result = ""
        for card in self.deck:
            result += " " + card.__str__()
        return "Deck contains" + result


#define event handlers for buttons
def deal():
    global outcome, in_play, score
    global deck, hand_dealer, hand_player
    
    outcome = "Hit or stand?"
    # your code goes here
    if(in_play == True):
        outcome = "Player lost because of re-deal! New deal?"
        score -= 1
        in_play = False
    else:
        deck = Deck()
        deck.shuffle()

        hand_dealer = Hand()
        hand_player = Hand()
        hand_player.add_card(deck.deal_card())
        hand_player.add_card(deck.deal_card())
        hand_dealer.add_card(deck.deal_card())
        hand_dealer.add_card(deck.deal_card())

        in_play = True

def hit():
    # replace with your code below    
    # if the hand is in play, hit the player
    global outcome, in_play, score
    
    if in_play:
        if hand_player.get_value() <= 21:
            hand_player.add_card(deck.deal_card())
        if hand_player.get_value() > 21:
            # if busted, assign a message to outcome, update in_play and score
            outcome = "You have busted. New deal?"
            in_play = False
            score -= 1
       
def stand():
    # replace with your code below
    global outcome, score, in_play
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more   
    while in_play and hand_dealer.get_value() < 17:
        hand_dealer.add_card(deck.deal_card())
        # assign a message to outcome, update in_play and score        
    if hand_dealer.get_value() > 21:
        outcome = "Dealer busted. Congratulations!"
        #            print "Dealer is busted. Player wins."
        score += 1
    else:
        if((hand_dealer.get_value() >= hand_player.get_value()) or
            (hand_player.get_value() > 21)):
            outcome = "Dealer wins. New deal?"
            score -= 1
        else:
            outcome = "Player wins. New deal?"
            score += 1

    in_play = False
        
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play, card_back, card_loc
    global outcome, score_player, score_dealer

    canvas.draw_text("Blackjack", [60, 70], 50, "Red")
    canvas.draw_text(outcome, [10, 150], 28, "Black")
    canvas.draw_text("Score " + str(score), [400, 70], 40, "Black")
    canvas.draw_text("Player", [60, 400], 30, "Black")
    canvas.draw_text("Dealer", [60, 200], 30, "Black")

    hand_player.draw(canvas, [100, 450])
    hand_dealer.draw(canvas, [100, 250])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136,300), CARD_BACK_SIZE)
                                    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
