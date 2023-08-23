#블로그 참고
#메모리 :31256 시간 :392
import sys
input=sys.stdin.readline
from itertools import combinations
n,m=map(int,input().split())
icecream=[]
cant=[[True for _ in range(n)]for _ in range(n)]
liist=[]
count=0

for _ in range(m):
    a,b=map(int,input().split())
    cant[a-1][b-1]=False
    cant[b-1][a-1]=False
    
'''
for i in range(1,n+1):
    liist.append(i)
icecream=list(combinations(liist,3))'''

for i in combinations(range(n),3):
    if not cant[i[0]][i[1]] or not cant[i[0]][i[2]] or not cant[i[1]][i[2]]:
        continue
    count+=1
print(count)
'''
#그래프 만들어서 풀려고 했음
for _ in range(m):
    a,b=map(int,input().split())
    liist.append([a,b])
    cant[a].append(b)
    cant[b].append(a)

for i in range(1,n+1):
    icecream.append(i)

#print(cant)
for i in range(1,n+1):
    icecream2=[]
    icecream2=[x for x in icecream if x not in cant[i]]
    icecream2.remove(i)
    for j in range(m):
        if liist[j][0] in icecream2 and liist[j][1] in icecream2:
            icecream2.remove(liist[j][0])
            icecream2.remove()

    #combination=list(combinations(icecream2,2))
    #print(i,combination)

'''
