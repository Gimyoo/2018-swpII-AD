The Game
===============
* 보드게임 'The Game'을 1인용으로 수정하여 만든 게임입니다.

<br>

#### 설치 및 실행
- 파이썬이 설치되어 있어야 합니다.
https://www.python.org/downloads/ 링크를 따라 이동하여 OS에 맞는 운영체제를 설치해주세요.
- PyQt5가 설치되어 있어야 합니다.
```python
pip install PyQt5
```
- 쉘에서 make명령어를 이용하여 게임을 실행할 수 있습니다.

<br>

#### 모듈
**gameGui.py**
- 인터페이스 위젯을 포함하는 UI 컴포넌트
- 게임의 기본적인 로직을 구현

**buttons.py**
- UI에 사용될 버튼을 구현

**dummy.py**
- 카드 더미와 사용자의 덱을 초기화하고 관리

**putCard.py**
- 사용자가 선택한 위치에 카드를 내려놓을 수 있는지 판단
- 게임의 승패 조건을 확인


<br>

#### 업데이트
**18/11/30**
- gameGUI 모델의 게임방법 수정

**18/11/30**
- 변수명 & 함수명 수정
    - **buttons**
        - class holdCard -> class handCard
    - **dummy**
        - self.handCard -> self.handcardList
        - def returnHand(self) -> def getHandCardList(self)
        - def returnDeck(self) -> def countDeck(self) 
    - **putCard**
        - self.cardList -> downCardList    
        - def basicCount(self) -> def resetPutCount(self)
        - def countReturn(self) -> def getPutCount(self)
    - **gameGui**
        - self.downOne1, self.downOne2, self.downHun1, selfdownHun2 -> self.downCard 리스트
        - holdCard -> handCard
        - holdCardLayout -> downCardLayout
        - holdLayout -> downLayout
        
- gameGui의 downCard와 putCard의 downCardList를 연결하여 downCard버튼들의 텍스트 설정

- 종료시 경고창 발생
    - **gameGui**
        - Endkey 추가
            - 어떤 버튼이 눌리는지 확인해서 종료 처리.

- putCard 알고리즘 변경
    - **putCard**
        - 몇 번 둘 수 있는지 예상 시뮬레이션의 폭을 넓게 수정
        - 이중 반복문 사용.
