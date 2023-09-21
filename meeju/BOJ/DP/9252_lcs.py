# 타입에러 멍밍,,,,역추적 유투브 참고
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

'''
ACAYKP
CAPCAK'''

str1= input().rstrip()
str2= input().rstrip()

dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
dp2 = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

# print(dp)
# print(str1,str2)

for i in range(len(str2)):
    if str2[i]==str1[0]:
        for k in range(i,len(str2)):
            dp[0][k]= 1
            dp2[0][k] = 1   # 대각선
        break
for i in range(len(str1)):
    if str1[i] == str2[0]:
        for k in range(i,len(str1)):
            dp[k][0] = 1
            dp2[k][0] = 1   # 대각선 
        break

# print(dp)

for i in range(1,len(str1)):  # 행이 str1
    for j in range(1,len(str2)):  # 열이 str2
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1]+1
            dp2[i][j] = 1   # 대각선
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i][j]= dp[i-1][j]
                dp2[i][j] = 2   # 위에서 
            else:
                dp[i][j] = dp[i][j-1]
                dp2[i][j] = 3 # 옆에서 
            


def go_back(i,j):

    if i <0 or j<0:
        return ""

    else:
        if dp2[i][j] == 1:
            return go_back(i-1,j-1) + str1[i]
        elif dp2[i][j] == 2:
            return go_back(i-1,j)
        elif dp2[i][j] == 3:
            return go_back(i,j-1)


result = go_back(len(str1)-1,len(str2)-1)
if result:
    print(len(result),result)
else:
    print(0)


            
