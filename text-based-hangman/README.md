Software Project II : hangman
====================
20181591 김유정
--------------


- game 파일을 실행하여 행맨 게임을 진행한다. 
- 사용자가 하나의 알파벳을 입력했을 때 랜덤으로
초기화된 비밀단어에 그 알파벳이 있으면 보여주고 없으면 목숨을 하나 줄인다. 목숨을 다 쓰기 전에
사용자가 비밀단어를 맞추면 승리하고, 맞추지 못한 채 목숨을 다 사용하면 패배한다.
- 게임의 요구사항에 해당하는 테스트 케이스를 만들고 유닛테스트를 진행한다.

<br>

---

## Requirements
**게임 시작**
- 프로그램을 실행하면 비밀단어, 입력한 단어 리스트, 목숨의 수, 
실패횟수를 초기화하여 사용자가 게임을 시작할 수 있게한다.

**게임 종료**
- 사용자가 목숨을 다 사용하기 전에 비밀 단어를 맞춘다면 성공, 맞추지 못한채 목숨을 다
사용한다면 실패를 보여주고 게임을 종료한다.
- 사용자가 모든 단어를 맞추었는데도 게임이 종료되지 않는 일이 발생해서는 안된다.

**현재 상황 출력**
- 사용자에게 지금까지 맞춘 알파벳과 남은 목숨을 보여준다.

**입력 판단**
- 사용자가 하나의 알파벳을 입력하면 그 알파벳이 비밀단어에 있는지 판단하여 있다면 보여주고
없다면 목숨을 하나 줄인다.
- 사용자가 추측한 알파벳을 입력하였을 때, 비밀단어에 해당 알파벳이 여러개 있다면 모두 출력하여
보여주어야한다. 만약 비밀단어가 apple이고, 사용자가 p를 입력하였다면 _ p p _ _ 를 출력해야한다.
- 사용자가 잘못된 입력을 할 경우, 잘못된 입력임을 알리고 입력을 무시한다.
- 사용자에게 입력받은 알파벳이 대문자라면 소문자로 변경한다.


<br>

## SW Design
**word** <br>
- 데이터베이스(word.txt)에서 랜덤으로 하나의 단어를 선택한다.

**hangman** <br>
- 게임이 시작할 때 사용자가 가지고 있는 목숨의 수를 설정한다.
- 게임을 진행하면서 남은 목숨의 수를 관리한다.
- 남은 목숨의 수에 대응하는 string을 설정한다.


**guess** <br>
- 비밀단어를 초기화한다.
- 현재까지 맞춘 알파벳과 실패한 횟수를 보여준다. 
- 사용자가 입력한 알파벳이 비밀단어에 있다면 해당하는 모든 위치에 그 알파벳을 출력한다.
- 사용자가 입력한 알파벳이 비밀단어에 없다면 실패횟수에 1을 추가하고, 남은 목숨을 1개 줄인다.
- 새로운 알파벳을 입력 받을 때 마다 리스트에 추가한다.
- 입력받은 알파벳이 대문자라면 소문자로 변경한다.

**game** <br>
- 게임을 종료할 때 까지 사용자에게 알파벳을 입력받아 게임을 진행한다.
- 게임 진행 상황을 출력한다.
- 숫자나, 한글 등 알파벳이 아닌 입력을 받을 경우 잘못된 입력임을 알리고 입력을 무시한다.
- 알파벳을 두 개 이상 입력 받을 경우 잘못된 입력임을 알리고 입력을 무시한다.
- 이전에 입력받은 알파벳이라면 이미 입력했음을 알리고 입력을 무시한다. 
- 사용자가 비밀단어의 모든 알파벳을 맞추었다면 성공했음을 알려주고
알파벳을 맞추기 전에 목숨을 다 사용했다면 실패했을 알려준다.
<br>

---

## Testcase and Unit test
다음과 같이 테스트케이스를 설정하여 테스트하였다.
```python
import unittest

from guess import Guess

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.g1 = Guess('default')      # 중복되는 알파벳이 없는 단어
        self.g2 = Guess('apple')        # 하나의 알파벳이 두번 등장하는 단어
        self.g3 = Guess('abscess')      # 하나의 알파벳이 세번 이상 등장하는 단어
        self.g4 = Guess('biblical')     # 두개 이상의 알파벳이 두번 이상 등장하는 단어

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        # default
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
```

<br>

---

## Code review
* 맞춰야 할 비밀단어 문자열을 '-'로 나타내기 위해 문자열의 길이만큼 for문을 반복하였는
파이썬은 문자열의 곱셈이 가능하여 파이썬의 특징을 살리기 위해 수정하였다.
```python
self.currentStatus = '_' * len(word)
```

- testGuess에서 guess메소드와 현재까지 입력한 문자들이 변수에 제대로 추가되었는지만
확인하였는데 각 변수를 받아오는 getter메소드를 만들어 테스트하는 것이 좋을 것 같다.

```python
    def getSecretWord(self):
        return self.secretWord
        
    def getCurrentStatus(self):
        return self.currentStatus
        
    def getGussedChars(self):
        return self.guessedChars
```



- 행맨 게임을 실행하기 위하여 게임이 진행되는 부분을 포함하여 총 4개의 모듈이 필요한데 과제에서는 guess모듈만 유닛테스트를 실행하였다. 나머지 모듈도 각각 요구사항
명세를 작성하여 테스트케이스를 만든 후 유닛테스트를 진행하면 
보다 나은 게임을 만들 수 있을 것이다.
    
    **guess**
    
    ```python
        def guess(self, character):
        character = character.lower()
        self.guessedChars |= {character}
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
    ```
    
    ```python
    def testDisplayCurrent(self):
        # default
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('D')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ _ _ _ _ ')
    ```
    
    <br>
    
    **word**
    
    ```python
        import unittest
        from word import Word
        
        class testGame(unittest.TestCase):
            def setUp(self):
                self.word = Word('words.txt')
        
            def tearDown(self):
                pass
        
            def testRandFromDB(self):
                for _ in range(100):
                    w = self.word.randFromDB()
                    self.assertTrue(w in self.word.words)
    ```
    
    <br>

    **hangman**
    
    ```python
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
    ```
     
