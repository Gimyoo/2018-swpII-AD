import random

class Dummy:
    def __init__(self):
        self.deck = []

        for i in range(2,100):
            self.deck.append(str(i))
        random.shuffle(self.deck)
        self.handCardList = []
        self.handCardList = self.deck[:8]
        self.deck = self.deck[8:]


    def takenCard(self, num):
        idx = self.handCardList.index(num)
        self.handCardList[idx] = ''
        #print(self.handCardList)
        return num  #int


    def takeCard(self, hand):
        for i in range(8):
            if self.countDeck() == 0:
                break
            else:
                if hand[i] == '':
                    hand[i] = self.deck.pop(0)
        self.handCardList = hand


    def countDeck(self):
        lenDeck = len(self.deck)
        return lenDeck #int


    def getHandCardList(self):
        return self.handCardList