# 34140 KB / 68 ms
# 블로그 참고 - 내가 생각한 방식과 같았는데, 계속 틀려서 확인했웅 ㅠ
import sys
input = sys.stdin.readline
from collections import deque
def bfs():
    queue=deque()
    queue.append((home[0],home[1])) # 좌표(x,y)
    while queue:
        x,y = queue.popleft()
        if abs(x-festival[0])+abs(y-festival[1])<=1000:return True # 패스티벌까지의 거리차이가 1000이하면 True
        else: 
            for i in range(n):  # 남은 편의점 위치를 다 확인
                if not visited[i]:
                 nx,ny = convenience_store[i][0],convenience_store[i][1] # 편의점 위치
                 if abs(x-nx)+abs(y-ny)<=1000: # 현재위치에서 편의점위치까지 1000이하면 queue에 추가
                     queue.append((nx,ny))
                     visited[i]= True
                    
    return False # 모든 갈 수 있는 거리 봤지만 True가 아니면 False
for _ in range(int(input())):
    n=int(input())
    home = tuple(map(int,input().split())) # 상근이네집 x,y
    convenience_store = []
    for _ in range(n):
        convenience_store.append(tuple(map(int,input().split()))) # 편의점 x,y
    festival= tuple(map(int,input().split())) # 패스티벌 x,y
    visited=[False for _ in range(n+1)]
    if bfs(): print("happy")
    else: print("sad")

