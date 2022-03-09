map = [[0 for i in range(8)] for j in range(8)]


def setQueen(i, j):
    for x in range(8):
        map[x][j] += 1
        map[i][x] += 1
        # диагонали, ведем учет клеток, которые уже перекрываются ферзями
        if 0 <= i+j-x < 8:
            map[i+j-x][x] += 1
        if 0 < i-j+x < 8:
            map[i-j+x][x] += 1
    map[i][j] = -1


def removeQueen(i, j):
    for x in range(8):
        map[x][j] -= 1
        map[i][x] -= 1
        # диагонали, ведем учет клеток, которые уже перекрываются ферзями
        if 0 <= i+j-x < 8:
            map[i+j-x][x] -= 1
        if 0 < i-j+x < 8:
            map[i-j+x][x] -= 1
    map[i][j] = 0


def printPosition():
    # формирование алфавита для шахматной доски
    abc = "abcdefgh"
    ans = []
    for i in range(8):
        for j in range(8):
            if map[i][j] == -1:
                ans.append(abc[j]+str(i+1))
    print(',  '.join(ans))


def solve(i):
    for j in range(8):
        if map[i][j] == 0:
            setQueen(i, j)
            if i == 7:
                printPosition()
            else:
                # рекурсия
                solve(i+1)
            removeQueen(i, j)


solve(0)
