# 80ms / 31256KB
def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a
N = int(input())
nList = list(map(int, input().split()))
M = int(input())
mList = list(map(int, input().split()))
A, B = 1, 1
for i in nList:
    A *= i
for i in mList:
    B *= i
ans = gcd(A, B)
if ans // 1000000000 >= 1:
    ans = str(ans % 1000000000)
    ans = "0"*(9-len(ans))+ans
    print(ans)
else:
    print(ans)