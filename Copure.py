from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *

class Copure(QMainWindow):
    def __init__(self, parent=None):
        super(Copure, self).__init__(parent)

        menubar = self.menuBar()
        centralwidget = QWidget()
        self.createAction(menubar)
        self.createButtons(centralwidget)
        self.statusBar()
        self.setCentralWidget(centralwidget)

        self.setWindowTitle("Copure")
        self.setWindowIcon(QIcon('cut.png'))
        self.statusBar().showMessage('Ready')

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

    def createAction(self, menubar):
        exitAct = QAction('&Exit', self)
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        timeOutAct = QAction('&Timeout', self)
        timeOutAct.setStatusTip('Set screenshot timeout')
        timeOutAct.triggered.connect(qApp.quit)

        emailAct = QAction('&Email Configuration', self)
        emailAct.setStatusTip('Configure the emails')
        emailAct.triggered.connect(qApp.quit)

        aboutCopureAct = QAction('&About', self)
        aboutCopureAct.setStatusTip('About Copure')
        aboutCopureAct.triggered.connect(qApp.quit)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(timeOutAct)
        editMenu.addAction(emailAct)
        aboutMenu = menubar.addMenu('&About')
        aboutMenu.addAction(aboutCopureAct)

    def createButtons(self, centralWidget):
        newButton = QPushButton("New", self)
        loadButton = QPushButton("Load", self)
        cropButton = QPushButton("Crop", self)
        readButton = QPushButton("Read", self)
        sendButton = QPushButton("Send", self)
        quitButton = QPushButton("Quit", self)

        frontPageLayout = QHBoxLayout()
        frontPageLayout.addWidget(newButton)
        frontPageLayout.addWidget(loadButton)
        frontPageLayout.addWidget(cropButton)
        frontPageLayout.addWidget(readButton)
        frontPageLayout.addWidget(sendButton)
        frontPageLayout.addWidget(quitButton)

        newButton.clicked.connect(self.doNew)
        loadButton.clicked.connect(self.doLoad)
        cropButton.clicked.connect(self.doCrop)
        readButton.clicked.connect(self.doRead)
        sendButton.clicked.connect(self.doSend)
        quitButton.clicked.connect(self.close)

        centralWidget.setLayout(frontPageLayout)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Copure()
    screen.show()

    sys.exit(app.exec_())