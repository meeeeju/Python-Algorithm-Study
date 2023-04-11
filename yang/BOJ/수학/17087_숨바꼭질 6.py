# 42172KB / 96ms
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
N, S = map(int, input().split())
A = list(map(int, input().split()))
aa = [abs(A[i]-S) for i in range(N)]
d = aa[0]
for a in aa:
    d = gcd(d, a)
print(d)