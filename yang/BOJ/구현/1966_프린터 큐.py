# 34140KB / 64ms
import sys
from collections import deque
input = sys.stdin.readline

def simulator(docs, n, m):
    indexedDocs = list(zip(docs, range(0, n)))
    sortedDocs = sorted(docs, reverse=True)
    sd = 0
    while sd < n:
        id = 0
        while id<len(indexedDocs):
            if sortedDocs[sd] == indexedDocs[id][0]:
                if indexedDocs[id][1] == m:
                    return sd
                indexedDocs.pop(id)
                sd += 1
            else :id += 1

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    print(simulator(docs, N, M)+1)