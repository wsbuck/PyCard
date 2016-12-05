from PyCard import playingcard
from PyCard import Deck
import matplotlib.pyplot as plt
from math import log

class Game_Engine(object):
    def __init__(self, Deck):
        self.Deck = Deck
        self.player1 = []
        self.player2 = []

    def deal(self):
        self.Deck.shuffle()
        while self.Deck.count() != 0:
            dummycard = self.Deck.card[0]
            del self.Deck.card[0]
            self.player1.append(dummycard)
            dummycard = self.Deck.card[0]
            del self.Deck.card[0]
            self.player2.append(dummycard)

    def war(self, counter):
        # self.counter = counter
        # print "%s and %s" % (len(self.player1), len(self.player2))
        # print "%s vs %s" % (self.player1[counter - 1].card_name, self.player2[counter - 1].card_name)
        # raw_input("pause...")
        if self.player1[counter - 1].number > self.player2[counter - 1].number:
            while counter != 0:
                dummycard = self.player1[counter - 1]
                del self.player1[counter - 1]
                self.player1.append(dummycard)
                dummycard = self.player2[counter - 1]
                del self.player2[counter - 1]
                self.player1.append(dummycard)
                counter = counter - 1
        elif self.player1[counter - 1].number < self.player2[counter - 1].number:
            while counter != 0:
                dummycard = self.player2[counter - 1]
                del self.player2[counter - 1]
                self.player2.append(dummycard)
                dummycard = self.player1[counter - 1]
                del self.player1[counter - 1]
                self.player2.append(dummycard)
                counter = counter - 1
        else:
            counter = counter + 4
            self.war(counter)

    def play_game(self):
        while len(self.player1) != 1:
            try:
                self.war(1)
            except:
                break
        if len(self.player1) > len(self.player2):
            return 1
        else:
            return 2

    def play_game_array(self):
        card_count1 = []
        card_count2 = []
        card_count1.append(26)
        card_count2.append(26)
        while len(self.player1) != 0:
            try:
                self.war(1)
            except:
                break
            card_count1.append(len(self.player1))
            card_count2.append(len(self.player2))
        if len(self.player1) > len(self.player2):
            return card_count1
        elif len(self.player2) > len(self.player1):
            return card_count2
        else:
            exit("error")
        # return card_count

###############################################################################
numgames = raw_input("Enter the amount of games you would like to simulate: ")
numgames = int(numgames) + 1

data = []

for x in range(1, numgames):
    a_Deck = Deck()
    a_Game = Game_Engine(a_Deck)
    a_Game.deal()
    data.append(a_Game.play_game_array())


for arr in data:
    t = []
    for x in range(1, len(arr) + 1):
        t.append(x)
    plt.plot(t, arr, "black")

plt.title('Games of War')
plt.xlabel('Turn Number')
plt.ylabel('Winner\'s Card Count')
plt.xscale('log')
plt.show()



# raw_input("...")
# p1, p2 = 0, 0
# for x in range(1,numgames):
#     a_Deck = Deck()
#     a_Game = Game_Engine(a_Deck)
#     a_Game.deal()
#     if a_Game.play_game() == 1:
#         p1 = p1 + 1
#     elif a_Game.play_game() == 2:
#         p2 = p2 + 1
#     else:
#         exit("Error")

# total = p1 + p2
# print "Player 1 wins %s games\nPlayer 2 wins %s games\nTotal %s games played" % (p1, p2, total)
