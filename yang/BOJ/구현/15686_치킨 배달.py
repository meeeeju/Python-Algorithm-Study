# 31256KB / 388ms
from sys import stdin
sinput = stdin.readline

def combination(chickens, M):
    def recur(s):
        if len(combi) == M:
            combi_result.append(combi.copy())
            return
        for i in range(s, len(chickens)):
            combi.append(chickens[i])
            recur(i+1)
            combi.pop()
    combi_result = []
    combi = []
    recur(0)
    return combi_result

def cal_distance(chicken, homes):
    chicken_distance = 0
    for h in homes:
        home_distance = float('inf')
        for c in chicken:
            home_distance = min(home_distance, abs(h[0]-c[0])+abs(h[1]-c[1]))
        chicken_distance += home_distance
    return chicken_distance
def solution():
    N, M = map(int, sinput().split())
    homes = []
    chickens = []
    for row in range(N):
        row_list = list(map(int, sinput().split()))
        for col in range(len(row_list)):
            if row_list[col]==0: continue
            elif row_list[col]==1: homes.append((row, col))
            else : chickens.append((row, col))
    ans = float('inf')
    combi_list = combination(chickens, M)
    for combi in combi_list:
        ans = min(ans, cal_distance(combi, homes))
    print(ans)
solution()