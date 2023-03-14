# 31256KB / 40ms

import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n : 달걀갯수 / # m : 고객수
p_list = []
for _ in range(m):
    p_list.append(int(input()))
p_list.sort(reverse=True)
price, profit = 0, 0 # 가격, 수익

for i in range(m):
    if i >= n:
        break
    if profit <= p_list[i]*(i+1):
        price = p_list[i]
        profit = p_list[i]*(i+1)

print(price, profit)