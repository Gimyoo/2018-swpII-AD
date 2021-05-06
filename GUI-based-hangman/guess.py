from model import Word
from model import Data
from model import Hangman

class Guess:
    def __init__(self):
        self.word = Word('words.txt')
        self.wordData = Data(self.word.randFromDB())
        self.lifeData = Hangman()
        self.guess('')

    def guess(self, char):
        secretWord = self.wordData.getSecretWord()

        if len(char) != 1:
            return 'WRONG'

        char.lower()

        guessedChars = self.wordData.getGuessedChars()
        if char in guessedChars:
            return 'OVERLAP'

        self.wordData.setGuessedChars(char)

        if char not in secretWord:
            self.lifeData.decreaseLife()
            return 'FAIL'
        else:
            self.wordData.setCurrentStatus()
            return 'SUCCESS'

    # 게임 종료
    def finished(self):
        currentStatus = self.wordData.getCurrentStatus()
        secretWord = self.wordData.getSecretWord()
        if currentStatus == secretWord:
            return True
        else:
            return False



