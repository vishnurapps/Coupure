from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
import xml.etree.cElementTree as ET
import time
import re

def readconfigEmail():
    try:
        e = ET.parse('EmailConfig.xml').getroot()
        uname = e.find("EmailConfig").find('UserName').text
        host = e.find("EmailConfig").find("Host").text
        port = e.find("EmailConfig").find("Port").text
        return uname, host, port
    except:
        return '','',''

class EmailConfigPopUp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() 

    def initUI(self):
        self.setWindowTitle("Email configuation")
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        self.setGeometry(width/2, height/2, 300, 300)
        lblUserName = QLabel("User Name", self)
        lblHostName = QLabel("Host", self)
        lblPort = QLabel("Port", self)

        hlayout0 = QGridLayout()
        self.tbHostAddr = QLineEdit()
        onlyInt = QIntValidator()
        self.tbPort = QLineEdit()
        self.tbPort.setValidator(onlyInt)
        self.tbUserName = QLineEdit()
        hlayout1 = QGridLayout()
        okButton = QPushButton("OK")
        okButton.clicked.connect(self.saveEmailConfig)
        cancelButton = QPushButton("Cancel")
        cancelButton.clicked.connect(self.closePopUp)
        hlayout0.addWidget(lblHostName,0,0)
        hlayout0.addWidget(self.tbHostAddr,0, 1, 1, 2)
        hlayout0.addWidget(lblUserName, 1, 0)
        hlayout0.addWidget(self.tbUserName, 1, 1, 1, 2)
        hlayout0.addWidget(lblPort, 2, 0)
        hlayout0.addWidget(self.tbPort, 2, 1, 1, 2)
        hlayout0.addWidget(okButton, 3, 1, 1, 1)
        hlayout0.addWidget(cancelButton, 3, 2, 1, 1)

        self.setLayout(hlayout0)
        self.setFixedSize(400, 150)
        self.readEmailConfig()
        self.show()
    def saveEmailConfig(self):
        if(not self.validateEmailConfig()):
            #TODO: messagebox invalid input
            return False
        self.writeEmailConfig()
        self.close()
    def closePopUp(self):
        self.close()
    def readEmailConfig(self):
        uname, host, port = readconfigEmail()
        self.tbUserName.setText(uname)
        self.tbHostAddr.setText(host)
        self.tbPort.setText(port)
    def validateEmailConfig(self):
        return re.match(r"[^@]+@[^@]+\.[^@]+", self.tbUserName.text())
    def writeEmailConfig(self):        
        root = ET.Element("root")
        doc = ET.SubElement(root, "EmailConfig")

        ET.SubElement(doc, "UserName").text = self.tbUserName.text()
        ET.SubElement(doc, "Host").text = self.tbHostAddr.text()
        ET.SubElement(doc, "Port").text = self.tbPort.text()

        tree = ET.ElementTree(root)
        tree.write("EmailConfig.xml")
        return True

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

    def emailConfig(self):
        self.w = EmailConfigPopUp()
        #self.w.setGeometry(QRect(100, 100, 400, 100))
        self.w.show()

    def createAction(self, menubar):
        exitAct = QAction('&Exit', self)
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        timeOutAct = QAction('&Timeout', self)
        timeOutAct.setStatusTip('Set screenshot timeout')
        timeOutAct.triggered.connect(qApp.quit)

        emailAct = QAction('&Email Configuration', self)
        emailAct.setStatusTip('Configure the emails')
        emailAct.triggered.connect(self.emailConfig)

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