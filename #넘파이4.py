import random

# 상수 정의
SIZE = 5
startRow, startCol = 1, 1
nSIZE = 3

# 초기값 설정
value = 1
myList1 = []

# 5x5 크기의 리스트 생성
for _ in range(SIZE):
    tmpList = []
    for _ in range(SIZE):
        tmpList.append(value)
        value += 1
    myList1.append(tmpList)

# myList1 출력
for i in range(SIZE):
    # 리스트 요소 출력
    [print("%3d" % myList1[i][k], end='') for k in range(SIZE)]
    print()

    # myList1에서 특정 영역 선택하여 myList2 생성
    myList2 = []
    for i in range(startRow, startRow + nSIZE):
        tmpList = []
        for k in range(startCol, startCol + nSIZE):
            tmpList.append(myList1[i][k])
        myList2.append(tmpList)

    # myList2 출력
    for i in range(nSIZE):
        # 리스트 요소 출력
        [print("%3d" % myList2[i][k], end='') for k in range(nSIZE)]
        print()
    print()
