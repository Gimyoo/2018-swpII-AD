import unittest
import random
from dummy import Dummy

class TestDummy(unittest.TestCase):
    def setUp(self):
        self.dum = Dummy()

    def tearDown(self):
        pass


    def testDeckAndHandCardList(self):
        tmpList = self.dum.deck + self.dum.handCardList
        for i in range(2, 100):
            self.assertIn(str(i), tmpList)


    def testTakenCard(self):
        idx = random.randrange(0,8)
        tmpHandCardList = self.dum.handCardList
        tmpHandCardList[idx] = ''
        num = self.dum.handCardList[idx]
        self.dum.takenCard(num)
        self.assertEqual(self.dum.handCardList, tmpHandCardList)


    def testTakeCard(self):
        tmpHandCardList = self.dum.handCardList
        for i in range(8):
            if tmpHandCardList[i] == '':
                tmpHandCardList[i] = self.dum.deck[0]
        self.dum.takeCard(self.dum.handCardList)
        self.assertEqual(self.dum.handCardList, tmpHandCardList)


    def testCountDeck(self):
        self.assertEqual(self.dum.countDeck(), len(self.dum.deck))


    def testGetHandCardList(self):
        self.assertEqual(self.dum.getHandCardList(), self.dum.handCardList)