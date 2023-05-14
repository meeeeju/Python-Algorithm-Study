# 블로그 참고
# 32820KB / 76ms
N = input()
if "0" not in N:
    print("-1")
else:
    newN = sorted(N, reverse=True)[:-1] # 맨 마지막은 무조건 "0" => 0 뺌
    total = 0
    for i in newN: # 3의 배수 판별법 : 각 자리수의 합이 3의 배수
        total += int(i)
    if total % 3 == 0:
        print(''.join(newN)+'0')
    else:
        print("-1")

'''
# 처음엔 N이 10**5 이하로 잘못 이해해서 완탐되는줄 알고 백트래킹으로 풀었음
# 근데 N이 10**5 자리수 이하.. => 시간초과
import sys
sys.setrecursionlimit(10**6)
def dfs(stack: list):
    if len(stack) == len(N):
        number = int(''.join(stack))
        if number%3 == 0:
            print(number*10)
            return True
    for i in range(len(N)): # 백트래킹
        if not visited[i]:
            visited[i] = True
            stack.append(N[i])
            if dfs(stack):
                return True
            visited[i] = False
            stack.pop(i)

N = input()
if not "0" in N:
    print(-1)
else:
    N = sorted(N)[1:] # 맨 마지막은 무조건 "0" => 0 뺌
    visited = [False]*(len(N))
    if not dfs([]):
        print("-1")
'''
