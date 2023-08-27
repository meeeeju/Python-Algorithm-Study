# 53804	268
import sys
import heapq


input = sys.stdin.readline

# 다익스트라의 시간 복잡도 
# 갱신된 정점이라도 다시 갱신될 수 있지..?

'''
8 9
1 2 3
1 3 2
1 4 4
2 5 2
3 6 1
4 7 3
5 8 6
6 8 2
7 8 7
1 8'''

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s,t = map(int,input().split())

def dikstra():

    dis = [float('inf') for _ in range(n+1)]
    dis[s] = 0
    pq=[]

    heapq.heappush(pq,(0,s))

    while pq:

        dis_v ,v= heapq.heappop(pq)

        if dis_v > dis[v] : # 이미 갱신된거라서 볼 필요가 없다
            continue
        
        for  w, cost_v_w in graph[v]:
            if dis_v+ cost_v_w < dis[w]:
                dis[w] = dis_v+ cost_v_w
                heapq.heappush(pq,(dis[w],w))

                # if w == t :
                #     return dis[t]
    return dis[t]
                

print(dikstra())





