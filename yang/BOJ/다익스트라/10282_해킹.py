# 49072KB / 972ms
# 시간초과나서 블로그 참고
# https://hillier.tistory.com/56
import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    computer = [[] for _ in range(N+1)]
    for _ in range(D):
        a, b, s = map(int, input().split())
        computer[b].append((a, s)) # 의존컴퓨터, 시간
    
    time = 0
    next_time = 1001
    visited = [-1] * (N+1)
    visited[C] = 0
    infection = [(0, C)] # 정렬을 위해 시간, 컴퓨터 순으로 저장
    while infection:
        it, ic = heapq.heappop(infection)
        for c, t in computer[ic]:
            if visited[c]==-1 or visited[c]>it+t:
                visited[c] = it+t
                heapq.heappush(infection, (it+t, c))
    count = 0
    for i in visited:
        if i != -1:
            count += 1
    print(f"{count} {max(visited)}")