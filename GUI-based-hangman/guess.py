class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = '_' * len(word)
        self.guessedChars = set()
        self.guess('')


    def guess(self, character):
        self.guessedChars.add(character)
        if character not in self.secretWord:
            return False
        else:
            currentStatus = ''
            matches = 0
            for c in self.secretWord:
                if c in self.guessedChars:
                    currentStatus += c
                else:
                    currentStatus += '_'

            self.currentStatus = currentStatus

            return True

    # 게임 종료
    def finished(self):
        if self.currentStatus == self.secretWord:
            return True
        else:
            return False

    # 현재까지 맞춘 비밀단어의 상태
    def displayCurrent(self):
        guessWord = ''
        for c in self.currentStatus:
            guessWord += (c + ' ')
        return guessWord

    # 현재까지 입력한 단어를 오름차순으로 출력
    def displayGuessed(self):
        guessed = ''
        for c in sorted(list(self.guessedChars)):
            guessed += (c + ' ')
        return guessed

