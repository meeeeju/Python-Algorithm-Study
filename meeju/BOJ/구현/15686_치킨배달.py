# 치킨 배달 블로그 참고
import sys
from itertools import combinations
input = sys.stdin.readline

# 가능한 조합의 수를 구한다
# 조합마다의 거리 계산해주기
# 시간 복잡도 의문점 : M 이 13개보다 작거나 같음 / M <= 치킨 집의 갯수 <= 13
# 백트래킹으로 조합 구할시, 시간 복잡도 : 13C12


'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2'''

def backtrack_comb(idx, arr):
    if len(arr)==m:
        combi.append(arr)
        return 

    for i in range(idx+1, len(chick)):
        if used[i]==False:
            used[i] = True
            backtrack_comb(i, arr+[chick[i]])
            used[i] = False


n, m = map(int, input().split())     
city = list(list(map(int, input().split())) for _ in range(n))
result = 999999
house = []      # 집의 좌표
chick = []      # 치킨집의 좌표
combi = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chick.append([i, j])
used = [False for i in range(len(chick))]

backtrack_comb(-1,[])

# print(combi)

for chi in combi:  # m개의 치킨집 선택한 조합들을 하나씩 꺼내보기
    temp = 0            # 도시의 치킨 거리
    for h in house: 
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):  # 치킨집은 m개 가질 수 있음
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result = min(result, temp)


# for chi in combinations(chick, m):  # m개의 치킨집 선택한 조합들을 하나씩 꺼내보기
#     temp = 0            # 도시의 치킨 거리
#     for h in house: 
#         chi_len = 999   # 각 집마다 치킨 거리
#         for j in range(m):  # 치킨집은 m개 가질 수 있음
#             chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
#         temp += chi_len
#     result = min(result, temp)

print(result)
