#combination 함수 찾아봄
#메모리 :31256 시간 :40ms

import sys
input=sys.stdin.readline
from itertools import combinations
L,C=map(int,input().split())
password=list(map(str,input().split()))

liist=set()
vowel=('a','e','i','o','u')
vow=[]
con=[]

for pw in password:
    if pw in vowel:
        vow.append(pw)
    else:
        con.append(pw)

for i in range(1,len(vow)+1):
    if L-i<2:
        break
    vo=list(combinations(vow,i))
    co=list(combinations(con,L-i))

    for v in vo:
        for c in co:
            liist.add("".join(sorted(v+c)))
liist=sorted(liist)
for i in liist:
    print(i)
