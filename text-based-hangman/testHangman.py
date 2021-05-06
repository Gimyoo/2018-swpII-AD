import unittest
from hangman import Hangman

class testGame(unittest.TestCase):
    def setUp(self):
        self.h = Hangman()

    def tearDown(self):
        pass

    def testDecreaseLife(self):
        for i in range(6,-1,-1):
            self.assertEqual(self.h.remainingLives, i)
            self.h.decreaseLife()

    def testcurrentShape(self):
        self.assertEqual(self.h.currentShape(), self.h.text[6])

if __name__ == '__main__':
    unittest.main()


