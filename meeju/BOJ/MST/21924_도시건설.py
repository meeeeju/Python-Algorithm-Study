# 	166756	3108
import sys
import heapq
input = sys.stdin.readline


def mstPrimLazy():
    def include(v):
        included[v] = True
        for w in info_graph[v]:
            if not included[w[1]]: heapq.heappush(pq,w) #새 정점 w와 인접한 간선 중 MST 외부와만 연결하는 간선 pq에 추가하기 위함

    edgesInMST = [] # MST에 포함될 간선 저장
    included = [False] * (N+1) # 만약 정점 v가 MST에 포함되어 있으면 included[v]=True
    weightSum = 0  # MST 간선 비용 합  
    pq=[]
    # pq = heapq() # Build a priority queue
    include(1)

    while pq and len(edgesInMST) <= N-1:
        e = heapq.heappop(pq)

        if included[e[1]]: continue # Ignore the edge v-w if both v and w are included in the MST #v와 w 둘다 mst 상에 있으면 이 간선 무시하기 위함
        edgesInMST.append(e)
        weightSum +=e[0]
        include(e[1])
    
    for i in range(1,N+1):
        if not included[i]:
            return -1
    
    return weightSum    

"""
N: 정점의 개수 (1번 ~ N번)
M: 간선의 개수
adj_mat: 그래프의 인접 행렬
"""
N, M = map(int, input().split()) # N : 건물의 갯수 , M : 도로의 갯수
info_graph = [[] for _ in range(N+1)]
Allcost = 0

for _ in range(M):
    v,w,cost = map(int,input().split())
    info_graph[v].append((cost,w))
    info_graph[w].append((cost,v))
    Allcost+=cost

# 1번 정점에서 탐색을 시작
result = mstPrimLazy()
if result == -1:
    print(-1)
else:
    print(Allcost-result)


''' # 크루스칼 알고리즘
import sys2
input = sys.stdin.readline
 
def find(c):
	if par[c] == c:
		return c
	else:
		par[c] = find(par[c])
	return par[c]
 
def union(a, b):
	a, b = find(a), find(b)
	par[max(a,b)] = min(a,b)
 
def check(a, b):
	return find(a) == find(b)
 
N, M = map(int,input().split())
par = [i for i in range(N+1)]
build = []
total_cost = 0
for _ in range(M):
    a, b, c = map(int,input().split())
    build.append((c, a, b))
    total_cost += c
build.sort()
 
cost = 0
for c, a, b in build:
    if not check(a, b):
        cost += c
        union(a, b)
 
tmp = 0
for i in range(1, N+1):
    if par[i] == i:
        tmp += 1
 
if tmp >= 2:
    print(-1)
else:
    print(total_cost - cost)'''
