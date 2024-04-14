import numpy as np

# 행렬의 크기를 결정하는 상수
SIZE = 5

# 0부터 255 사이의 랜덤한 정수로 이루어진 SIZE x SIZE 크기의 행렬을 생성합니다.
numpyAry = np.random.randint(0, 255, size=(SIZE, SIZE))

# 생성된 행렬을 출력합니다.
print(numpyAry)
print()

# 행렬의 각 요소에 100을 더하여 값을 변경합니다.
numpyAry += 100

# 변경된 행렬을 출력합니다.
print(numpyAry)
