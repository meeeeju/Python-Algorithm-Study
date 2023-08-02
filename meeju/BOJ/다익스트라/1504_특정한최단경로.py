# 왜 틀린지 모르겠송 ,,,ㅠ2ㅠ
import sys
import heapq
input = sys.stdin.readline

'''
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3'''

N, E = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):

    a,b,c = map(int,input().split())
    graph[a].append((b,c))  # 튜플(정점, 거리)
    graph[b].append((a,c))

must_v1,must_v2 = map(int,input().split())


def dikstra(s,e):

    dis =[float('inf') for _ in range(N+1)]

    q = [(0,s)]
    dis[s]= 0 

    if s==e:
        return 0

    while q :
        cost, v = heapq.heappop(q)

        if v == e :
            return cost
        if cost > dis[v]:
            continue
        for w,w_cost in graph[v]:

            if dis[w] > dis[v]+ w_cost :
                dis[w] = dis[v]+w_cost
                heapq.heappush(q,(dis[w],w))
    return -1


def main():

    for w,dis_w in graph[must_v1]:
        if w == must_v2:
            must_dis = dis_w
            break
    else:
        print(-1)
        return 
    

    path11 = dikstra(1,must_v1)
    path12 = dikstra(must_v2,N)

    path21 = dikstra(1,must_v2)
    path22 = dikstra(must_v1,N)

    if path11 >= 0 and path12 >= 0 :
        case1 = path11 + path12 + must_dis
    else:
        case1 = float('inf')
    if path21 >= 0 and path22 >= 0 :
        case2 = path21 + path22 + must_dis
    else:
        case2 = float('inf')
        
    result = min(case1,case2)
    if result >= float('inf') :
        print(-1)
    else:
        print(result)

main()