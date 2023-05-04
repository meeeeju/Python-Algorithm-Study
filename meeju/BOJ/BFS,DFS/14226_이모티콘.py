# 39052kb /	7624ms
import sys
from queue import Queue
input = sys.stdin.readline

'''
화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
화면에 있는 이모티콘 중 하나를 삭제한다.'''

S  = int(input())

def bfs(S):

    # display = 0     # 화면
    # clipboard = 0      # 클립보드
    
    q = Queue()
    q.put((1,0,0))    # (화면 , 클립보드, 시간 )
    visited= [(1,0)]

    while q.qsize() > 0 :

        now = q.get()

        if now[0] == S :
            return now[2]
        
        # 1. 클립보드에 화면 이모티콘 복사
        if (now[0]  > 0):
            if not (now[0],now[0]) in visited:
                q.put((now[0],now[0],now[2]+1))
                visited.append((now[0],now[0]))
                
        # 화면에 클립보드 이모티콘 붙여넣기
        if now[1] > 0 :
            temp = now[0] + now[1]
            if temp == S :
                return now[2]+1
            if not (temp,now[1]) in visited :
                q.put((temp,now[1],now[2]+1))
                visited.append((temp,now[1]))

        # 화면에 임의로 한개 삭제하기 
        if now[0]-1 > 0 :
            if not (now[0]-1,now[1]) in visited :
                if now[0]-1 == S:
                    return now[2]+1
                q.put((now[0]-1,now[1],now[2]+1))
                visited.append((now[0]-1,now[1]))

print(bfs(S))       
        