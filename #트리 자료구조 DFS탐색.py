# 그래프 정의: 딕셔너리 형태로 그래프를 표현합니다.
DFS_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# 방문한 노드를 저장할 리스트 초기화
visited_list = list()

# DFS 함수 정의
def dfs_func(DFS_graph, start):
    # 시작 노드를 방문한 리스트에 추가
    visited_list.append(start)
    # 방문한 지점 출력
    print(f'방문지점: {visited_list}')

    # 시작 노드의 인접 노드들에 대해 순회
    for node in DFS_graph[start]:
        print("node:", node)

        # 목표 노드인 'C'를 만나면 탐색 중단
        if node == "C":
            print("STOP")
            break

        # 해당 노드가 방문한 적이 없는 경우에만 재귀 호출하여 탐색을 이어감
        if node not in visited_list:
            dfs_func(DFS_graph, node)

# DFS 함수 호출
dfs_func(DFS_graph, 'A')
