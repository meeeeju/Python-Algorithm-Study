# 116824KB / 580ms
from sys import stdin
input = stdin.readline

# 입력받기
N = int(input())
home = []
for _ in range(N):
    home.append(list(map(int, input().split())))
stack = [(0,0,0,1)] # 파이프의 위치
ans = 0
while stack:
    x1,y1,x2,y2 = stack.pop()
    # if x1==y1==N-1 or x2==y2==N-1:
    if x2==y2==N-1:
        ans += 1
    if x1==x2: # 파이프가 가로
        nx1, ny1, nx2, ny2 = x1, y1+1, x2, y2+1
        if nx1<N and ny1<N and nx2<N and ny2<N and home[nx2][ny2]==0:
            stack.append((nx1, ny1, nx2, ny2))
        nx1, ny1, nx2, ny2 = x1, y1+1, x2+1, y2+1
        if nx1<N and ny1<N and nx2<N and ny2<N and home[nx2][ny2]==0 and home[nx2-1][ny2]==0 and home[nx2][ny2-1]==0:
            stack.append((nx1, ny1, nx2, ny2))
    elif y1==y2: # 파이프가 세로
        nx1, ny1, nx2, ny2 = x1+1, y1, x2+1, y2
        if nx1<N and ny1<N and nx2<N and ny2<N and home[nx2][ny2]==0:
            stack.append((nx1, ny1, nx2, ny2))
        nx1, ny1, nx2, ny2 = x1+1, y1, x2+1, y2+1
        if nx1<N and ny1<N and nx2<N and ny2<N and home[nx2][ny2]==0 and home[nx2-1][ny2]==0 and home[nx2][ny2-1]==0:
            stack.append((nx1, ny1, nx2, ny2))
    else: # 파이브가 대각선
        nx1, ny1, nx2, ny2 = x1+1, y1+1, x2, y2+1
        if nx1<N and ny1<N and nx2<N and ny2<N and home[nx2][ny2]==0:
            stack.append((nx1, ny1, nx2, ny2))
        nx1, ny1, nx2, ny2 = x1+1, y1+1, x2+1, y2
        if nx1<N and ny1<N and nx2<N and ny2<N and home[nx2][ny2]==0:
            stack.append((nx1, ny1, nx2, ny2))
        nx1, ny1, nx2, ny2 = x1+1, y1+1, x2+1, y2+1
        if nx1<N and ny1<N and nx2<N and ny2<N and home[nx2][ny2]==0 and home[nx2-1][ny2]==0 and home[nx2][ny2-1]==0:
            stack.append((nx1, ny1, nx2, ny2))
print(ans)