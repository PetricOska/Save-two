# 주어진 리스트
arr = [40, 70, 60, 30, 10, 50]

# 선택정렬 전 리스트 출력
print(f'선택정렬 전 : {arr}')

# 구분선 출력
print("+" * 40)

# 선택정렬 알고리즘 수행
for i in range(len(arr) - 1):
    # 현재 단계에서 가장 작은 값의 인덱스를 저장하는 변수 초기화
    min_idx = i
    
    # 현재 인덱스 이후의 값들과 비교하여 가장 작은 값을 찾음
    for j in range(min_idx + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    
    # 현재 단계에서 가장 작은 값과 현재 위치를 바꿈
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    # 현재 단계의 결과 출력
    print(f'{i+1}단계: {arr}')

# 구분선 출력
print("+" * 40)

# 선택정렬 결과 출력
print(f'선택정렬 결과 : {arr}')