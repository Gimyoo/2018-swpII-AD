import random

# gui에서 안쓴거 주석처리 해뒀음
class Dummy:
    def __init__(self):
        self.deck = ['97','99','2','3','87','88','90','91','92','93','94','95','6','4','56']
        #for i in range(89,100):
        #    self.deck.append(str(i))
        #random.shuffle(self.deck)
        self.handCard = []
        self.handCard = self.deck[:8]
        self.deck= self.deck[8:]

    def returnHand(self):
        return self.handCard

    def returnDeck(self):
        return len(self.deck) #int


    def takenCard(self, num):
        idx = self.handCard.index(num)
        self.handCard[idx] = ''
        print(self.handCard)
        return num  #int


    def takeCard(self, hand):
        for i in range(8):
            if self.returnDeck() == 0:
                break
            else:
                if hand[i] == '':
                    hand[i] = self.deck.pop(0)
        self.handCard = hand



    # def displayHandCard(self):
    #     HandCard = ''
    #     for i in range(len(self.handCard)):
    #         HandCard += (str(self.handCard[i]) + ' ')
    #     return HandCard

