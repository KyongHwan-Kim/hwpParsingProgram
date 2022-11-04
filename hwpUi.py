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

inputData = {
            "companyName": loadUserInfo['companyName'],
            "userTeam": loadUserInfo['userTeam'],
            "userName": loadUserInfo['userName'],
            "birthday": loadUserInfo['birthday'],
            "weekStart" : "",
            "weekEnd" : "",
            "monStart": "06시",
            "monEnd": "06시",
            "tuesStart": "06시",
            "tuesEnd": "06시",
            "wenStart": "06시",
            "wenEnd": "06시",
            "turStart": "06시",
            "turEnd": "06시",
            "friStart" : "06시",
            "friStart" : "06시",
            }
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
        inputData['weekStart'] = startDate.toString()

        # end Calender Setting
        endCal = QCalendarWidget(self)
        endCal.setGridVisible(True)
        endCal.clicked[QDate].connect(self.showEndDate)
        self.endLbl = QLabel(self)
        endDate = endCal.selectedDate()
        inputData['weekEnd'] = endDate.toString()

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
        #Total Setting
        totalHbox = QHBoxLayout()
        totalHbox.addStretch(1)
        totalHbox.addStretch(1)
        self.totallbl = QLabel('일괄 적용',self)
        totalFont = self.totallbl.font()
        totalFont.setPointSize(10)
        self.totallbl.setFont(totalFont)

        totalStartcb = QComboBox(self)
        totalStartcb.addItem('06시')
        totalStartcb.addItem('07시')
        totalStartcb.addItem('08시')
        totalStartcb.addItem('09시')
        totalStartcb.addItem('10시')
        totalStartcb.move(50, 50)
        totalStartcb.activated[str].connect(self.onTotalStartActivated)

        self.totallonglbl = QLabel(' ~ ',self)
        totallongFont = self.totallonglbl.font()
        totallongFont.setPointSize(10)
        self.totallonglbl.setFont(totallongFont)

        totalEndcb = QComboBox(self)
        totalEndcb.addItem('15시')
        totalEndcb.addItem('16시')
        totalEndcb.addItem('17시')
        totalEndcb.addItem('18시')
        totalEndcb.addItem('19시')
        totalEndcb.move(50, 50)
        totalEndcb.activated[str].connect(self.onTotalEndActivated)

        totalHbox.addWidget(self.totallbl)
        totalHbox.addWidget(totalStartcb)
        totalHbox.addWidget(self.totallonglbl)
        totalHbox.addWidget(totalEndcb)
        totalHbox.setAlignment(Qt.AlignCenter)
        totalVbox.addLayout(totalHbox)
        #monday
        monHbox = QHBoxLayout()
        monHbox.addStretch(1)
        monHbox.addStretch(1)
        self.monlbl = QLabel('월요일',self)
        monFont = self.monlbl.font()
        monFont.setPointSize(10)
        self.monlbl.setFont(monFont)

        monStartcb = QComboBox(self)
        monStartcb.addItem('06시')
        monStartcb.addItem('07시')
        monStartcb.addItem('08시')
        monStartcb.addItem('09시')
        monStartcb.addItem('10시')
        monStartcb.move(50, 50)
        monStartcb.activated[str].connect(self.onMonStartActivated)

        self.monlonglbl = QLabel(' ~ ',self)
        monlongFont = self.monlonglbl.font()
        monlongFont.setPointSize(10)
        self.monlonglbl.setFont(monlongFont)

        monEndcb = QComboBox(self)
        monEndcb.addItem('15시')
        monEndcb.addItem('16시')
        monEndcb.addItem('17시')
        monEndcb.addItem('18시')
        monEndcb.addItem('19시')
        monEndcb.move(50, 50)
        monEndcb.activated[str].connect(self.onMonEndActivated)

        monHbox.addWidget(self.monlbl)
        monHbox.addWidget(monStartcb)
        monHbox.addWidget(self.monlonglbl)
        monHbox.addWidget(monEndcb)
        monHbox.setAlignment(Qt.AlignCenter)
        totalVbox.addLayout(monHbox)
        #tuesday
        tusHbox = QHBoxLayout()
        tusHbox.addStretch(1)
        tusHbox.addStretch(1)
        self.tuslbl = QLabel('화요일',self)
        tusFont = self.tuslbl.font()
        tusFont.setPointSize(10)
        self.tuslbl.setFont(tusFont)

        tusStartcb = QComboBox(self)
        tusStartcb.addItem('06시')
        tusStartcb.addItem('07시')
        tusStartcb.addItem('08시')
        tusStartcb.addItem('09시')
        tusStartcb.addItem('10시')
        tusStartcb.move(50, 50)
        tusStartcb.activated[str].connect(self.onTusStartActivated)

        self.tuslonglbl = QLabel(' ~ ',self)
        tuslongFont = self.tuslonglbl.font()
        tuslongFont.setPointSize(10)
        self.tuslonglbl.setFont(tuslongFont)

        tusEndcb = QComboBox(self)
        tusEndcb.addItem('15시')
        tusEndcb.addItem('16시')
        tusEndcb.addItem('17시')
        tusEndcb.addItem('18시')
        tusEndcb.addItem('19시')
        tusEndcb.move(50, 50)
        tusEndcb.activated[str].connect(self.onTusEndActivated)

        tusHbox.addWidget(self.tuslbl)
        tusHbox.addWidget(tusStartcb)
        tusHbox.addWidget(self.tuslonglbl)
        tusHbox.addWidget(tusEndcb)
        totalVbox.addLayout(tusHbox)
        #wedsday
        wedHbox = QHBoxLayout()
        wedHbox.addStretch(1)
        wedHbox.addStretch(1)
        self.wedlbl = QLabel('수요일',self)
        wedFont = self.wedlbl.font()
        wedFont.setPointSize(10)
        self.wedlbl.setFont(wedFont)

        wedStartcb = QComboBox(self)
        wedStartcb.addItem('06시')
        wedStartcb.addItem('07시')
        wedStartcb.addItem('08시')
        wedStartcb.addItem('09시')
        wedStartcb.addItem('10시')
        wedStartcb.move(50, 50)
        wedStartcb.activated[str].connect(self.onWenStartActivated)

        self.wedlonglbl = QLabel(' ~ ',self)
        wedlongFont = self.wedlonglbl.font()
        wedlongFont.setPointSize(10)
        self.wedlonglbl.setFont(wedlongFont)

        wedEndcb = QComboBox(self)
        wedEndcb.addItem('15시')
        wedEndcb.addItem('16시')
        wedEndcb.addItem('17시')
        wedEndcb.addItem('18시')
        wedEndcb.addItem('19시')
        wedEndcb.move(50, 50)
        wedEndcb.activated[str].connect(self.onWenEndActivated)

        wedHbox.addWidget(self.wedlbl)
        wedHbox.addWidget(wedStartcb)
        wedHbox.addWidget(self.wedlonglbl)
        wedHbox.addWidget(wedEndcb)
        totalVbox.addLayout(wedHbox)
        #tursday
        turHbox = QHBoxLayout()
        turHbox.addStretch(1)
        turHbox.addStretch(1)
        self.turlbl = QLabel('목요일',self)
        turFont = self.turlbl.font()
        turFont.setPointSize(10)
        self.turlbl.setFont(turFont)

        turStartcb = QComboBox(self)
        turStartcb.addItem('06시')
        turStartcb.addItem('07시')
        turStartcb.addItem('08시')
        turStartcb.addItem('09시')
        turStartcb.addItem('10시')
        turStartcb.move(50, 50)
        turStartcb.activated[str].connect(self.onTurStartActivated)

        self.turlonglbl = QLabel(' ~ ',self)
        turlongFont = self.turlonglbl.font()
        turlongFont.setPointSize(10)
        self.turlonglbl.setFont(turlongFont)

        turEndcb = QComboBox(self)
        turEndcb.addItem('15시')
        turEndcb.addItem('16시')
        turEndcb.addItem('17시')
        turEndcb.addItem('18시')
        turEndcb.addItem('19시')
        turEndcb.move(50, 50)
        turEndcb.activated[str].connect(self.onTurEndActivated)

        turHbox.addWidget(self.turlbl)
        turHbox.addWidget(turStartcb)
        turHbox.addWidget(self.turlonglbl)
        turHbox.addWidget(turEndcb)
        totalVbox.addLayout(turHbox)
        #friday
        friHbox = QHBoxLayout()
        friHbox.addStretch(1)
        friHbox.addStretch(1)
        self.frilbl = QLabel('금요일',self)
        friFont = self.frilbl.font()
        friFont.setPointSize(10)
        self.frilbl.setFont(friFont)

        friStartcb = QComboBox(self)
        friStartcb.addItem('06시')
        friStartcb.addItem('07시')
        friStartcb.addItem('08시')
        friStartcb.addItem('09시')
        friStartcb.addItem('10시')
        friStartcb.move(50, 50)
        friStartcb.activated[str].connect(self.onFriStartActivated)

        self.frilonglbl = QLabel(' ~ ',self)
        frilongFont = self.frilonglbl.font()
        frilongFont.setPointSize(10)
        self.frilonglbl.setFont(frilongFont)

        friEndcb = QComboBox(self)
        friEndcb.addItem('15시')
        friEndcb.addItem('16시')
        friEndcb.addItem('17시')
        friEndcb.addItem('18시')
        friEndcb.addItem('19시')
        friEndcb.move(50, 50)
        friEndcb.activated[str].connect(self.onFriEndActivated)

        friHbox.addWidget(self.frilbl)
        friHbox.addWidget(friStartcb)
        friHbox.addWidget(self.frilonglbl)
        friHbox.addWidget(friEndcb)
        totalVbox.addLayout(friHbox)
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

    def onTotalStartActivated(self, text):
        friStartcb.setCurrentText(text)
        inputData['monStart'] = text
        inputData['tuesStart'] = text
        inputData['wenStart'] = text
        inputData['turStart'] = text
        inputData['friStart'] = text

    def onTotalEndActivated(self, text):
        inputData['monEnd'] = text
        inputData['tuesEnd'] = text
        inputData['wenEnd'] = text
        inputData['turEnd'] = text
        inputData['friEnd'] = text

    def onMonStartActivated(self, text):
        inputData['monStart'] = text
    def onMonEndActivated(self, text):
        inputData['monEnd'] = text
    def onTusStartActivated(self, text):
        inputData['tuesStart'] = text
    def onTusEndActivated(self, text):
        inputData['tuesEnd'] = text
    def onWenStartActivated(self, text):
        inputData['wenStart'] = text
    def onWenEndActivated(self, text):
        inputData['wenEnd'] = text
    def onTurStartActivated(self, text):
        inputData['turStart'] = text
    def onTurEndActivated(self, text):
        inputData['turEnd'] = text
    def onFriStartActivated(self, text):
        inputData['friStart'] = text
    def onFriEndActivated(self, text):
        inputData['friEnd'] = text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

