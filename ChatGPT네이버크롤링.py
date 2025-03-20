#ChatGPT네이버크롤링.py

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_news_titles(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 네이버 검색 결과 페이지에서 뉴스 제목을 포함하는 태그 찾기
    titles = []
    for title in soup.select(".news_tit"):
        titles.append(title.text)
    
    return titles

def save_to_excel(data, filename="results.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "News Titles"
    
    ws.append(["News Title"])
    
    for title in data:
        ws.append([title])
    
    wb.save(filename)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"
    news_titles = crawl_news_titles(url)
    
    if news_titles:
        save_to_excel(news_titles)
    else:
        print("No news titles found.")
