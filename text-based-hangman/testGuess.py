import unittest

from guess import Guess

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('apple')
        self.g3 = Guess('abscess')
        self.g4 = Guess('biblical')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        # default
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ _ _ ')
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('D')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

        # apple : 중복되는 알파벳 존재
        self.assertEqual(self.g2.displayCurrent(), '_ _ _ _ _ ')
        self.g2.guess('e')
        self.assertEqual(self.g2.displayCurrent(), '_ _ _ _ e ')
        self.g2.guess('a')
        self.assertEqual(self.g2.displayCurrent(), 'a _ _ _ e ')
        self.g2.guess('p')
        self.assertEqual(self.g2.displayCurrent(), 'a p p _ e ')
        self.g2.guess('l')
        self.assertEqual(self.g2.displayCurrent(), 'a p p l e ')

        # abscess : 세번 사용되는 알파벳 존재
        self.assertEqual(self.g3.displayCurrent(), '_ _ _ _ _ _ _ ')
        self.g3.guess('e')
        self.assertEqual(self.g3.displayCurrent(), '_ _ _ _ e _ _ ')
        self.g3.guess('s')
        self.assertEqual(self.g3.displayCurrent(), '_ _ s _ e s s ')
        self.g3.guess('b')
        self.assertEqual(self.g3.displayCurrent(), '_ b s _ e s s ')
        self.g3.guess('a')
        self.assertEqual(self.g3.displayCurrent(), 'a b s _ e s s ')
        self.g3.guess('c')
        self.assertEqual(self.g3.displayCurrent(), 'a b s c e s s ')


        # biblical : 두번 이상 사용되는 알파벳 2개 이상 존재, 시작할 때 e, n 없음
        self.assertEqual(self.g4.displayCurrent(), '_ _ _ _ _ _ _ _ ')
        self.g4.guess('b')
        self.assertEqual(self.g4.displayCurrent(), 'b _ b _ _ _ _ _ ')
        self.g4.guess('i')
        self.assertEqual(self.g4.displayCurrent(), 'b i b _ i _ _ _ ')
        self.g4.guess('l')
        self.assertEqual(self.g4.displayCurrent(), 'b i b l i _ _ l ')
        self.g4.guess('c')
        self.assertEqual(self.g4.displayCurrent(), 'b i b l i c _ l ')
        self.g4.guess('a')
        self.assertEqual(self.g4.displayCurrent(), 'b i b l i c a l ')



    def testDisplayGuessed(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayGuessed(), ' e ')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' d e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')




if __name__ == '__main__':
    unittest.main()

