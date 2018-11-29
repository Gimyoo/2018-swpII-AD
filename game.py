from dummy import Dummy
from putCard import PutCard
from gameGui import GUI

from PyQt5.QtWidgets import QApplication
import sys

class Game():
    def __init__(self):
        super().__init__()
        self.gui = GUI()
        self.gameStart()

    def gameStart(self):
        self.leftDeck = self.gui.dummy.returnDeck()
        self.gui.dummyDeck.setText('남은 카드 수\n\n' + str(self.leftDeck))

        for i in range(8):
            self.gui.holdCard[i].setText(str(self.gui.dummy.handCard[i]))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    sys.exit(app.exec_())