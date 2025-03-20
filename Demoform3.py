# DemoForm2.py
# DemoForm2.ui + DemoForm2.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# 웰크롤링
from bs4 import BeautifulSoup
# 웹서버에 요청
import urllib.request
# 특정 문자열 검색
import re 

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 윈도우 클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    # 슬롯 메서드 추가
    def firstClick(self):
        hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}
        f = open('client.txt', 'wt', encoding='utf-8')
        for n in range(0,10): # 1페이지부터 10페이지까지의 게시글 탐색
                #클리앙의 중고장터 주소 
                data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
                #웹브라우져 헤더 추가 
                req = urllib.request.Request(data, headers = hdr) #사파리 브라우져로 접속하는 것을 표시
                data = urllib.request.urlopen(req).read() #위의 요청을 보내고 응답을 받음
                page = data.decode('utf-8', 'ignore') #한글 변환
                soup = BeautifulSoup(page, 'html.parser') #html로 파싱
                list = soup.findAll('span', attrs={'data-role':'list-title-text'})
                for item in list:
                        try:
                                title = item.text.strip() #공백 제거해서 출력
                                if (re.search('아이패드', title)):
                                        print(title)
                                        f.write(title + '\n')
                        except:
                                pass
        f.close()
        self.label.setText("중고장터 검색 완료")
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