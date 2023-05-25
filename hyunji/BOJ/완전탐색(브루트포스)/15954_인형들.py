#메모리 :298484 시간 :560
import sys
import math

input = sys.stdin.readline

n, k = map(int, input().split())
person = list(map(int, input().split()))
liist = []
liist2 = []


def var(liist):
    varr = 0
    average = sum(liist) / len(liist)
    for i in range(len(liist)):
        varr += (liist[i] - average) ** 2
    return varr / len(liist)


for i in range(k, n + 1):
    for j in range(n - i + 1):
        liist.append(person[j : j + i])

for i in range(len(liist)):
    liist2.append(math.sqrt(var(liist[i])))


liist2.sort()
print(liist2[0])
