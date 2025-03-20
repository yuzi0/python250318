# DemoForm2.py
# DemoForm2.ui + DemoForm2.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 윈도우 클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    # 슬롯 메서드 추가
    def firstClick(self):
        self.label.setText("첫번째 버튼을 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭")

# 진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()