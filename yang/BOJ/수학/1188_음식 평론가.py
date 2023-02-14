# 40ms / 31256KB
# 블로그 참고
def gcd(a,b):
    while b>0:
        a, b = b, a%b
    return a
n, m = map(int, input().split())
a = gcd(n,m)
print(m-a)