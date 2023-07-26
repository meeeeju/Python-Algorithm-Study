#오ㅐ안되는지 몰게쑴,,
import sys
input=sys.stdin.readline

n=int(input())
liist=[]
maxx=0
for _ in range(n):
    liist.append(list(input().rstrip()))

def count_max(liist):
    maxx=1
    for i in range(n):
        count=1
        for j in range(1,n):
            if liist[i-1][j]==liist[i][j]:
                count+=1
            else:
                count=1
            maxx=max(count,maxx)
        count=1
        for i in range(1,n):
            if liist[i][j-1]==liist[i][j]:
                count+=1
            else:
                count=1
            maxx=max(count,maxx)
        #count=1
    return maxx 

for i in range(n):
    for j in range(n):
        if i+1<n:
            if liist[i][j]!=liist[i+1][j]:
                liist[i][j]=liist[i+1][j]
                liist[i+1][j]=liist[i][j]
                maxx=max(maxx,count_max(liist))
                liist[i+1][j]=liist[i][j]
                liist[i][j]=liist[i+1][j]
        if j+1<n:
            if liist[i][j]!=liist[i][j+1]:
                liist[i][j]=liist[i][j+1]
                liist[i][j+1]=liist[i][j]
                maxx=max(maxx,count_max(liist))
                liist[i][j+1]=liist[i][j]
                liist[i][j]=liist[i][j+1]

'''
for i in range(1,n):
    for j in range(1,n):
        if i<n:
            if liist[i-1][j]!=liist[i][j]:
                liist[i-1][j]=liist[i][j]
                liist[i][j]=liist[i-1][j]
                maxx=max(maxx,count_max(liist))
                liist[i][j]=liist[i-1][j]
                liist[i-1][j]=liist[i][j]
        if j<n:
            if liist[i][j-1]!=liist[i][j]:
                liist[i][j-1]=liist[i][j]
                liist[i][j]=liist[i][j-1]
                maxx=max(maxx,count_max(liist))
                liist[i][j]=liist[i][j-1]
                liist[i][j-1]=liist[i][j]
            
        '''
print(maxx)
