# 31256KB / 1688ms (Python3)
# 117436KB / 448ms (PyPy3)
# 풀긴 풀었는데 어렵당..

import sys
input = sys.stdin.readline

def checkSafeArea():
    visited = [[False]*M for _ in range(N)]
    safeArea = blankCount # 일단 빈칸을 모두 안전지대라고 가정
    stack = []
    for vi, vj in virusList:
        stack.append((vi, vj))
        visited[vi][vj] = True
        while stack:
            i, j = stack.pop()
            for v in range(4):
                nextI = i + dvi[v]
                nextJ = j + dvj[v]
                if 0<=nextI<N and 0<=nextJ<M and not visited[nextI][nextJ]:
                    visited[nextI][nextJ] = True
                    if labMap[nextI][nextJ] == 0: # 빈칸이 안전지대가 아닐때
                        stack.append((nextI, nextJ))
                        safeArea -= 1
    return safeArea

def bruteforce(startI, startJ, count):
    if count==3:
        global ans
        tempAns = checkSafeArea()
        ans = max(tempAns, ans)
        return
    # (startI, startJ) 부터 고르자
    for i in range(startI, N):
        for j in range(M):
            if i==startI and j<startJ: continue
            if labMap[i][j]==0:
                # (i, j)를 고름.
                labMap[i][j] = -1
                bruteforce(i+(j+1)//M, (j+1)%M, count+1)
                labMap[i][j] = 0
    

N, M = map(int, input().split())
labMap = []
virusList = []
blankCount = -3 # 벽 세울 빈칸 미리 빼둠
for i in range(N):
    labMap.append(list(map(int,input().split())))
    for j in range(M):
        if labMap[i][j] == 2:
            virusList.append((i, j))
        elif labMap[i][j] == 0:
            blankCount += 1 

dvi = [0, 0, 1, -1]
dvj = [1, -1, 0, 0]
ans = 0
bruteforce(0, 0, 0) # (0, 0) 부터 고르고, 세운 벽은 0개
print(ans)
