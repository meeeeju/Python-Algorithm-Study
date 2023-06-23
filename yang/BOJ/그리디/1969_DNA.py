# 31256KB / 68ms
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dnaList = []
for _ in range(N):
    dnaList.append(input().rstrip())

ansDNA = []
ansDistance = 0
for i in range(M):
    dnaCount = dict()
    maxCount = 0
    for j in range(N):
        if dnaList[j][i] not in dnaCount:
            dnaCount[dnaList[j][i]] = 0
        dnaCount[dnaList[j][i]] += 1
        maxCount = max(maxCount, dnaCount[dnaList[j][i]])
    ansDistance += N-maxCount
    for key, value in dnaCount.items():
        if value == maxCount:
            if len(ansDNA) <= i: ansDNA.append(key)
            else: ansDNA[i] = min(ansDNA[i], key)
print("".join(ansDNA))
print(ansDistance)