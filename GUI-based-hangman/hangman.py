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

