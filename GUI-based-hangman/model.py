import random

class Data:
    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = '_' * len(word)
        self.guessedChars = set()


    # 비밀단어
    def getSecretWord(self):
        return self.secretWord

    # 현재까지 맞춘 상태
    def getCurrentStatus(self):
        guessWord = ''
        for c in self.currentStatus:
            guessWord += (c + ' ')
        return guessWord

    # 현재까지 입력한 알파벳
    def getGuessedChars(self):
        guessed = ''
        for c in sorted(list(self.guessedChars)):
            guessed += (c + ' ')
        return guessed

    # 입력한 알파벳들 중 비밀단어에 있는 알파벳 현재상태에 반영
    def setCurrentStatus(self):
        self.currentStatus = ''
        for char in self.secretWord:
            if char in self.guessedChars:
                self.currentStatus += char
            else:
                self.currentStatus += '_'

    def setGuessedChars(self, char):
        self.guessedChars.add(char)



class Word:
    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1
        print('%d words in DB' % self.count)

    def randFromDB(self):
        randomWord = ''
        # 단어 길이가 3이상인 것이 나올 때 까지 단어 뽑기
        while len(randomWord) < 3:
            r = random.randrange(self.count)
            randomWord = self.words[r]
        return randomWord


class Hangman:

    text = [

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',

    ]

    def __init__(self):
        self.remainingLives = len(self.text) - 1

    # 남은 목숨
    def getRemainingLives(self):
        return self.remainingLives

    # 목숨 줄이기
    def decreaseLife(self):
        self.remainingLives -= 1

    # 현재 목숨에 대응하는 그림 그리기
    def currentShape(self):
        return self.text[self.remainingLives]