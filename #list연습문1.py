a=[]

for _ in range(5):
    i=int(input("점수를 입력하세요"))

    a.append(i)

m=max(a)
n=min(a)
p=sum(a)/5

print("5명의 성적은", a, end='\n')
print("5명 중 최고 점수는 %d입니다."% m)
print("5명 중 최저 점수는 %d입니다."% n)
print("5명의 평균점수는 %d입니다."% p)