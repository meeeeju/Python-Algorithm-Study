# 40ms/ 33376KB
import sys
from math import gcd
        
tlist=[]
for _ in range(int(sys.stdin.readline())):
    tlist.clear()
    tlist = list(map(int,sys.stdin.readline().split())) # tlist에 t 입력받기
    total_gcd=0  # gcd 합 저장할 변수
    for i in range(1,len(tlist)):   # 이중배열 돌며 모든 쌍의 gcd 구하기
        for j in range(i+1,len(tlist)):
            total_gcd+=gcd(tlist[i],tlist[j])
   
    print(total_gcd)
