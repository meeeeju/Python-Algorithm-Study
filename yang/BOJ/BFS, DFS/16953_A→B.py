# 31256KB / 40ms
A, B = map(int, input().split())
count = 0
while A < B:
    if B%10 == 1:
        B = B//10
    elif B%2 == 0:
        B = B//2
    else:
        break
    count += 1

if A == B:
    print(count+1)
else:
    print(-1)
