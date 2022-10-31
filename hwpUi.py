import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QCalendarWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox
)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
import json 

with open("defaultInfo.json", "r", encoding='UTF8') as user:
    loadUserInfo = json.load(user)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        totalVbox = QVBoxLayout()
        # User Info Setting
        userLabel = QLabel("기본 정보 : "+loadUserInfo['companyName']+" / " + loadUserInfo['userTeam']+" / " + loadUserInfo['userName'] +" / "+loadUserInfo['birthday'], self)
        userLabel.setAlignment(Qt.AlignCenter)
        userFont = userLabel.font()
        userFont.setPointSize(10)
        userLabel.setFont(userFont)
        totalVbox.addWidget(userLabel)
        # start Calender Setting
        startCal = QCalendarWidget(self)
        startCal.setGridVisible(True)
        startCal.clicked[QDate].connect(self.showStartDate)
        self.startLbl = QLabel(self)
        startDate = startCal.selectedDate()
        self.startLbl.setText("시작 일자 : "+startDate.toString())

        # end Calender Setting
        endCal = QCalendarWidget(self)
        endCal.setGridVisible(True)
        endCal.clicked[QDate].connect(self.showEndDate)
        self.endLbl = QLabel(self)
        endDate = endCal.selectedDate()
        self.endLbl.setText("종료 일자 : "+endDate.toString())
        #Calender Layout
        startCalVbox = QVBoxLayout()
        endCalVbox = QVBoxLayout()
        startCalVbox.addWidget(self.startLbl)
        startCalVbox.addWidget(startCal)
        endCalVbox.addWidget(self.endLbl)
        endCalVbox.addWidget(endCal)
        calHbox = QHBoxLayout()
        calHbox.addStretch(1)
        calHbox.addStretch(1)
        calHbox.addLayout(startCalVbox)
        calHbox.addLayout(endCalVbox)
        totalVbox.addLayout(calHbox)
        #monday
        self.monlbl = QLabel('월요일',self)
        monFont = self.monlbl.font()
        monFont.setPointSize(10)
        self.monlbl.setFont(monFont)
        moncb = QComboBox(self)
        moncb.addItem('06시')
        moncb.addItem('07시')
        moncb.addItem('08시')
        moncb.addItem('09시')
        moncb.addItem('10시')
        moncb.move(50, 50)
        moncb.activated[str].connect(self.onMonStartActivated)


        #Total Layout
        self.setLayout(totalVbox)
        # btn = QPushButton("Save", self)
        # btn.move(50, 50)
        # btn.resize(btn.sizeHint())
        # btn.clicked.connect(QCoreApplication.instance().quit)
        self.setWindowTitle("군인들을 위한 유연근무제 작성 툴 - made by justin")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showStartDate(self, date):
        self.startLbl.setText("시작 일자 : "+date.toString())

    def showEndDate(self, date):
        self.endLbl.setText("종료 일자 : "+date.toString())

    def showStartComboBox(self, week):    
        cb = QComboBox(self)
        cb.addItem('06시')
        cb.addItem('07시')
        cb.addItem('08시')
        cb.addItem('09시')
        cb.addItem('10시')
        cb.move(50, 50)
        cb.activated[str].connect(self.onActivated(cb, week))

    def showEndComboBox(self):    
        cb = QComboBox(self)
        cb.addItem('15시')
        cb.addItem('16시')
        cb.addItem('17시')
        cb.addItem('18시')
        cb.addItem('19시')
        cb.move(50, 50)
        return cb.activated[str]

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

