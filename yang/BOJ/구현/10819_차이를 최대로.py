# 31256KB / 132ms
import sys
input = sys.stdin.readline

def find(turn):
    if turn == N:
        global answer
        test = 0
        temp = array[debug[0]]
        for i in range(1, N):
            temp -= array[debug[i]]
            test += abs(temp)
            temp = array[debug[i]]
        answer = max(answer, test)
        # print(test, debug)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            debug.append(i)
            find(turn+1)
            debug.pop()
            visited[i] = False
    return

N = int(input())
array = list(map(int, input().split()))
answer = 0
visited = [False]*N
debug = []
find(0)
print(answer)