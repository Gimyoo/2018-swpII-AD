class Guess:
    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = '_' * len(word)
        self.guessedChars = set()
        self.guess('')

    def guess(self, character):
        character = character.lower()
        self.guessedChars.add(character)
        if character not in self.secretWord:
            return False
        else:
            currentStatus = ''
            # matches = 0
            for c in self.secretWord:
                if c in self.guessedChars:
                    currentStatus += c
                else:
                    currentStatus += '_'

            self.currentStatus = currentStatus
            
            return True

    def finished(self):
        if self.currentStatus == self.secretWord:
            return True
        else:
            return False


    def displayCurrent(self):
        guessWord = ''
        for c in self.currentStatus:
            guessWord += (c + ' ')
        return guessWord


    def displayGuessed(self):
        guessed = ''
        for c in sorted(list(self.guessedChars)):
            guessed += (c + ' ')
        return guessed

    def getSecretWord(self):
        return self.secretWord

    def getCurrentStatus(self):
        return self.currentStatus

    def getGussedChars(self):
        return self.guessedChars