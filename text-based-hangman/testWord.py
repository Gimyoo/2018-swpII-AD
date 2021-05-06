import unittest
from word import Word

class testGame(unittest.TestCase):
    def setUp(self):
        self.word = Word('words.txt')

    def tearDown(self):
        pass

    def testRandFromDB(self):
        for _ in range(1000):
            w = self.word.randFromDB()
            self.assertTrue(w in self.word.words)


if __name__ == '__main__':
    unittest.main()
