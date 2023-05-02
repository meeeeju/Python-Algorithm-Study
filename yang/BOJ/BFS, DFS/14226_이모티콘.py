# 51988KB / 740ms
from heapq import heappop, heappush
S = int(input())
# S >=2 이기 때문에 1회 복사, 1회 붙여넣기까지는 필수
pq = [(2, 2, 1)] # 정답, 이모티콘 개수, 클립보드의 이모티콘 개수
visited = [False]*2001
while pq:
    ans, count, clipBoard = heappop(pq)
    if count == S :
        print(ans)
        break
    visited[count] = True
    if count*2 <= 2000 and not visited[count*2]:
        heappush(pq, (ans+2, count*2, count)) # 복붙
    if count+clipBoard <= 2000 and not visited[count+clipBoard]:
        heappush(pq, (ans+1, count+clipBoard, clipBoard)) # 붙
    if count-1 >= 2 and not visited[count-1]:
        heappush(pq, (ans+1, count-1, clipBoard)) # 삭제
