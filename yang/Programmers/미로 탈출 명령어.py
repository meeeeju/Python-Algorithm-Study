# 질문 게시판 참고 : https://school.programmers.co.kr/questions/43761

def solution(n, m, x, y, r, c, k):
    dirX = [1, 0, 0, -1] # array[x][y] 일 때 d, l, r, u
    dirY = [0, -1, 1, 0]
    direction = ["d", "l", "r", "u"]
    stack = [(x, y, 0, "")]
    while stack:
        x, y, count, path = stack.pop()
        if x == r and y == c:
            if (k - count) % 2 == 1:
                return "impossible"
            elif k == count:
                return path
        for v in range(4):
            nextX = x + dirX[v]
            nextY = y + dirY[v]
            if abs(nextX - r) + abs(nextY - c) + count + 1 > k: continue # <- 왜 이 줄이 없으면 아예 틀리지?
            if 1 <= nextX <= n and 1 <= nextY <= m and count < k:
                stack.append((nextX, nextY, count + 1, path + direction[v]))
                break
    return "impossible"

'''
# 테스트 4~8만 통과하는 코드 (나머지는 시간 초과)
import sys
sys.setrecursionlimit(5000)

def solution(n, m, x, y, r, c, k):
    # 변수 초기화
    dirX = [1, 0, 0, -1] # array[x][y] 일 때 d, l, r, u
    dirY = [0, -1, 1, 0]
    d = ["d", "l", "r", "u"]
    route = [] # 경로 저장 (스택)
    ans = "impossible"
    flag = False # 정답을 찾았는지 여부
    def go(nx, ny, nk):
        nonlocal flag
        if flag or nk < 0: return
        if nx == r and ny == c and nk == 0:
            nonlocal ans
            flag = True
            ans = "".join(route)
            return
        for v in range(4):
            if 1 <= nx + dirX[v] <= n and 1 <= ny + dirY[v] <= m:
                route.append(d[v])
                go(nx + dirX[v], ny + dirY[v], nk - 1)
                route.pop()
    go(x, y, k)
    return ans
'''


n, m, x, y, r, c, k = 3, 4, 2, 3, 3, 1, 5
result = solution(n, m, x, y, r, c, k)
print(result)
