#블로그 참고..했지만 이해가 잘안됨 쩝

N=int(input())
liist=[]

while N:
    if N&1:
        liist.append('[/]')
        N*=2
    elif N&2:
        liist.append('[+]')
        N-=2
    else:
        liist.append('[*]')
        N//=2
print(len(liist))
print(' '.join(liist[::-1]))
