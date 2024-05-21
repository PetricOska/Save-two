stack=[]

ABC=input("문자열을 입력해 주세요:")

print("+++삽입되는 순서+++")

for char in ABC:
    stack.append(char)
    print(stack)

print("+++삭제되는 순서+++")

while stack:
    print(stack.pop(), end="")
print()
print(stack)