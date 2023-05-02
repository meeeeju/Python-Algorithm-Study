# 40284 KB / 136 ms
from collections import deque
def bfs():
    queue = deque()
    queue.append((1,0,0))
    visited=[[False for _ in range(1001)] for _ in range(1001)]  # [이모티콘 수][클립보드 이모티콘 수]
    visited[1][0]=True
    while queue:
        count,time,clipboard=queue.popleft()  # count : 이모티콘 수 , time : 시간 , clipboard : 클립보드에 저장된 이모티콘 수
        if count+clipboard==S or count-1 == S: return time+1  # 붙여넣기 했을 때나, 하나 삭제했을 때 S랑 개수가 같다면 time+1 리턴
        
        queue.append((count,time+1,count))  # 복사
        if clipboard!=0 and 0<count+clipboard<=1000 and not visited[count+clipboard][clipboard]:  # 붙여넣기
            visited[count+clipboard][clipboard]=True
            queue.append((count+clipboard,time+1,clipboard))
        if 0<count-1<=1000 and not visited[count-1][clipboard]: # 삭제
            visited[count-1][clipboard]=True
            queue.append((count-1,time+1,clipboard))
            
S = int(input())
print(bfs())

