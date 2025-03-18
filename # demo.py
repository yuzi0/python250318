# demo.py
print("Hello VS Code")

result = 3 + 5
print(result)

#디버깅: 논리적 오류를 찾는 도구
#반복문
#VS 사용법 - F5 디버깅 시작 / Ctrl+F5 디버깅없이 실행 / F11 한 줄씩 실행
for i in [1,2,3]: #VS 사용법 - 중단점(Break Point) 
    print(i)

#튜플
tp = (10,20,30)
print(tp)
print(type(tp))

#함수를 정의
def calc(a,b):
    return a+b, a*b

#함수를 호출
print(calc(3,4))

args = (5,6)
print(calc(*args))
#print(calc(args)) #오류 출력

#형식 변환
a = set((1,2,3))
print(a)
print(type(a))
b = list(a)
b.append(4)
print(b)
print(type(b))
