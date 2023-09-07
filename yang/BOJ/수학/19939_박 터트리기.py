# 98% 에서 틀림
from sys import stdin
sinput = stdin.readline
N, K = map(int, sinput().split())

if N<sum(range(1, K)):
    print("-1")
else:
    ans = K-1
    if N%K != 0: 
        if K==2 and N%2==1:
            pass
        else:
            ans += 1
    print(ans)