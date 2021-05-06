#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton

from guess import Guess


class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1)
        statusLayout.addWidget(self.charInput, 3, 0)

        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.startGame)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

        # Start a new game on application launch!
        self.startGame()


    def startGame(self):
        self.logic = Guess()
        hangmanShape = self.logic.lifeData.currentShape()
        self.hangmanWindow.setPlaceholderText(hangmanShape)
        self.gameOver = False
        self.currentWord.setFixedWidth(350)
        self.currentWord.setText(self.logic.wordData.getCurrentStatus())
        self.guessedChars.setText(self.logic.wordData.getGuessedChars())
        self.message.clear()
        return

    def guessClicked(self):
        char = self.charInput.text()
        self.charInput.clear()
        self.message.clear()

        if self.gameOver == True:
            self.message.setText('Game over')
            return

        status = self.logic.guess(char)

        if status == 'WRONG':
            self.message.setText('You entered wrong value!')
            return

        if status == 'OVERLAP':
            self.message.setText('You already guessed \"' + char + '\"')
            return

        if status == 'FAIL':
            self.message.setText('\"' + char + '\" is not in secret word.')


        hangmanShape = self.logic.lifeData.currentShape()
        self.hangmanWindow.setPlaceholderText(hangmanShape)

        currentStatus = self.logic.wordData.getCurrentStatus()
        self.currentWord.setText(currentStatus)

        guessedChars = self.logic.wordData.getGuessedChars()
        self.guessedChars.setText(guessedChars)

        if self.logic.finished():
            self.message.setText('You Win!')
            self.gameOver = True

        elif self.logic.lifeData.getRemainingLives() == 0:
            self.message.setText('Game Over...')
            self.gameOver = True

        return



if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())

