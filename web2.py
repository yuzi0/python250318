# web.py
# 웹크롤링 코들르 작성

# Chap09_Selector.html, Chat09_test.html 파일 사용

from bs4 import BeautifulSoup

# 웹페이지 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()
# 검색이 용이한 객체 생성
soup = BeautifulSoup(page, 'html.parser')

# 태그는 삭제하고 내부 컨텐츠만 가져오기 : text 속성
f = open("Chap09_test.txt", "wt", encoding="utf-8")
for tag in soup.find_all("p"):
    title = tag.text.strip()
    titme = title.replace("\n", "")
    print(title)
    f.write(title + "\n")
f.close()