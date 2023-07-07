# 31256KB / 48ms
n = int(input())
ansSet = set()
for x in range(n+1):
    for y in range(n-x+1):
        for z in range(n-x-y+1):
            ans = x + 5*y + 10*z + 50*(n-x-y-z)
            ansSet.add(ans)
print(len(ansSet))