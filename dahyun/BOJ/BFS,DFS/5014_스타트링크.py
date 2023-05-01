# 92248 KB / 1708 ms  - heapq
# 40528 KB / 620 ms  - deque
# import heapq
# def bfs():
#     queue = [(abs(S-G),S,0)]
#     visited=[False for _ in range(1000001)]
#     while queue:
#         dif,now,count = heapq.heappop(queue)
#         if now==G: return count
#         if now+U<=F and not visited[now+U] :
#             visited[now+U]=True
#             heapq.heappush(queue,(abs(S-(now+U)),now+U,count+1))
#         if now-D>0 and not visited[now-D] :
#             visited[now-D]=True
#             heapq.heappush(queue,(abs(S-(now-D)),now-D,count+1))
#     return "use the stairs"   
from collections import deque 
def bfs():
    queue = deque()
    queue.append((S,0))
    visited=[False for _ in range(1000001)]
    while queue:
        now,count = queue.popleft()
        if now==G: return count   # now와 G가 같다면 count 리턴
        if now+U<=F and not visited[now+U] :  # 위로 올라갔을 때의 층을 방문하지 않았고, 최대높이보다 작은 층일 때
            visited[now+U]=True
            queue.append((now+U,count+1))
        if now-D>0 and not visited[now-D] :  # 아래로 내려갔을 때의 층을 방문하지 않았고, 0층보다 높은 층일 때
            visited[now-D]=True
            queue.append((now-D,count+1))
    return "use the stairs"      # 엘레베이터로 갈 수 있는 모든 층을 보아도 G로 갈 수 없을 때 리턴
F,S,G,U,D = map(int,input().split())
print(bfs())
