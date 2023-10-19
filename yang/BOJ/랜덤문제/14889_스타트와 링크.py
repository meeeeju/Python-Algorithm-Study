# 31120KB / 4136ms (Python3)
# 119704KB / 1744ms (PyPy3)
import sys
input = sys.stdin.readline

def find_combi(x): # 모든 조합 구하기
    if len(team)==N//2:
        status = calcul_status(set(team))
        global ans
        ans = min(ans, status)
        return
    for i in range(x, N):
        team.append(i)
        find_combi(i+1)
        team.pop()

def calcul_status(combi): # 능력치 최솟값 구하기
    start = 0
    link = 0
    for i in range(N):
        for j in range(i+1, N): # Sij 점수 구하기
            if i in combi and j in combi:
                start += S[i][j] + S[j][i]
            elif i not in combi and j not in combi:
                link += S[i][j] + S[j][i]
    return abs(start-link)

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

# 경우의 수 찾기
combi_list = []
team = []
ans = float('inf')
find_combi(0)
print(ans)