#31256KB/	336ms
import sys
from itertools import combinations, permutations
input = sys.stdin.readline

def calculate(store):  
    ans=0  
    for hi,hj in home:  # 모든 집  hi,hj
        semi_ans=100000000
        for si,sj in store:  # 치킨 집 위치 si,sj
            semi_ans=min(semi_ans,abs(hi-si)+abs(hj-sj))  # semi_ans : 하나의 집에 대해 가장 가까운 치킨 거리 구하기
        ans+= semi_ans
    return ans
    
N,M = map(int,input().split())
chicken = []  # 치킨 집 위치
home = [] # 집 위치
for i in range(N):
    t = list(map(int,input().split()))
    for j in range(N):
        if t[j]==1: home.append((i,j))  # 집 위치 저장
        elif t[j]==2: chicken.append((i,j))  # 치킨집 위치 저장
        
store_chicken = list(combinations(chicken,M)) # 치킨집들을 조합으로 M만큼 뽑아내기

result=100000000  # 도시의 치킨 거리 

for i in range(len(store_chicken)):  # M개만큼 뽑은 치킨집
    result = min(result,calculate(store_chicken[i]))  # i번째 조합이 가장 작은 도시의 치킨 거리를 가지는 지 확인
print(result)
    
