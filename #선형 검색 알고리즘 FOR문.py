# 주어진 리스트 정의
LSearch_list = [12, 10, 27, 51, 7, 96]
print(LSearch_list)

# 초기 인덱스 설정
i = 0

# 사용자로부터 검색할 수 입력 받기
search = int(input("당신이 찾고자 하는 수를 입력해 검색해보세요>>> "))

# 리스트를 순회하며 검색하는 반복문
for i in range(0, len(LSearch_list)):
    # 현재 인덱스의 값을 출력
    print(f'index {i}:', LSearch_list[i])
    
    # 검색값과 현재 인덱스의 값이 일치하는지 확인
    if LSearch_list[i] == search:
        # 일치하면 탐색 성공 메시지 출력 후 종료
        print(f'인덱스[{i}]에서 탐색 성공')
        print('탐색 종료')
        break