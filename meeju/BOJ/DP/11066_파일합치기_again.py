# 실패 ^^ i 에서 j 를 구하는데에서 막혔따,,,
import sys
import copy
input = sys.stdin.readline


'''
2   T
4   K (장의 수 )
40 30 30 50
15 
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32'''

# 혼자 풀어본 코드 
'''
T= int(input())

for _ in range(T):
    K = int(input())
    chapter_list=[0]+list(map(int,input().split()))
    prefix =[0 for _ in range(K+1)]

    dp = copy.deepcopy(chapter_list)

    for i in range(K+1): # prefix 구하기
        prefix[i]=chapter_list[i]+prefix[i-1]
    print(prefix)

    for i in range(2,K+1):
        for j in range(1,i):
            if dp[i] == chapter_list[i]:
                dp[i]=dp[i]-prefix[j]+dp[j]+ +prefix[i]
            dp[i]=min(dp[i],2*prefix[i]-prefix[j]+dp[j])
    print(dp)
'''


def solve(k,file_size):

    # S[i]는 1장부터 i장까지의 합 ex) S[3] : 1장, 2장, 3장 파일 크기의 합
    S = [0 for _ in range(k+1)]
    for i in range(1, k+1):
        S[i] = S[i-1] + file_size[i]

    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용 -> DP[1][N] : 1장에서 N장까지 합치는데 필요한 비용
    # DP[i][k] + DP[k+1][j] + sum(file_size[i]~file_size[j])
    DP = [[0 for i in range(k+1)] for _ in range(k+1)]
    for i in range(2, k+1): # 부분 파일의 길이
        for j in range(1, k+2-i):   # 시작점
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1])

    print(DP[1][k])


T = int(input())    # 테스트 케이스

for _ in range(T):
    k = int(input())    # 장의 수
    file_size = [0]+list(map(int,input().split()))  #  각 파일의 크기를 담아 놓은 리스트

    solve(k,file_size)

