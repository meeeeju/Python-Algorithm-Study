# 블로그 참고  - 2차원  다익스트라
import sys, heapq

# 입력부
n,m,k = map(int, sys.stdin.readline().split()) # n : 도시의 수 , m : 도로 , k : 포장할 도로 개수
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
    
# inf : 임의의 무한대값
inf = 98765432109876543210

# d : 2차원 다익스트라 배열. 현재 정점 i에서 포장을 j개 했을 때 드는 최소거리
d = [[inf] * (k + 1) for _ in range(n + 1)]
q = []
for i in range(k + 1): # 정점 1까지는 포장을 할 필요 없음 -> 0
    d[1][i] = 0
heapq.heappush(q, (0,1,0))  # 현재 시간, 현재 정점, 포장 개수

# 다익스트라 
while q:
    now_dist, now, p = heapq.heappop(q)  # 현재 시간, 현재 정점, 포장 개수
    if d[now][p] < now_dist:  # 현재 정점에서 p개의 도로를 포장했을 때 시간 < 현재 시간 -> 더 볼 필요 없음
        continue
    # 현재 정점에서 포장이 가능한 경우
    if p + 1 <= k:
        for (next, next_dist) in adj[now]:  # next : 다음 정점 , next_dist : 다음 정점까지 시간
            if d[next][p + 1] > now_dist:  # 도로를 포장한 것이니까 현재 시간(now_dist)만 저장함
                d[next][p + 1] = now_dist
                heapq.heappush(q, (now_dist, next, p + 1))
                
    # 기본적으로 포장을 하지 않는 경우
    for (next, next_dist) in adj[now]:
        if d[next][p] > now_dist + next_dist:  # 도로를 포장하지 않았으니까, 현재 시간(now_dist)와 다음 정점까지의 시간(next_dist)의 합 저장
            d[next][p] = now_dist + next_dist
            heapq.heappush(q, (now_dist + next_dist, next, p))
            
# 정답 출력
ans = inf
for i in range(k + 1):
    ans = min(ans, d[n][i])
print(ans)
