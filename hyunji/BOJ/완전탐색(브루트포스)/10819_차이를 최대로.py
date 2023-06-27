#메모리 :35692 #시간 :148
from itertools import permutations
n=int(input())
liist=list(map(int,input().split()))
liist2=list(permutations(liist,n))
maxx=0

for i in range(len(liist2)):
    summ=0
    for j in range(1,n):
        summ+=abs(liist2[i][j-1]-liist2[i][j])
    if summ>maxx:
        maxx=summ
print(maxx)
