import random

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


    def test(self):
        return 'default'


    def randFromDB(self):
        randomWord = ''
        # 단어 길이가 3이상인 것이 나올 때 까지 단어 뽑기
        while len(randomWord) < 3:
            r = random.randrange(self.count)
            randomWord = self.words[r]
        return randomWord



