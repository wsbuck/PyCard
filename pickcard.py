from PyCard import playingcard
from PyCard import Deck
from PyCard import engine
from sys import exit

a_Deck = Deck()
# a_Deck.createDeck()
shuffle_bool = raw_input("Would you like to shuffle the Deck?\nEnter 'Y' or 'N': ")
if shuffle_bool.lower() == 'y':
    a_Deck.shuffle()
elif shuffle_bool.lower() == 'n':
    pass
else:
    print "Invalid Entry"
    exit(1)

a_Game = engine(a_Deck)
# for x in range(0,52):
#     print a_Deck.cards[x].card_name + " " + str(x)
print "Enter an integer 1 through %s" % str(a_Deck.count())
while True:
    try:
        a_Game.play()
    except:
        exit(1)
