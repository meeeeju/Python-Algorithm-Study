# 블로그 참고
# 212232KB / 29824ms
N = int(input())
queen = [-1] * N

def promising(r, q):
    for i in range(r):
        if queen[i] == q: return False
        if abs(queen[i]-q) == r-i: return False
    return True

def nqueen(row): # row에 queen 둘 차례
    if row == N:
        global ans
        ans += 1
        return
    for i in range(N):
        if promising(row, i):
            queen[row] = i
            nqueen(row+1)
            queen[row] = -1
    
ans = 0
nqueen(0)
print(ans)