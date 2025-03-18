#function1.py

#함수 정의
def setValue(newValue):
    x = newValue
    print("함수내부:", x)


#함수 호출
retValue = setValue(5)
print(retValue)

#다중의 값을 리턴
def swap(x,y):
    return y, x

#호출
retValue = swap(3,4)
print(retValue)

#이름해석규칙(스코핑 룰) : 지역L > 전역G > 내장B 순서로 이름을 검색
x = 5           #전역변수
def func(a):
    return a+x

print(func(1))

def func2(a):
    x = 3       #지역변수
    return a+x

print(func2(1))

#기본값을 명시
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자 방식
def connectURL(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURL("multi.com", "80"))    #함수의 인자
print(connectURL(port="8080",server="multi.com"))   #키워드 인자