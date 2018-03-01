from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Copure(QWidget):
    def __init__(self, parent=None):
        super(Copure, self).__init__(parent)

        self.newButton = QPushButton("New")
        self.loadButton = QPushButton("Load")
        self.cropButton = QPushButton("Crop")
        self.readButton = QPushButton("Read")
        self.sendButton = QPushButton("Send")
        self.quitButton = QPushButton("Quit")

        self.frontPageLayout = QHBoxLayout()
        self.frontPageLayout.addWidget(self.newButton)
        self.frontPageLayout.addWidget(self.loadButton)
        self.frontPageLayout.addWidget(self.cropButton)
        self.frontPageLayout.addWidget(self.readButton)
        self.frontPageLayout.addWidget(self.sendButton)
        self.frontPageLayout.addWidget(self.quitButton)

        self.mainLayout = QHBoxLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        self.mainLayout.addLayout(self.frontPageLayout)

        self.setLayout(self.mainLayout)
        self.setWindowTitle("Copure")

        self.newButton.clicked.connect(self.doNew)
        self.loadButton.clicked.connect(self.doLoad)
        self.cropButton.clicked.connect(self.doCrop)
        self.readButton.clicked.connect(self.doRead)
        self.sendButton.clicked.connect(self.doSend)
        self.quitButton.clicked.connect(self.close)

    def doNew(self):
        print("Inside doNew")

    def doLoad(self):
        print("Inside doLoad")

    def doCrop(self):
        print("Inside doCrop")

    def doRead(self):
        print("Inside doRead")

    def doSend(self):
        print("Inside doSend")

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Copure()
    screen.show()

    sys.exit(app.exec_())