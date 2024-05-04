# 정렬할 리스트를 정의합니다.
arr = [40, 70, 60, 30, 10, 50]

# 선택 정렬 알고리즘을 사용하여 리스트를 정렬합니다.
# 리스트의 길이만큼 반복합니다. 마지막 요소는 자동으로 정렬되기 때문에 len(arr) - 1만큼만 반복합니다.
for i in range(len(arr) - 1):
    # 현재 인덱스의 값을 최소값으로 가정합니다.
    small_idx = i
    # 현재 인덱스(i) 이후의 모든 요소를 비교하여 최소값을 찾습니다.
    for j in range(i + 1, len(arr)):
        # 현재까지의 최소값보다 작은 값을 찾으면 해당 인덱스를 최소값의 인덱스로 갱신합니다.
        if arr[small_idx] > arr[j]:
            small_idx = j

    # 현재 인덱스(i)와 최소값의 인덱스(small_idx)에 있는 요소를 교환합니다.
    arr[i], arr[small_idx] = arr[small_idx], arr[i]

# 정렬된 리스트를 출력합니다.
print(arr)