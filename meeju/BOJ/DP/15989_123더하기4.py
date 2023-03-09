import sys
input = sys.stdin.readline


'''
3 # 테스트 케이스
4
7
10'''

def number_of_method(a):
    return a

T = int(input())
test_num = [None for _ in range(T)]

for i in range(T):
    test_num[i]= int(input())
    #print(number_of_method(int(input())))

max_num = max(test_num)
dp = [ 0 for _ in range(test_num+1)]
dp[1]=1 # (1)
dp[2]=1 # (1+1)
dp[3]=2 # (1+1+1, 1+2)
dp[4]=4
dp[5]=5
dp[6]=7


for i in range(7,max+1):
    a= dp[i-1]
    if i-2 ==3 or i-2 ==2:
        b= 1
    else:
        b= dp[i-2] -dp[i-3]
    if 
        
        or i-2 ==3:

    b= dp[i-2]-dp[i-3]
    c= dp[i-3]-(dp[i-4]+dp[i-5])







