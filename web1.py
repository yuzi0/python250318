# web.py
# 웹크롤링 코들르 작성

# Chap09_Selector.html, Chat09_test.html 파일 사용

from bs4 import BeautifulSoup

# 웹페이지 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()
# 검색이 용이한 객체 생성
soup = BeautifulSoup(page, 'html.parser')

# <p>태그 몽땅 검색
# print(soup.find_all("p"))

# <p>태그 한개 검색
# print(soup.find("p"))

# 조건 : <p class="outer-text">태그 검색
# print(soup.find_all("p", class_="outer-text"))

# attrs 속성을 이용한 <p>태그 검색
# print(soup.find_all("p", attrs={"class":"outer-text"}))

# 태그는 삭제하고 내부 컨텐츠만 가져오기 : text 속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    titme = title.replace("\n", "")
    print(title)