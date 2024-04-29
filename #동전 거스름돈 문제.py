def calculate_change(coins, amount):
    # 거스름돈을 저장할 딕셔너리 초기화
    change = {}
    
    print("거스름으로 바꿀 수 있는 동전 종류:", coins)
    print("고객에게 지불할 돈을 입력해주세요:")
    
    # 사용자로부터 고객에게 지불할 돈 입력 받기
    payment = int(input())
    
    # 주어진 동전의 종류를 내림차순으로 정렬하여 큰 단위 동전부터 처리
    for coin in sorted(coins, reverse=True):
        # 해당 동전으로 지불할 수 있는 최대 개수 계산
        count = payment // coin
        if count > 0:
            # 딕셔너리에 동전 종류와 개수 저장
            change[coin] = count
            # 지불할 금액에서 해당 동전으로 지불한 금액 뺌
            payment -= count * coin
            print(f"{coin}원의 개수:{count}")
            print(f"{coin}을 뺀 남은 액수:{payment}")
    
    # 거스름돈 딕셔너리와 동전별 개수 출력
    print("따라서, 거스름돈은 동전별 각각", change, "개 지불하면 됩니다.")

# 거스름돈 종류
coins = [500, 100, 50, 10]

# 거스름돈 계산 함수 호출
calculate_change(coins, 0)  # 두 번째 매개변수는 임시 값으로 전달