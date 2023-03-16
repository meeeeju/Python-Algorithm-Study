#66736KB /	256ms

import sys
input = sys.stdin.readline
'''
5 3 # N명 K 조 
1 3 5 6 10  # 아이들의 키
''' 


N,k = map(int,input().split())
height = list(map(int,input().split()))


if N ==k:   # 조의 갯수와 전체 학생수가 같은 경우
    print(0)
else:

    min_cost = height[-1]-height[0]     # 최소 비용 초기화 
    adj_cost = [0 for _ in range(N-1)]  # 인접 비용

    for i in range(N-1):
        adj_cost[i]=height[i+1]-height[i]

    adj_cost.sort(reverse=True)
    min_cost -= sum(adj_cost[0:k-1])


    print(min_cost)
        
