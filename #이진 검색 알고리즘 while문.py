# 이진 탐색을 위한 리스트와 탐색할 값 설정
BSearch_list = [7, 10, 12, 25, 96, 1004]
search = 12

# 리스트의 처음과 끝 인덱스 설정
low = 0
high = 6  # 리스트의 길이는 6이지만 인덱스는 0부터 시작하므로 high는 5가 되어야 합니다.

# 탐색 횟수를 세는 변수 초기화
count = 0

# low가 high보다 작거나 같은 동안 반복
while low <= high:
    # 중간 인덱스 계산
    middle = int((low + high) / 2)

    # 중간 값이 찾는 값과 같으면
    if search == BSearch_list[middle]:
        count = count + 1
        # 검색 성공 메시지 출력
        print(f'주어진 리스트에서 인덱스[{middle}]위치의 값인 {search}을/를 총{count}번만에 검색성공')
        print("탐색종료")
        break
    # 찾는 값이 중간 값보다 크면
    elif search > BSearch_list[middle]:
        # low를 중간보다 하나 뒤로 이동
        low = middle + 1
        # 탐색 횟수 증가
        count = count + 1
    # 찾는 값이 중간 값보다 작으면
    else:
        # high를 중간보다 하나 앞으로 이동
        high = middle - 1
        # 탐색 횟수 증가
        count = count + 1