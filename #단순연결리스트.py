class Node:
    def __init__(self, data):
        # 노드의 데이터를 설정합니다.
        self.data = data
        # 다음 노드를 가리키는 포인터를 초기화합니다.
        self.next = None

class LinkedList:
    def __init__(self):
        # 연결 리스트의 시작점인 헤드를 초기화합니다.
        self.head = None
    
    def append(self, data):
        # 새로운 노드를 생성합니다.
        new_node = Node(data)
        # 리스트가 비어있다면 새로운 노드를 헤드로 지정하고 종료합니다.
        if not self.head:
            self.head = new_node
            return
        # 리스트가 비어있지 않다면 마지막 노드를 찾아 새로운 노드를 연결합니다.
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def print_values(self):
        # 연결 리스트의 각 노드의 값을 출력합니다.
        current = self.head
        while current:
            # 각 노드의 데이터를 ':'를 기준으로 분리하여 값 부분만 출력합니다.
            value, _ = current.data.split(":")
            print("value:", value)
            current = current.next
        # 마지막 노드를 표시합니다.
        print("final node")

# 연결 리스트 생성
linked_list = LinkedList()
linked_list.append("일:65")
linked_list.append("월:54")
linked_list.append("화:12")
linked_list.append("수:117")
linked_list.append("목:80")
linked_list.append("금:31")
linked_list.append("토:0[0]")

# 출력
linked_list.print_values()