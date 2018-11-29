from PyQt5.QtWidgets import QPushButton


class basicButton(QPushButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setText(text)
        self.clicked.connect(callback)

class downCard(basicButton):
    def __init__(self, text, label, callback):
        super().__init__(text, callback)
        self.label = label
        self.setFixedHeight(100)
        self.setFixedWidth(80)

class holdCard(basicButton):
    def __init__(self, text, callback):
        super().__init__(text, callback)
        self.setEnabled(False)
        self.setFixedHeight(100)
        self.setFixedWidth(80)