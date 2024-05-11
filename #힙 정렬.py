def big_heap(a, b):
    """
    최대 힙을 구성하는 함수
    :param a: 리스트
    :param b: 현재 힙의 크기
    """
    for i in range(1, b + 1):
        c = i
        while c != 0:
            # 현재 노드 c와 그 부모 노드 r의 인덱스 계산
            r = (c - 1) // 2
            # 부모 노드의 값이 현재 노드의 값보다 작으면 두 노드의 값을 교환
            if a[r] < a[c]:
                a[r], a[c] = a[c], a[r]
            # 부모 노드로 이동하여 계속해서 최대 힙 조건을 만족시키도록 함
            c = r

def heap_s(a):
    """
    힙 정렬을 수행하는 함수
    :param a: 정렬할 리스트
    """
    # 힙 정렬의 핵심 과정을 수행
    for i in range(len(a) - 1, 0, -1):
        # 최대 힙을 구성하는 함수 호출
        big_heap(a, i)
        # 최대 힙에서 가장 큰 값을 맨 뒤로 이동
        a[0], a[i] = a[i], a[0]

# 주어진 리스트
arr = [40, 70, 60, 30, 10, 50, 90, 80, 20]

# 힙 정렬 수행
heap_s(arr)

# 정렬된 리스트 출력
print(arr)