# 44480KB / 232ms
import sys
input = sys.stdin.readline

N = int(input())
extensionsDict = {}
for _ in range(N):
    name, extension = input().rstrip().split('.')
    if extension not in extensionsDict:
        extensionsDict[extension] = 0
    extensionsDict[extension] += 1
ans = sorted(extensionsDict.items(), key=lambda k:k[0])
for e, c in ans:
    print(e, c)