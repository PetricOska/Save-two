import numpy as np
import random

# 파이썬 리스트 생성
pythonList = [random.randint(0, 255) for _ in range(5)]
print('* 파이썬 리스트 -->', pythonList)

# NumPy 배열로 변환
numpyAry1 = np.array(pythonList)
print('* array(pythonList) -->', numpyAry1)

# 0부터 4까지의 배열 생성
numpyAry2 = np.arange(5)
print('* arange(5) -->', numpyAry2)

# 3부터 7까지의 배열 생성
numpyAry3 = np.arange(3, 8)
print('* arange(3, 8) -->', numpyAry3)

# 0부터 99까지 20 간격으로 배열 생성
numpyAry3 = np.arange(0, 100, 20)
print('* arange(0, 100, 20) -->', numpyAry3)

# 모든 요소가 1인 배열 생성
numpyAry4 = np.ones(5)
print('* ones(5) --> \n', numpyAry4)

# 모든 요소가 1인 3x4 배열 생성
numpyAry5 = np.ones((3, 4))
print('* ones((3,4)) --> \n', numpyAry5)

# 모든 요소가 0인 배열 생성
numpyAry6 = np.zeros(5)
print('* zeros(5) -->', numpyAry6)

# 초기화되지 않은 배열 생성
numpyAry7 = np.empty(6)
print('* empty(6) -->', numpyAry7)

# 모든 요소가 33인 배열 생성
numpyAry8 = np.full(5, 33)
print('* full(5, 33) -->', numpyAry8)

# 대각선 요소만 1이고 나머지는 0인 배열 생성
numpyAry9 = np.identity(5)
print('* identity(5) --> \n', numpyAry9)
