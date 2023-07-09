#메모리 :31256 시간 :48
import sys
input=sys.stdin.readline
from itertools import combinations_with_replacement
n=int(input())
summ=0
liist=[]
def romma(n):
    global summ
    for i in combinations_with_replacement([1,5,10,50], n):
        summ+=sum(i)
        if summ not in liist:
            liist.append(summ)
        summ=0
    return len(liist)
print(romma(n))
