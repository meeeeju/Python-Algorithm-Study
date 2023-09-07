#메모리 :31256 시간 :92
n,k=map(int,input().split())
liist=[]
for _ in range(n):
    nation,gold,silver,bronze=map(int,input().split())
    liist.append([nation,gold,silver,bronze])
liist=sorted(liist,key=lambda x:(-x[1],-x[2],-x[3]))


liist[0].append(1)
#print(liist)
a,b,c=liist[0][1],liist[0][2],liist[0][3]
for i in range(1,n):
    if liist[i][1]==a and liist[i][2]==b and liist[i][3]==c:
        liist[i].append(liist[i-1][4])
        
    else:
        liist[i].append(i+1)
    a,b,c=liist[i][1],liist[i][2],liist[i][3]
    
liist=sorted(liist,key=lambda x:(x[0]))
print(liist[k-1][4])
