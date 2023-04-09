# 31256KB / 40ms
def solve():
    S = input()
    N = len(S)
    count = 0
    p = N-1
    while p >= 0:
        if S[p:N] == S[p:N][::-1]: # S[N-1:p-1:-1] 이거 안됨 ㅠ
            count = N+p
        p-=1
    return count
    
print(solve())