The Game 개발문서
===============

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