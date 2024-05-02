class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

w = input("회문을 입력하세요.")

s=[]
q=[]
st = Stack()
qu = Queue()

for char in w:
    st.push(char)
    qu.enqueue(char)

while not st.is_empty():
    s.append(st.pop())

while not qu.is_empty():
    q.append(qu.dequeue())  

j=0
i=0
for i in range(len(s)):
    
    if s[i]==q[j]:                  
        print("True")
    else :
        print("False")
    i+=1
    j+=1