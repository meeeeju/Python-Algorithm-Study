import sys
input = sys.stdin.readline

# electrics에 대한 visited 체크 => 비트연산자. 
# 1개에서부터 K개를 만들때까지 재귀호출.
def make_combi(count, combi_sum, visited):
    if count == K: return
    if mem[count][visited]:
        return mem[count][visited]
    mem[count][visited] = True
    for i in range(len(electrics)):
        if (1 << i) & visited == 0: # 방문 안함
            ans.add(combi_sum + electrics[i])
            make_combi(count + 1, combi_sum + electrics[i], visited | (1 << i))

N, K = map(int, input().split())
electrics = list(map(int, input().split()))
mem = [[False]*(K+1) for _ in range(100000)] # mem[count][visited]
ans = set()
make_combi(0, 0, 0)
print(len(ans))
print(*sorted(list(ans)))