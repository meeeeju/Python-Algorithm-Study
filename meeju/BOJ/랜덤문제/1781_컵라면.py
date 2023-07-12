# 	60964	536
# 블로그 참고 (그리디)
import heapq
import sys
input = sys.stdin.readline

'''
7   # 숙제의 갯수
1 6 # 데드라인, 컵라면 수 
1 7
3 2
3 1
2 4
2 5
6 1'''
N = int(input())
problem_info = [0 for _ in range(N)]
for i in range(N):
    problem_info[i]= tuple(map(int,input().split()))
problem_info.sort()

queue = []


for deadline,noodle in problem_info:
    heapq.heappush(queue,noodle)
    if deadline < len(queue) :  # deadline 이 현재 단위 시간보다 빠르면 
        heapq.heappop(queue)
print(sum(queue))

