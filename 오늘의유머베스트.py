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
f = open('F:\\교육\\20250317 Python핵심과정\\work\\todayhumor.txt', 'wt', encoding='utf-8')

for n in range(1,11): # 1페이지부터 10페이지까지의 게시글 탐색
        #오늘의유머의 중고장터 주소 
        data = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr) #사파리 브라우져로 접속하는 것을 표시
        data = urllib.request.urlopen(req).read() #위의 요청을 보내고 응답을 받음
        page = data.decode('utf-8', 'ignore') #한글 변환
        soup = BeautifulSoup(page, 'html.parser') #html로 파싱
        list = soup.findAll('td', attrs={'class':'subject'})

        # <td class="subject">
        #   <a href="/board/view.php?table=bestofbest&amp;no=479074&amp;s_no=479074&amp;page=1" target="_top">만화모음 &amp; 펀딩 소식</a>
        #   <span class="list_memo_count_span"> [23]</span>  
        #   <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span>
        #   <img src="http://www.todayhumor.co.kr/board/images/list_icon_pencil.gif?2" alt="창작글" style="margin-right:3px;top:2px;position:relative"> 
        # </td>

        for item in list:
                try:
                        title = item.find('a').text.strip()
                        # print(title)
                        if (re.search('한국', title)):
                                print(title)
                                f.write(title + '\n')
                                # print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
# 파일 닫기
f.close()