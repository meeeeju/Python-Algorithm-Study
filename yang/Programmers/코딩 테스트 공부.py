# 2개 case 시간초과 남..

from heapq import heappush, heappop

def solution(alp, cop, problems):
    n = len(problems)
    maxAlp, maxCop = alp, cop
    for i in range(n):
        maxAlp = max(maxAlp, problems[i][0])
        maxCop = max(maxCop, problems[i][1])
    visited = [[100000]*500 for _ in range(500)]
    pq = [(0,alp,cop)]
    visited[alp][cop] = 0
    while pq:
        time, alp, cop = heappop(pq)
        if alp >= maxAlp and cop >= maxCop:
            return time
        if visited[alp+1][cop] > time+1:
            heappush(pq, (time+1, alp+1, cop))
            visited[alp+1][cop] = time+1
        if visited[alp][cop+1] > time+1:
            heappush(pq, (time+1, alp, cop+1))
            visited[alp][cop+1] = time+1
        for i in range(n):
            if problems[i][0]<=alp and problems[i][1]<=cop: # 풀 수 있는 문제
                if visited[alp+problems[i][2]][cop+problems[i][3]] > time+problems[i][4]:
                    heappush(pq, (time+problems[i][4], alp+problems[i][2], cop+problems[i][3]))
                    visited[alp+problems[i][2]][cop+problems[i][3]] = time+problems[i][4]
            #elif problems[i][0]>alp: break
    return -1