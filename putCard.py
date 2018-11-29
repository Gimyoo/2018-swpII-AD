
class PutCard:

    def __init__(self, cardlist):
        self.HandCard = cardlist
        self.count = 0
        self.putCount = 0
        self.cardList= [1, 1, 100, 100]

    def equalCard(self,card):
        if card in self.HandCard:
            return True
        else:
            return False

    def basicCount(self):
        self.putCount = 0

    def countReturn(self):
        return self.putCount

    def displayCard(self):
        cardlist = ''
        for i in range(4):
            cardlist += (str(self.cardList[i])+' ')
        return cardlist

    def guess(self, cardlist, deckNum):
        count = 0

        for i in range(len(cardlist)):
            if cardlist[i] == '':
                continue
            else:
                c = int(cardlist[i])

            if c + 10 == self.cardList[0] or c > self.cardList[0]:
                count += 1
            elif c + 10 == self.cardList[1] or c > self.cardList[1]:
                count += 1
            elif c - 10 == self.cardList[2] or c < self.cardList[2]:
                count += 1
            elif c - 10 == self.cardList[3] or c < self.cardList[3]:
                count += 1
            elif (c - 10) in cardlist:
                count += 1
            elif (c + 10) in cardlist:
                count += 1


        # print(self.cardList[0] , self.cardList[1], self.cardList[2], self.cardList[3])
        # print(count)

        if count < 2 and deckNum > 0:
            return False
        elif count < 1 and deckNum == 0: #덱 0장일때는 1개만 가능해도 메세지 안뜨게 처리
            return False
        else:
            return True


    def checkPut(self, downNum, holdNum, label):
        if label < 2:
            if downNum < holdNum or downNum == holdNum + 10:
                self.cardList[label] = holdNum
                self.putCount +=1
                self.count+=1
                return True
        else:
            if downNum > holdNum or downNum == holdNum-10:
                self.cardList[label] = holdNum
                self.putCount+=1
                self.count +=1
                return True

        return False

