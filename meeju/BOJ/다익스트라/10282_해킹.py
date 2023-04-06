# 48684kb /	768ms

import sys
import heapq
input = sys.stdin.readline


'''
2
3 2 2
2 1 5
3 2 5
3 3 1
2 1 2
3 1 8
3 2 4'''

def dijkstra(start):
    count = 1 # 감염된 컴퓨터의 수 
    q = []
    heapq.heappush(q,(0,start)) # 시작 노드 정보 우선순위 큐에 삽입
    while q:
        dis, node = heapq.heappop(q)

        if disTo[node] < dis:   # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경부 ( = 방문한 셈 ) 무시
            continue
        for next in graph[node]:
            cost = disTo[node] + next[1]    # cost = next 까지의 거리
            if cost < disTo[next[0]]:
                disTo[next[0]] = cost
                count += 1
                heapq.heappush(q,(cost,next[0]))
    return count

# testcase = int(input())
INF = float("inf")

for _ in range(int(input())):
    n,d,c = map(int,input().split())  # n : 컴퓨터 갯수 , d : 의존성 갯수 , c : 해킹당한 컴퓨터의 번호

    graph = [ [] for _ in range(n+1)]
    disTo = [INF] * (n+1)
    edgeTo = [ None] * (n+1)
    disTo[c]=0

    for i  in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s)) # b에서 a 로 가는 전염 시간은 s 만큼 걸림

    dijkstra(c)

    result = []

    for i in disTo:
        if i < INF:
            result.append(i)

    print(len(result),max(result))



# virus_cnt = n- 1-disTo.count(INF)
# print(virus_cnt , max(disTo),sep=' ')
# print(disTo)


