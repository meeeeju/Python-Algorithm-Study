# 31120	5396
import sys
input = sys.stdin.readline

''''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0'''

N = int(input())
score_board = [0 for i in range(N)]
visited = [False for _ in range(N)]

result = float('inf')
for i in range(N):
    row = list(map(int,input().split()))
    score_board[i] = row

def dfs(k,index):
    global result
    
    if len(k) == N//2:
        
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += score_board[i][j]
                elif (not visited[i])and (not visited[j]):
                    link += score_board[i][j]
        result = min(abs(start-link),result)

        pass
    else:
        for i in range(index+1,N):
            if not visited[i]:
                visited[i] = True
                dfs(k+[i],i)
                visited[i] = False
            


dfs([],-1)
print(result)