i=int(input("시작할 수를 입력하세요:"))

while i<=30:
    if i==28:
        print("%d는/은 중단하고자 했던 %d입니다."% (i, i))
        break
    elif i%2==0:
        print("%d는/은 짝수"% i)
    else :
        print("%d는/은 홀수"% i)
    i+=1