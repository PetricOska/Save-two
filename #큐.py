from collections import deque

# 사용자로부터 정수 N을 입력받습니다. 이는 큐에 넣을 원소의 개수를 나타냅니다.
N = int(input())

# deque 자료구조를 생성합니다.
myQueue = deque()

# 1부터 N까지의 숫자를 큐에 추가합니다.
for i in range(1, N+1):
    myQueue.append(i)

# 큐에 원소가 하나 남을 때까지 반복합니다.
while len(myQueue) > 1:
    # 큐의 맨 앞의 원소를 제거합니다.
    myQueue.popleft()
    # 큐의 맨 앞의 원소를 꺼내서 다시 큐의 맨 뒤에 추가합니다.
    myQueue.append(myQueue.popleft())

# 큐에 남아 있는 원소를 출력합니다. 이것이 마지막으로 남은 원소입니다.
print(myQueue[0])
