## 함수 선언 부분 ##
def func1() :
    a = 10 #지역변수
    print("func1()에서 a값 %d" % a)

def func2() :
    print("func2()에서 a값 %d" % a)

## 변수 선언 부분 ##
a = 20 #전역 변수

## 메인 코드 부분 ##
print(func1())
print(func2())