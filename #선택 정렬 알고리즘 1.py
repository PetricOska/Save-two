def select_sort(arr):
    min_idx = 0  # 가장 작은 값을 찾기 위한 인덱스 변수 초기화
    print(f'선택정렬 전: {arr}')  # 선택 정렬 전 배열 출력
    for i in range(len(arr) - 1):  # 배열의 길이 - 1 만큼 반복
        min_idx = i  # 현재 인덱스를 가장 작은 값의 인덱스로 설정
        print(f'인덱스[{min_idx}]의 값인 {arr[min_idx]}의 위치', end='->')  # 현재 인덱스의 값과 위치 출력
        for j in range(min_idx + 1, len(arr)):  # 현재 인덱스 이후의 값들과 비교하기 위한 반복문
            if arr[j] < arr[min_idx]:  # 현재 인덱스보다 작은 값을 발견하면
                min_idx = j  # 가장 작은 값의 인덱스를 업데이트
        
        # 가장 작은 값과 현재 위치의 값을 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f'배열에서 가장 작은 값인 {arr[i]} 위치[{min_idx}]와 변경')  # 교환 과정 출력
        print(f'인덱스[{i}]단계 교환 후 결과:{arr}')  # 현재 단계의 결과 출력
        print()
    print("=" * 70)  # 결과 구분을 위한 구분선 출력
    print(f'선택 정렬된 이후: {arr}')  # 선택 정렬된 배열 출력

array = [40, 70, 60, 30, 10, 50]  # 주어진 배열
select_sort(array)  # 선택 정렬 함수 호출