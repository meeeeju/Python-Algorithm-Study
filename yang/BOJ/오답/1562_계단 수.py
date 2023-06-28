# 38596KB / 140ms
def find(i, j, check):
    if mem[i][j][check] != -1:
        return mem[i][j][check]
    if i==N-1:
        if check==allChecked:
            mem[i][j][check] = 1
            return 1
        else:
            mem[i][j][check] = 0
            return 0
    
    mem[i][j][check] = 0
    if 0<=j-1:
        mem[i][j][check] += find(i+1, j-1, check|(1<<(10-j)))%MOD
    if j+1<10:
        mem[i][j][check] += find(i+1, j+1, check|(1<<(8-j)))%MOD
    return mem[i][j][check]%MOD


N = int(input())
if N < 10:
    print(0)
    exit()
allChecked = int('0b1111111111', 2)
MOD = 1000000000
mem = [[[-1]*(allChecked+1) for _ in range(10)] for _ in range(N)] # mem[i][j] : i번째 자리에서 j로 만들수 있는 계단수
ans = 0
for j in range(1, 10):
    check = 1<<(9-j)
    ans += find(0, j, check)
print(ans%MOD)