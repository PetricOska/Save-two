def growRich():
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = goldMaze[0][0]

    rowSum = memo[0][0]
    for i in range(1, COL):
        rowSum += goldMaze[0][i]
        memo[0][i] = rowSum

    colSum = memo[0][0]
    for i in range(1, ROW):
        colSum += goldMaze[i][0]
        memo[i][0] = colSum

    for row in range(1, ROW):
        for col in range(1, COL):
            if memo[row][col-1] > memo[row-1][col]:
                memo[row][col] = memo[row][col-1] + goldMaze[row][col]
            else:
                memo[row][col] = memo[row-1][col] + goldMaze[row][col]

    print("## 메모이제이션 ##")
    for row in memo:
        print(' '.join(map(str, row)))

    path = [[0 for _ in range(COL)] for _ in range(ROW)]
    row, col = ROW-1, COL-1

    while row > 0 or col > 0:
        path[row][col] = goldMaze[row][col]
        if row == 0:
            col -= 1
        elif col == 0:
            row -= 1
        elif memo[row][col-1] > memo[row-1][col]:
            col -= 1
        else:
            row -= 1
    path[0][0] = goldMaze[0][0]

    print()
    print("## 메모이제이션(황금 미로 길) ##")
    for row in path:
        print(' '.join(map(str, row)))

    return memo[ROW-1][COL-1]


ROW, COL = 5, 5
goldMaze = [[1, 4, 4, 2, 2],
            [1, 3, 3, 0, 5],
            [1, 2, 4, 3, 0],
            [3, 3, 0, 4, 2],
            [1, 3, 4, 5, 3]]

maxGold = growRich()
print()
print('최대 황금 -->', maxGold)
