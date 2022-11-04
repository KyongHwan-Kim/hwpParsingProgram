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
        userLabel = QLabel("기본 정보 : "+loadUserInfo['companyName']+" / " + loadUserInfo['userTeam']+" / " + loadUserInfo['userName'] +" / "+loadUserInfo['birthday'], self)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

