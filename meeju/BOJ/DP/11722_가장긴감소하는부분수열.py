# 31256KB /	100ms
import sys
input = sys.stdin.readline


def main():

    N = int(input())    
    A = [0]+list(map(int,input().split()))

    dp = [1 for _ in range(N+1)]

    if N==1:
        print(1)
        return

    for i in range(2,N+1):

        for j in range(1,i):
            if A[i]<A[j]:
                dp[i]=max(dp[i],dp[j]+1)

    print(max(dp))
    return

main()