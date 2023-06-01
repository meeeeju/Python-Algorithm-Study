import sys
input=sys.stdin.readline

n, k, p, x = map(int, input().split())
numdigital = [
    [1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1],
]

count = 0
x = list(map(int, str(x).zfill(k)))
liist = []
for i in range(n + 1):
    num = str(i).zfill(k)
    liist.append(list(map(int, str(num))))

for i in range(len(liist)):
    flag = 0
    for j in range(k):
        if liist[i][j] != x[j]:
            for m in range(7):
                if numdigital[liist[i][j]][m] != numdigital[x[j]][m]:
                    flag += 1
    if flag <= p:
        count += 1


print(count - 1)
