# 31256KB / 44ms
import sys
input = sys.stdin.readline

n = int(input())
time = [0]*(n)
price = [0]*(n)
for i in range(n):
    time[i], price[i] = map(int, input().split())

mem = [0]*(n+1)
for i in range(n):
    next = i+time[i]
    for k in range(next, n+1):
        mem[k] = max(mem[i]+price[i], mem[k])
print(max(mem))