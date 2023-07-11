#블로그 참고
n=int(input())
liist=[]
while n:
    if n&1:
        liist.append('[/]')
        n*=2
    elif n&2:
        liist.append('[+]')
        n-=2
    else:
        liist.append('[*]')
        n//=2
if len(liist)>99:
    print("-1")
else:
    print(len(liist))
    print(''.join(liist[::-1]))
