import random

SIZE = 5
# 5x5 크기의 이차원 리스트를 생성하기 위해 SIZE를 설정합니다.

pythonList = [[random.randint(0, 255) for _ in range(SIZE)] for _ in range(SIZE)]
# 0부터 255 사이의 랜덤한 정수를 가지는 5x5 크기의 이차원 리스트를 생성합니다.
# 리스트 컴프리헨션을 사용하여 행렬의 각 요소를 랜덤하게 초기화합니다.

# 생성된 리스트를 출력합니다.
for i in range(SIZE):
    for k in range(SIZE):
        print("%3d" % pythonList[i][k], end='')
    print()
print()

# 각 요소에 100을 더하여 값을 변경합니다.
for i in range(SIZE):
    for k in range(SIZE):
        pythonList[i][k] += 100

# 변경된 리스트를 출력합니다.
for i in range(SIZE):
    for k in range(SIZE):
        print("%3d" % pythonList[i][k], end ='')
    print()
