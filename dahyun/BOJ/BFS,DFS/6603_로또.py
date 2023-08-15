#31256KB/ 48ms
import sys
input = sys.stdin.readline
from itertools import combinations 

while(True):
    nlist = list(map(int,input().split()))
    if nlist[0]==0: break
    for llist in combinations(nlist[1:],6):
        print(*llist)
    print()
