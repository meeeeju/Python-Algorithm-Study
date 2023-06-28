#BackJoon 1562 계단수
# 블로그 참고 ㅠ
# 39188 KB/1028 ms
import sys
MOD = 1000000000
N=int(sys.stdin.readline())
dp=[[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]
# bit_mast=[1<<0,1<<1,1<<2,1<<3,1<<4,1<<5,1<<6,1<<7,1<<8,1<<9]
for i in range(1,10):
    dp[1][i][1<<i]=1

for length in range(N): # 길이
    for last in range(10): # 마지막 자리의 숫자
        for bit in range(1024): # BITMASKING
            if last < 9 : 
                next_bit = bit | (1<<(last+1))
                dp[length+1][last+1][next_bit]+=dp[length][last][bit]
                dp[length+1][last+1][next_bit]%=MOD
            if last > 0 :
                next_bit = bit | (1<<(last-1))
                dp[length+1][last-1][next_bit]+=dp[length][last][bit]
                dp[length+1][last-1][next_bit]%=MOD

answer=0
for last in range(10):
    answer+=dp[N][last][1023]
    answer%=MOD
print(answer)
