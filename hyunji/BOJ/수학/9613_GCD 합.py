#메모리 : 31256 시간 : 44ms
T=int(input())
liist=[]
def GCD(n,k):
   
    for i in range(n,0,-1):
        if n%i==0:
            if k%i==0:
                return i

for i in range(T):
    liist=list(map(int,input().split()))
    N=liist[0]
    liist=sorted(liist[1:])
    summ=0
    for j in range(N-1):
        for m in range(j+1,N):
            summ+=GCD(liist[j],liist[m])
    print(summ)
