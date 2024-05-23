from collections import deque

# 그래프 정의
BFS_graph = {
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
def dfs_func(BFS_graph, start):
    # 시작 노드를 큐에 추가
    que = deque([start])

    # 큐가 빌 때까지 반복
    while que:
        # 큐에서 노드를 꺼냄
        node = que.pop()
        print("node:", node)

        # 목표 노드 'E'에 도달하면 탐색 중단
        if node == "E":
            print("STOP")
            break

        # 현재 노드가 방문한 적이 없으면
        if node not in visited_list:
            # 방문한 노드 리스트에 추가하고 출력
            visited_list.append(node)
            print(f'방문지점:{visited_list}')

            # 현재 노드의 인접 노드들을 큐의 왼쪽에 추가하여 탐색 진행
            que.extendleft(BFS_graph[node])

# DFS 함수 호출
dfs_func(BFS_graph, 'A')