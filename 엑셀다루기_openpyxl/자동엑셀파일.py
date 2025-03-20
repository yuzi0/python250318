import openpyxl
import random

# 엑셀 워크북 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Products"

# 헤더 추가
headers = ["제품ID", "제품명", "수량", "가격"]
ws.append(headers)

# 샘플 제품명 리스트
product_names = [
    "TV", "냉장고", "세탁기", "에어컨", "전자레인지", 
    "청소기", "컴퓨터", "노트북", "스마트폰", "태블릿"
]

# 100개의 데이터 생성
for i in range(1, 101):
    product_id = f"P{i:03}"  # 제품 ID (예: P001, P002, ...)
    product_name = random.choice(product_names)  # 랜덤 제품명
    quantity = random.randint(1, 100)  # 수량 (1~100 랜덤)
    price = random.randint(10000, 1000000)  # 가격 (1만~100만 랜덤)
    ws.append([product_id, product_name, quantity, price])

# 엑셀 파일 저장
wb.save("products.xlsx")
print("products.xlsx 파일이 생성되었습니다.")