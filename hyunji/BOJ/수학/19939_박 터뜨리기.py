#메모리 :31388 시간 :44
n,k=map(int,input().split())
def ball():
    liist=[]
    
    if n//k==1:
        for i in range(1,k+1):
            liist.append(i)
        if sum(liist)>n:
            return -1
        elif n-sum(liist)==k or sum(liist)==n:
            return liist[-1]-liist[0]
        else:
            for j in range(k-1,0,-1):
                liist[j]=liist[j]+1
            return liist[-1]-liist[0]
    else:
        summ=0
        for i in range(1,k):
            summ+=i
        if summ>n:
            return -1
        x=(n-summ)//k

        for i in range(k):
            liist.append(x+i)
        
        if n-sum(liist)==k or sum(liist)==n:
            return liist[-1]-liist[0]
        else:
            for j in range(k-1,0,-1):
                liist[j]=liist[j]+1
            return liist[-1]-liist[0]

print(ball())
