# 35500KB / 124ms
import sys
input = sys.stdin.readline

n = int(input())
lope = []
for _ in range(n):
    lope.append(int(input()))
lope.sort(reverse=True)
ans = lope[0]
for i in range(n):
    ans = max(ans, lope[i]*(i+1))

print(ans)
