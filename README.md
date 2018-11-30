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