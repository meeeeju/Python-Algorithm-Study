# 2376ms / 31256KB
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    ans = 2 if n<2 else n
    while True:
        for i in range(2, int(ans**0.5)+1):
            if ans % i == 0:
                ans += 1
                break
        else:
            print(ans)
            break