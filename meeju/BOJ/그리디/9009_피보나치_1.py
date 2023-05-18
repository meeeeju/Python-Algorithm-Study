# 	31256kb /68ms
import sys
input = sys.stdin.readline

def main():
    
    test_case = int(input()) # 4
    for _ in range(test_case):

        n = int(input()) # 100
        n_answer=[]
        k=1
        dp=[0,1]
        while True:
            x = dp[-1]+dp[-2]
            dp.append(x)
            if x > n :
                break

        while n >0:
            for i in range(len(dp)):
                if dp[i]>n:
                    k = i-1
                    break
            n_answer.append(dp[k])
            n -= dp[k]
        print(*n_answer[::-1])
        
main()