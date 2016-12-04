from sys import exit
from random import randint

class playingcard(object):
    def __init__(self, card_name):
        self.card_name = card_name
        self.number = None
        self.suite = None
        self.color = None


    def get_cardname(self):
        print self.card_name

class Deck(object):
    def __init__(self):
        self.card = []
        tempnum = 1
        cardnames = [
                    "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                    "Nine", "Ten", "Jack", "Queen", "King"
                    ]
        for x in range(1,53):
            if tempnum > 13:
                tempnum = 1
            if x <= 13:
                card_name = cardnames[(tempnum - 1)] + " of Hearts"
                card = playingcard(card_name)
                card.number = tempnum
                card.suite = "Hearts"
                card.color = "Red"
            elif x <= 26:
                card_name = cardnames[(tempnum - 1)] + " of Diamonds"
                card = playingcard(card_name)
                card.number = tempnum
                card.suite = "Diamonds"
                card.color = "Red"
            elif x <= 39:
                card_name = cardnames[(tempnum - 1)] + " of Spades"
                card = playingcard(card_name)
                card.number = tempnum
                card.suite = "Spades"
                card.color = "Black"
            else:
                card_name = cardnames[(tempnum - 1)] + " of Clubs"
                card = playingcard(card_name)
                card.number = tempnum
                card.suite = "Clubs"
                card.color = "Black"
            tempnum = tempnum + 1
            self.card.append(card)

    def shuffle(self):
        # self.createDeck()
        for x in range(0,1000):
            randnum = randint(0, len(self.card) - 1)
            tempcard = self.card[randnum]
            del self.card[randnum]
            self.card.append(tempcard)

    def count(self):
        return len(self.card)

class engine(object):
    def __init__(self, PlayingDeck):
        self.PlayingDeck = PlayingDeck

    def play(self):
        # self.PlayingDeck.shuffle()
        picknum = int(raw_input("> ")) - 1
        print self.PlayingDeck.card[picknum].card_name


# a_Deck = Deck()
# a_Game = engine(a_Deck)
# a_Game.play()
