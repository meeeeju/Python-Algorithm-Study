# 31256KB / 48ms
from sys import stdin
sinput = stdin.readline

N, K = map(int, sinput().split())
country_info = [(-1, -1, -1)]*(N+1)
for _ in range(N):
    country, gold, sliver, bronze = map(int, sinput().split())
    country_info[country] = (gold, sliver, bronze)

rank = 0 # K보다 잘한 나라 수
for gold, sliver, bronze in country_info:
    if gold > country_info[K][0]:
        rank += 1
    elif gold == country_info[K][0]:
        if sliver > country_info[K][1]:
            rank += 1
        elif sliver==country_info[K][1]: 
            if bronze > country_info[K][2]:
                rank += 1

print(rank+1)