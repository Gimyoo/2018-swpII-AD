import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QMessageBox,
    QHBoxLayout, QVBoxLayout, )
from PyQt5.QtCore import Qt


from buttons import basicButton, downCard, handCard

from dummy import Dummy
from putCard import PutCard



class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.warning = QMessageBox()

        # Button
        self.startButton = basicButton('게임시작', self.startClicked)
        self.howToPlayButton = basicButton('게임방법', self.howClicked)
        self.exitButton = basicButton('게임종료', self.exitClicked)

        self.oneToHun1 = QPushButton('99\n\n↑\n\n1')
        self.oneToHun2 = QPushButton('99\n\n↑\n\n1')
        self.hunToOne1 = QPushButton('100\n\n↓\n\n2')
        self.hunToOne2 = QPushButton('100\n\n↓\n\n2')

        self.downCard = []
        for i in range(4):
            self.downCard.append(downCard('', i, self.downCardClicked))

        self.dummyDeck = QPushButton('남은 카드 수\n\n')
        self.dummyDeck.setFixedHeight(100)
        self.dummyDeck.setFixedWidth(80)

        self.turnEndButton = basicButton('턴 종료', self.turnEndClicked)
        self.turnEndButton.setFixedWidth(120)

        self.handCard = []
        for i in range(8):
            self.handCard.append(handCard('', self.handCardClicked))


        # Layout
        menuLayout = QHBoxLayout()
        menuLayout.addWidget(self.startButton)
        menuLayout.addWidget(self.howToPlayButton)
        menuLayout.addWidget(self.exitButton)

        basicCardLayout = QHBoxLayout()
        basicCardLayout.addWidget(self.oneToHun1)
        basicCardLayout.addWidget(self.oneToHun2)
        basicCardLayout.addWidget(self.hunToOne1)
        basicCardLayout.addWidget(self.hunToOne2)

        downCardLayout = QHBoxLayout()
        for i in range(4):
            downCardLayout.addWidget(self.downCard[i])

        downLayout = QVBoxLayout()
        downLayout.addLayout(basicCardLayout)
        downLayout.addLayout(downCardLayout)

        dummyLayout = QHBoxLayout()
        dummyLayout.addWidget(self.dummyDeck)

        turnEndLayout = QVBoxLayout()
        turnEndLayout.addLayout(dummyLayout)
        turnEndLayout.addWidget(self.turnEndButton)

        settingLayout = QHBoxLayout()
        settingLayout.addLayout(downLayout)
        settingLayout.addStretch()
        settingLayout.addLayout(turnEndLayout)
        settingLayout.addStretch()

        handCardLayout = QHBoxLayout()
        for i in range(8):
            handCardLayout.addWidget(self.handCard[i])

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
        self.handCardList = self.dummy.getHandCardList()

        self.putCard = PutCard(self.handCardList)
        self.downCardList = self.putCard.getDownCardList()

        for i in range(4):
            downCardNum = str(self.downCardList[i])
            self.downCard[i].setText(downCardNum)

        for i in range(8):
            handCardNum = str(self.handCardList[i])
            self.handCard[i].setText(handCardNum)

        self.dummyDeck.setText('남은 카드 수\n\n'+ str(self.dummy.countDeck()))


    # esc눌러서 게임종료
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            #정말 종료하시겠습니까?
            self.close()

    #게임시작
    def startClicked(self):
        self.gameStart()


    #게임방법
    def howClicked(self):
        self.warning.question(self, '게임방법',
                              '# 게임의 진행\n' +
                              '2~98까지의 숫자카드 98장을 잘 섞어 더미를 만들고 플레이어에게 8장을 나누어 줍니다.' +
                              '한 차례에 최소 2장의 카드를 내려놓아야합니다.' +
                              '원한다면 더 많은 카드를 내려놓을 수 있습니다.' +
                              '카드를 내려놓을 때는 한 번에 한 장씩 내려놓아야 하며, 내려놓을 때마다 원하는 위치를 선택한 뒤, 내려고하는 카드를 선택합니다.' +
                              '오름차순 위치에 카드를 놓을 때는 반드시 이전에 놓인 카드보다 높은 숫자를 놓아야 합니다.' +
                              '내림차순 위치는 오름차순 위치와 반대로 이전에 놓인 카드보다 낮은 숫자를 놓아야 합니다.'+
                              '카드를 조건에 맞게 내려놓았다면 차례를 마칠 수 있습니다.'
                              '차례를 종료하면 이번에 내려놓은 만큼의 카드를 더미에서 가져옵니다.\n\n' +

                              '#되돌리기 규칙\n' +
                              '일반적으로는 열마다 정해진 규칙대로 카드를 놓아야 하지만, 되돌리기 규칙에 해당하는 카드는 일반 규칙을 무시하고 놓을 수 있습니다.' +
                              '-오름차순 위치: 현재 위치에 표시된 카드보다 정확히 10이 낮은 카드를 낼 수 있습니다.' +
                              '-내림차순 위치: 현재 위치에 표시된 카드보다 정확히 10이 높은 카드를 낼 수 있습니다.\n\n' +

                              '#게임의 종료\n' +
                              '숫자 카드 더미가 떨어지면, 더 이상 카드를 뽑지 않고 게임을 진행합니다.'+
                              '만약 한 차례에 놓아야 하는 최소한의 카드를 내려놓을 수 없다면(카드 더미가 남아있다면 2장, 카드 더미가 없다면 1장)'+
                              '게임은 즉시 종료되고 플레이어는 게임에서 패배합니다.'+
                              '만약 플레이어가 자신의 카드를 전부 내려놓았다면, 플레이어들의 승리입니다.'

                              , QMessageBox.Yes)



    #게임종료
    def exitClicked(self):
        #정말 종료하시겠습니까?
        self.close()



    #턴 종료
    def turnEndClicked(self):
        self.putCount = self.putCard.getPutCount()
        self.handCardList = self.dummy.getHandCardList()

        if self.putCount >= 2:
            self.dummy.takeCard(self.handCardList)

            self.deckNum = self.dummy.countDeck()

            self.dummyDeck.setText('남은 카드 수\n\n' + str(self.deckNum))
            for i in range(8):
                self.handCard[i].setText(self.handCardList[i])
                self.handCard[i].setEnabled(False)
            self.putCard.resetPutCount()

            if self.putCard.guess(self.handCardList, self.deckNum) == False: #여긴 덱 장수 신경안씀
                self.warning.question(self, 'Game Over', 'You lose', QMessageBox.Yes)
                #self.startClicked() #게임 자동초기화
            else:
                pass
        else:
            self.warning.question(self, 'Error', '두 장 이상의 카드를 옮긴 후 종료 할 수 있습니다.', QMessageBox.Yes)
            self.dummyDeck.setText('남은 카드 수\n\n' + str(self.dummy.countDeck()))




    # 내려놓아진 패
    def downCardClicked(self):
        self.downLocation = self.sender()
        for i in range(8):
            self.handCard[i].setEnabled(True)


    # 사용자의 덱에 있는 카드
    def handCardClicked(self):
        self.holdNum = self.sender()

        try:
            downNum = int(self.downLocation.text())
            holdNum = int(self.holdNum.text())

            if self.putCard.checkPut(downNum, holdNum, self.downLocation.label):
                num = self.dummy.takenCard(self.holdNum.text())
                self.downLocation.setText(num)
                self.holdNum.setText('')

            for i in range(8):
                self.handCard[i].setEnabled(False)

            self.handCardList = self.dummy.getHandCardList()
            self.deckNum = self.dummy.countDeck()

            if self.deckNum == 0 and self.handCardList.count('')== 8:
                self.warning.question(self, 'Game Over', 'You Win (ﾉﾟ▽ﾟ)ﾉ', QMessageBox.Yes)
                #self.startClicked() #게임 자동초기화
            elif self.putCard.guess(self.handCardList, self.deckNum)== False and self.deckNum == 0:
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
