# 시간 : 40ms / 메모리 : 31256KB
import sys
input = sys.stdin.readline

def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a

t = int(input())
for _ in range(t):
    case = list(map(int, input().split()))
    gcdSum = 0
    for i in range(1, case[0]+1):
        for j in range(i+1, case[0]+1):
            gcdSum += gcd(case[i], case[j])
    print(gcdSum)