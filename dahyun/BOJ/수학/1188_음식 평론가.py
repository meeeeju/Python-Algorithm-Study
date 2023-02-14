#블로그 참고
#33508KB / 44ms
import sys
import math
N,M = map(int,sys.stdin.readline().split())

if N>=M and N%M==0 : print(0)
else : print(M-math.gcd(N,M))
