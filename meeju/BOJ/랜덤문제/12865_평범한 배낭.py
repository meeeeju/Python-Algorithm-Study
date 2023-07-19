# 블로그 참조 
# 0-1 knapsack problem
import heapq
import sys
'''
4 7 N(물품의 수) K(버틸 수 있는 가방의 무게)
6 13 W V
4 8
3 6
5 12


물건의 가치의 최댓값
'''

    
n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))  # (6kg , 13가치)

for i in range(1, n+1): # 현재 담을라고 하는 물건
    for j in range(1, k+1): 
        w = thing[i][0]
        v = thing[i][1]

        if j < w:   # 현재 담을라고 하는 물건의 무게가 한도 무게(j)를 초과하는 경우
            d[i][j] = d[i-1][j]
        else:       # 현재 담을라고 하는 물건의 무게(w)가 한도 무게(j)보다 작거나 같은 경우
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])