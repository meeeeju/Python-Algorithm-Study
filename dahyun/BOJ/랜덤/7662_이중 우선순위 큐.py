#블로그코드 참고 - 최소힙구하는건 알겠는데 최대힙은 진짜 하나하나 다 수동으로 구해야하나 싶어서 블로그봤엉
import sys
input = sys.stdin.readline
import heapq
for _ in range(int(input())):
    k = int(input())
    maxh,minh=[],[]
    visited = [False] * k
    for i in range(k):
        cal,N = map(str,input().split())
        N=int(N)
        if cal=='I':
            heapq.heappush(minh,(N,i))
            heapq.heappush(maxh,(-N,i))
            visited[i]=True
        elif N==1:
            while maxh and not visited[maxh[0][1]]: # i 번째 값이 최솟값에서 빠졌을 수도 있으니까 확인
                heapq.heappop(maxh)
            if maxh:  # 최댓값 빼주기
                visited[maxh[0][1]] = False  # 최솟값에도 해당 값이 저장되어있으므로 visited[]=False
                heapq.heappop(maxh)
        else:
            while minh and not visited[minh[0][1]]: # i 번째 값이 최댓값에서 빠졌을 수도 있으니까 확인
                heapq.heappop(minh)
            if maxh: # 최솟값 빼주기
                visited[minh[0][1]] = False # 최댓값에도 해당 값이 저장되어있으므로 visited[]=False
                heapq.heappop(minh)
        # 마지막까지 최대힙, 최소힙 모두 한번 더 확인
        while minh and not visited[minh[0][1]]:
            heapq.heappop(minh)
        while maxh and not visited[maxh[0][1]]:
            heapq.heappop(maxh)
        print(-maxh[0][0], minh[0][0]) if maxh and minh else print("EMPTY") 
            
