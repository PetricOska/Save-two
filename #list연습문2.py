a = []

for _ in range(5):
    i = int(input("점수를 입력하세요: "))
    a.append(i)

m = max(a)
n = min(a)
p = sum(a) / 5

print("5명의 성적은", a, end='\n')

while True:
    select = int(input("검색하고 싶은 내용을 고르시오(0:종료, 1:최고점, 2:최저점, 3:평균): "))

    if select == 1:
        print("5명 중 최고 점수는 %d입니다." % m)
        break
    elif select == 2:
        print("5명 중 최저 점수는 %d입니다." % n)
        break
    elif select == 3:
        print("5명의 평균점수는 %.2f입니다." % p)
        break
    elif select == 0:
        break