#개허무함....
#메모리 :53788 시간 :132ms
import sys
input=sys.stdin.readline
N=int(input())
liist=list(map(int,input().split()))
'''
liist2=[]

if len(liist)<=2:
    print(min(liist))
else:
    house=0
    for i in range(len(liist)):
        house=liist[i]
        minn=0
        for j in range(len(liist)):
            minn+=abs(house-liist[j])
        liist2.append((house,minn))
    #liist2.sort(key=lambda x:x[1])
    
    a,b=min(liist2,key=lambda x:x[1])
    print(a)'''
if len(liist)<=2:
    print(min(liist))
else:
    liist.sort()
    if N%2==0:
        i=N//2-1
        print(liist[i])
    else:
        i=N//2
        print(liist[i])
