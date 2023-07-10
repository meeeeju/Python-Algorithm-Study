# 31256 KB / 44 ms
from itertools import combinations_with_replacement # 중복조합
N = int(input())
count=0
isit=set()
for cwr in combinations_with_replacement([1,5,10,50],N): 
    if not sum(cwr) in isit : # 합이 isit에 존재하지 않을 때 추가
        count+=1
        isit.add(sum(cwr))
print(count)
