#메모리 :40316 시간 :124
from collections import deque
s=int(input())
q=deque()
q.append((1,0))
visited=dict()
visited[(1,0)]=0

while q:
    a,b=q.popleft()
    if a==s:
        print(visited[(a,b)])
        break
    
    if (a,a) not in visited.keys(): #이모티콘 모두 복사
        visited[(a,a)]=visited[(a,b)]+1
        q.append((a,a))
    if (a+b,b) not in visited.keys(): #클립보드 이모티콘 복붙
        visited[(a+b,b)]=visited[(a,b)]+1
        q.append((a+b,b))
    if (a-1,b) not in visited.keys(): #이모티콘 하나 삭제
        visited[(a-1,b)]=visited[(a,b)]+1
        q.append((a-1,b))
