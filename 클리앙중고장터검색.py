# coding:utf-8
# 웰크롤링
from bs4 import BeautifulSoup
# 웹서버에 요청
import urllib.request
# 특정 문자열 검색
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

# 파일에 쓰기
f = open('F:\\교육\\20250317 Python핵심과정\\work\\client.txt', 'wt', encoding='utf-8')

for n in range(0,10): # 1페이지부터 10페이지까지의 게시글 탐색
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr) #사파리 브라우져로 접속하는 것을 표시
        data = urllib.request.urlopen(req).read() #위의 요청을 보내고 응답을 받음
        page = data.decode('utf-8', 'ignore') #한글 변환
        soup = BeautifulSoup(page, 'html.parser') #html로 파싱
        list = soup.findAll('span', attrs={'data-role':'list-title-text'})

        # <span class="subject_fixed" data-role="list-title-text" title="플레이스테이션5 (PS5) 슬림 디지털 에디션 팝니다. (택포 40만원)">
        #         플레이스테이션5 (PS5) 슬림 디지털 에디션 팝니다. (택포 40만원)
        # </span>

        for item in list:
                try:
                        title = item.text.strip() #공백 제거해서 출력
                        # print(title)
                        if (re.search('아이패드', title)):
                                print(title)
                                f.write(title + '\n')
                                # print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
# 파일 닫기
f.close()