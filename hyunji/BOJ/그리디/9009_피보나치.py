#왜틀리는지 모르겠음,,,,,,ㅠ
import sys
input = sys.stdin.readline
t = int(input())


def fibonacci():
    liist = [0, 1]

    for i in range(2, 43):
        liist.append(liist[i - 1] + liist[i - 2])

    liist.sort(reverse=True)
    return liist


for i in range(t):
    n = int(input())
    fibo = []
    for j in fibonacci():
        if n >= j:
            fibo.append(j)
            n -= j
        if n == 0:
            break
        # fibo.sort(reverse=True)
    print(*sorted(fibo))
    
