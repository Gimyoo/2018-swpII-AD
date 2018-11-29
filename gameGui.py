import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QMessageBox,
    QHBoxLayout, QVBoxLayout, )
from PyQt5.QtCore import Qt


from buttons import basicButton, downCard, holdCard

from dummy import Dummy
from putCard import PutCard



class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.warning = QMessageBox()

        self.startButton = basicButton('게임시작', self.startClicked)
        self.howToPlayButton = basicButton('게임방법', self.howClicked)
        self.exitButton = basicButton('게임종료', self.exitClicked)

        self.oneToHun1 = QPushButton('99\n\n↑\n\n1')
        self.oneToHun2 = QPushButton('99\n\n↑\n\n1')
        self.hunToOne1 = QPushButton('100\n\n↓\n\n2')
        self.hunToOne2 = QPushButton('100\n\n↓\n\n2')

        self.downOne1 = downCard('1', 0, self.downCardClicked)
        self.downOne2 = downCard('1', 1, self.downCardClicked)
        self.downHun1 = downCard('100', 2, self.downCardClicked)
        self.downHun2 = downCard('100', 3, self.downCardClicked)

        self.dummyDeck = QPushButton('남은 카드 수\n\n')
        self.dummyDeck.setFixedHeight(100)
        self.dummyDeck.setFixedWidth(80)

        self.turnEnd = basicButton('턴 종료', self.turnEndClicked)
        self.turnEnd.setFixedWidth(120)

        self.holdCard = []
        for i in range(8):
            self.holdCard.append(holdCard('', self.holdCardClicked))


        menuLayout = QHBoxLayout()
        menuLayout.addWidget(self.startButton)
        menuLayout.addWidget(self.howToPlayButton)
        menuLayout.addWidget(self.exitButton)

        basicCardLayout = QHBoxLayout()
        basicCardLayout.addWidget(self.oneToHun1)
        basicCardLayout.addWidget(self.oneToHun2)
        basicCardLayout.addWidget(self.hunToOne1)
        basicCardLayout.addWidget(self.hunToOne2)

        holdCardLayout = QHBoxLayout()
        holdCardLayout.addWidget(self.downOne1)
        holdCardLayout.addWidget(self.downOne2)
        holdCardLayout.addWidget(self.downHun1)
        holdCardLayout.addWidget(self.downHun2)

        holdLayout = QVBoxLayout()
        holdLayout.addLayout(basicCardLayout)
        holdLayout.addLayout(holdCardLayout)

        dummyLayout = QHBoxLayout()
        dummyLayout.addWidget(self.dummyDeck)

        turnEndLayout = QVBoxLayout()
        turnEndLayout.addLayout(dummyLayout)
        turnEndLayout.addWidget(self.turnEnd)

        settingLayout = QHBoxLayout()
        settingLayout.addLayout(holdLayout)
        settingLayout.addStretch()
        settingLayout.addLayout(turnEndLayout)
        settingLayout.addStretch()

        handCardLayout = QHBoxLayout()
        for i in range(8):
            handCardLayout.addWidget(self.holdCard[i])

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(menuLayout)
        mainLayout.addLayout(settingLayout)
        mainLayout.addLayout(handCardLayout)

        self.setLayout(mainLayout)

        self.setWindowTitle('The Game')
        self.setGeometry(300, 100, 600, 400)

        self.show()
        self.gameStart()



    def gameStart(self):
        self.dummy = Dummy()
        self.hand = self.dummy.returnHand() #getter메소드 만들기,,?

        self.putCard = PutCard(self.hand)

        for i in range(8):
            self.holdCard[i].setText(str(self.hand[i]))

        self.dummyDeck.setText('남은 카드 수\n\n'+ str(self.dummy.returnDeck()))


    # esc눌러서 게임종료
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()



    #게임시작
    def startClicked(self):
        self.downOne1.setText('1')
        self.downOne2.setText('1')
        self.downHun1.setText('100')
        self.downHun2.setText('100')
        #재시작할때 숫자 원래대로 돌림.
        self.gameStart()


    #게임방법
    def howClicked(self):
        self.warning.question(self, '게임방법',
                              '# 게임규칙\n' +
                              '2~98까지의 숫자가 적힌 카드 99장이 있다. '
                              '1이 적힌 카드 위에는 오름차순에 해당되는 숫자카드만 둘 수 있고,' +
                              '100이 적힌 카드 위에는 오름차순에 해당되는 숫자카드만 둘 수 있다.\n' +
                              '즉, 앞의 두 카드에는 제일 위에 있는 숫자보다 큰 수만 둘 수 있고,' +
                              '뒤의 두 카드에는 제일 위에 있는 숫자보다 작은 수만 둘 수 있다.\n' +
                              '그러나 특수 규칙으로 앞의 두 카드에는 제일 위에 있는 숫자보다 정확히 10 작은 수를 둘 수 있고,'+
                              '뒤의 두 카드에는 제일 위에 있는 숫자보다 정확히 10큰 수를 둘 수 있다.\n'
                              '더미에 카드가 남아있다면 한 턴에 최소 2장이상 내려놓아야 턴을 종료할 수 있다.\n\n' +
                              '# 승리\n' +
                              '더미에 남아 있는 카드 수가 0이되고, 플레이어가 가진 카드도 모두 내려놓으면 승리한다.\n\n' +
                              '# 패배\n' +
                              '더미 또는 플레이어의 덱에 카드가 남아 있는데 더 이상 내려놓을 수 있는 카드가 없다면 패배한다.', QMessageBox.Yes)



    #게임종료
    def exitClicked(self):
        self.close()



    #턴 종료
    def turnEndClicked(self):
        self.putCount = self.putCard.putCount
        self.hand = self.dummy.returnHand()


        if self.putCount >= 2:
            self.dummy.takeCard(self.hand)

            self.deckNum = self.dummy.returnDeck()

            self.dummyDeck.setText('남은 카드 수\n\n' + str(self.deckNum))
            for i in range(8):
                self.holdCard[i].setText(self.hand[i])
                self.holdCard[i].setEnabled(False)
            self.putCard.basicCount()

            if self.putCard.guess(self.hand, self.deckNum) == False: #여긴 덱 장수 신경안씀
                self.warning.question(self, 'Game Over', 'You lose', QMessageBox.Yes)
                #self.startClicked() #게임 자동초기화
            else:
                pass
        else:
            self.warning.question(self, 'Error', '두 장 이상의 카드를 옮긴 후 종료 할 수 있습니다.', QMessageBox.Yes)
            self.dummyDeck.setText('남은 카드 수\n\n' + str(self.dummy.returnDeck()))




    # 내려놓아진 패
    def downCardClicked(self):
        self.downLocation = self.sender()
        for i in range(8):
            self.holdCard[i].setEnabled(True)


    # 사용자의 덱에 있는 카드
    def holdCardClicked(self):
        self.holdNum = self.sender()

        try:
            downNum = int(self.downLocation.text())
            holdNum = int(self.holdNum.text())

            if self.putCard.checkPut(downNum, holdNum, self.downLocation.label):
                num = self.dummy.takenCard(self.holdNum.text())
                self.downLocation.setText(num)
                self.holdNum.setText('')

            for i in range(8):
                self.holdCard[i].setEnabled(False)

            self.hand = self.dummy.returnHand()
            self.deckNum = self.dummy.returnDeck()

            if self.deckNum == 0 and self.hand.count('')== 8:
                self.warning.question(self, 'Game Over', 'You Win (ﾉﾟ▽ﾟ)ﾉ', QMessageBox.Yes)
                #self.startClicked() #게임 자동초기화
            elif self.putCard.guess(self.hand, self.deckNum)== False and self.deckNum == 0:
                self.warning.question(self, 'Game Over', 'You lose', QMessageBox.Yes)#여기선 덱이 0장일때만 승패관리함
                #self.startClicked() #게임 자동초기화
            else:
                pass

        except:
            self.warning.question(self, 'Error', '이미 낸 카드입니다.', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    ex.show()
    app.exec()
