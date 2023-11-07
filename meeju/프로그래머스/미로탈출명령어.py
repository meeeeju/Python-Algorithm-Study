from collections import deque
# https://cheon2308.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv3-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-%EB%AA%85%EB%A0%B9%EC%96%B4
# https://dhalsdl12.tistory.com/284
def solution(n, m, x, y, r, c, k):
    
    result = []
    maps = [[0 for i in range(m)] for _ in range(n)]
    maps[x-1][y-1]=1
    maps[r-1][c-1]=2
    
    q= deque()
    q.append((x-1,y-1,0,''))
    
    dx = [1,0,0,-1] # 행
    dy = [0,-1,1,0] # 열
    dict_dir = {0:'d',1:'l',2:'r',3:'u'} # d l r u 
    
    # 거르기 : 최단 거리보다 k가 작거나 (k-최단거리)가 홀수인 경우
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    cnt = 0 
    while q:
        now = q.popleft()

        if maps[now[0]][now[1]]==2: # 목표 지점 도착할 시 
            if now[2] == k:
                result = now[3]
                break
            elif (k-now[2])%2==1:
                result = 'impossible'
                break
        for i in range(4):  # 목표 지점 
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue 
            re_distance = abs(nx-r+1)+abs(ny-c+1)+now[2]+1
            if re_distance > k:
                continue
            temp = now[3]+ dict_dir[i]
            q.append((nx,ny,now[2]+1,temp))
    return result

print(solution(3,4,2,3,3,1,5))



''' # 블로그 코드
# 조건문 이해 안 됨
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dAlpha = ['d', 'l', 'r', 'u']
answer = "z"


def isVaild(nx, ny, n, m):
    return 1 <= nx and nx <= n and 1 <= ny and ny <= m


def dfs(n, m, x, y, r, c, prev_s, cnt, k):
    global answer
    if k < cnt + abs(x - r) + abs(y - c):   # 조건문 이해 안 됨
        return
    if x == r and y == c and cnt == k:
        answer = prev_s
        return
    for i in range(4):
        if isVaild(x + dx[i], y + dy[i], n, m) and prev_s < answer:
            dfs(n, m, x + dx[i], y + dy[i], r, c, prev_s+dAlpha[i], cnt + 1, k)


def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    dfs(n, m, x, y, r, c, "", 0, k)

    return answer'''
