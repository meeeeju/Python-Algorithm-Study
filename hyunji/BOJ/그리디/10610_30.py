#메모리 :32388 시간 :80
N=input()
summ=0

if '0' not in N:
    print(-1)
else:
    maxx=sorted(N,reverse=True)
    for i in maxx:
        summ+=int(i)
    if summ%3==0:
        print(''.join(maxx))
    else:
        print(-1)
