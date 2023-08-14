#메모리 :31256 시간 :44
from itertools import combinations
import sys
input=sys.stdin.readline
liist=[]
while True:
    string=list(map(int,input().split()))
    if string[0]==0:
        exit()
    else:
        for i in combinations(string[1:],6):
            print(*i)
    print()

