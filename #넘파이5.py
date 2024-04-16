import numpy as np

# 이미지의 크기를 결정하는 상수 SIZE를 설정합니다.
SIZE = 5

# SIZE x SIZE 크기의 랜덤 이미지 배열을 생성합니다.
imageAry = np.random.randint(0, 255, size=(SIZE, SIZE))

# 초기 이미지 배열을 출력합니다.
print('### 1. 초기 이미지 배열 ###')
print(imageAry)

# 초기 이미지 배열을 'source.npy' 파일로 저장합니다.
np.save('source', imageAry)

# 이미지 배열의 모든 요소에 10을 더한 후 출력합니다.
print('### 2. 10 증가한 이미지 배열 ###')
imageAry += 10
print(imageAry)

# 128 미만인 요소를 0으로, 128 이상인 요소를 255로 바꾼 후 출력합니다. (흑백 처리)
print('### 3. 흑백 처리된 이미지 배열 ###')
imageAry = np.where(imageAry < 128, 0, 255)
print(imageAry)

# 이미지 배열의 요소를 반전시킨 후 출력합니다.
print('### 4. 반전된 이미지 배열 ###')
imageAry = 255 - imageAry
print(imageAry)

# 'result2.npy' 파일에서 이미지 배열을 복구하여 출력합니다.
print('### 복구1: result2.npy ###')
imageAry = np.load('result2.npy')
print(imageAry)

# 'result1.npy' 파일에서 이미지 배열을 복구하여 출력합니다.
print('### 복구2: result1.npy ###')
imageAry = np.load('result1.npy')
print(imageAry)

# 'source.npy' 파일에서 이미지 배열을 복구하여 출력합니다. (원본)
print('### 복구3(원본): source.npy ###')
imageAry = np.load('source.npy')
print(imageAry)
