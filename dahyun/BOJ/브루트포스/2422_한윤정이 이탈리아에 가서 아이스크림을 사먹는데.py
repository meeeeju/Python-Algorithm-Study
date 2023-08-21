#31932KB/	288ms
#선아 코드 참고 - for구문의 i+1, j+1 범위 참고
import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # N은 아이스크림 종류의 수이고, M은 섞어먹으면 안 되는 조합의 개수
no=[set() for _ in range(N+1)]
result=0
for i in range(M):
    a,b = map(int,input().split())
    no[a].add(b)
    no[b].add(a)

for i in range(1,N+1):  # 첫번째 선택
    for j in range(i+1,N+1): # 두번째 선택
        if i in no[j] or j in no[i]: continue  # 첫번째 선택이 j와 맛없는 조합인지 확인
        for k in range(j+1,N+1): # 세번째 선택
            if k in no[i] or k in no[j]: continue # 마지막 선택이 첫번째 선택, 두번째 선택과 맛없는 조합인지 확인
            result+=1
print(result)

