# 31256KB / 120ms
# 계속 틀려서 비슷하게 푼 블로그 참고
# https://juintination.tistory.com/entry/%EB%B0%B1%EC%A4%80-11722%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
mem = [-1]*(N+1)
def sequence(idx):
    if mem[idx] == -1:
        for i in range(idx+1, N):
            if A[idx] > A[i]:
                mem[idx] = max(mem[idx], 1 + sequence(i))
        if mem[idx] == -1 : mem[idx] = 1
    return mem[idx]
ans = 0
for i in range(N):
    ans = max(ans, sequence(i))
print(ans)