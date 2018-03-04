from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
import time

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

    def test(self):
        print("TIme over")

    def tick(self):
        print('tick')

    def doNew(self):
        print("Inside doNew")
        self.hide()
        time.sleep(5)
        if(self.isHidden()):

            self.timerScreen = QTimer()
            self.timerScreen.setInterval(2000)
            self.timerScreen.setSingleShot(True)
            self.timerScreen.timeout.connect(self.tick)

            QApplication.instance().beep()
            screen = QApplication.primaryScreen()
            if screen is not None:
                self.originalPixmap = screen.grabWindow(0)
            else:
                self.originalPixmap = QPixmap()
            print(self.screenshotLabel.width())
            print(self.screenshotLabel.height())
            self.screenshotLabel.setPixmap(self.originalPixmap.scaled(
                self.screenshotLabel.size(), Qt.KeepAspectRatio,
                    Qt.SmoothTransformation))
            self.screenshotLabel.show()
        self.show()

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

        self.screenshotLabel = QLabel()
        self.screenshotLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.screenshotLabel.setAlignment(Qt.AlignCenter)
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        padding = 150
        self.screenshotLabel.setMinimumSize(width-padding,height-padding)
        self.screenshotLabel.hide()

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

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.screenshotLabel)
        mainLayout.addLayout(frontPageLayout)

        centralWidget.setLayout(mainLayout)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Copure()
    screen.show()

    sys.exit(app.exec_())