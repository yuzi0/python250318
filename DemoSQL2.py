# DemoSQL.py
# SQLite3를 사용한 데모
import sqlite3

# 연결객체는 생성 (물리적인 파일에 저장)
con = sqlite3.connect(r'F:\교육\20250317 Python핵심과정\work\sample.db')
# 커서 객체를 생성
cur = con.cursor()
# 테이블을 생성
cur.execute('CREATE TABLE PhoneBook (Name text, PhoneNum text);')
# 1건의 데이터를 입력
cur.execute("INSERT INTO PhoneBook VALUES ('Derick', '010-1234-5678');")
# 입력 파라미터 처리
name = '홍길동'
phoneNumber = '010-5678-1234'
cur.execute("INSERT INTO PhoneBook VALUES (?, ?);", (name, phoneNumber))
# 여러건 입력: 2차원 데이터 (2행 2열)
datalist = (('이순신', '010-1234-5678'), ('전우치', '010-5678-1234'))
cur.executemany("INSERT INTO PhoneBook VALUES (?, ?);", datalist)

# 데이터를 조회
cur.execute('SELECT * FROM PhoneBook;')
for row in cur:
    print(row)

# 정상적으로 완료
con.commit()