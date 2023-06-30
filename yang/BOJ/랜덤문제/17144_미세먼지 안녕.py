# 117308KB / 436ms (PyPy3)
import sys
input = sys.stdin.readline

# 1. 미세먼지를 확산시키고
# 2. 공기청정기를 작동시킴

R, C, T = map(int, input().split())
array = []
dusts1 = []
dusts2 = []
firstCleaner = -1
secondCleaner = -1
for r in range(R):
    array.append(list(map(int, input().split())))
    for c in range(C):
        if array[r][c]==-1:
            if firstCleaner==-1:
                firstCleaner = r
            else:
                secondCleaner = r


dr = [0, 0, 1, -1] # 좌하우상 (반시계순)
dc = [1, -1, 0, 0]
for t in range(T):
    # 1. 미세먼지 확산
    tempArray = [array[i][:] for i in range(R)]
    for r in range(R):
        for c in range(C):
            if array[r][c] < 5: continue
            for v in range(4):
                nextR = r + dr[v]
                nextC = c + dc[v]
                if 0<=nextR<R and 0<=nextC<C and array[nextR][nextC]>=0:
                    tempArray[nextR][nextC] += array[r][c]//5
                    tempArray[r][c] -= array[r][c]//5
    array = tempArray
    # 2. 공기청정기 작동 - 반시계방향
    array[firstCleaner-1][0] = 0
    # 하
    for r in range(firstCleaner-1, -1, -1):
        if array[r][0] > 0:
            array[r+1][0] = array[r][0]
            array[r][0] = 0
    # 좌
    for c in range(1, C):
        if array[0][c] > 0:
            array[0][c-1] = array[0][c]
            array[0][c] = 0
    # 상
    for r in range(1, firstCleaner+1):
        if array[r][C-1] > 0:
            array[r-1][C-1] = array[r][C-1]
            array[r][C-1] = 0
    # 우
    for c in range(C-2, 0, -1): #C-1~1
        if array[firstCleaner][c] > 0:
            array[firstCleaner][c+1] = array[firstCleaner][c]
            array[firstCleaner][c] = 0
    
    # 2. 공기청정기 작동 - 시계방향
    array[secondCleaner+1][0] = 0
    # 상
    for r in range(secondCleaner+2, R):
        if array[r][0] > 0:
            array[r-1][0] = array[r][0]
            array[r][0] = 0
    # 좌
    for c in range(1, C):
        if array[R-1][c] > 0:
            array[R-1][c-1] = array[R-1][c]
            array[R-1][c] = 0
    # 하
    for r in range(R-2, secondCleaner-1, -1): 
        if array[r][C-1] > 0:
            array[r+1][C-1] = array[r][C-1]
            array[r][C-1] = 0
    # 우
    for c in range(C-2, 0, -1):
        if array[secondCleaner][c] > 0:
            array[secondCleaner][c+1] = array[secondCleaner][c]
            array[secondCleaner][c] = 0
    # print("=================")
    # print(f"{t}일 째")
    # for i in range(R):
    #     print(array[i])
    # print("=================")
ans = sum(map(sum, array))+2
print(ans)