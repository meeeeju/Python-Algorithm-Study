# 115560 KB/ 284 ms (pypy)
# 선아 코드 참고
'''
import sys
import numpy
input = sys.stdin.readline
N,K = map(int,input().split())
nlist = list(map(int,input().split()))
result = 1000000000000

for i in range(N):
    if i>N-K : break
    if i==N-K : result=min(result,numpy.std(nlist[i:]))
    else: result=min(result,numpy.std(nlist[i:i+K]))
print(result)
'''
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
nlist = list(map(int,input().split()))
result = float('inf')

for i1 in range(N): #시작점
    for i2 in range(i1+K-1,N): # 끝 점
        vsum=0
        mean = sum(nlist[i1:i2+1])/(i2-i1+1)
        for j in range(i1,i2+1):vsum+= (nlist[j]-mean)**2
        result=min(result,(vsum/(i2-i1+1)))
print(round(result**0.5,11))


