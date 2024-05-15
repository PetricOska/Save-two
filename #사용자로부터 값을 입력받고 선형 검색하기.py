# 빈 리스트 생성
LSearch_list = list()

# 사용자로부터 5개의 수 입력받아 리스트에 추가
for i in range(5):
    num = int(input("입력할 수를 입력하세요:"))
    LSearch_list.append(num)

# 입력된 리스트 출력
print("리스트=", LSearch_list)

# 사용자로부터 찾고자 하는 수 입력
search = int(input("찾고자 하는 수를 입력하세요:"))

# 리스트를 순회하며 검색하는 반복문
for idx in range(0, len(LSearch_list)):
    # 현재 인덱스의 값을 출력
    print(f'index {idx}:', LSearch_list[idx])
    
    # 검색값과 현재 인덱스의 값이 일치하는지 확인
    if LSearch_list[idx] == search:
        # 일치하면 탐색 성공 메시지 출력 후 종료
        print(f'인덱스[{idx}]에서 탐색 성공')
        print("탐색 종료")
        break