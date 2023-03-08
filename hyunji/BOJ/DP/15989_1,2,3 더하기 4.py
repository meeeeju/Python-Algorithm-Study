#메모리 :31256 시간 :44ms
import sys
input=sys.stdin.readline
T=int(input())
dp=[1 for _ in range(10001)]
liist=[]
dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=3
dp[4]=4
dp[5]=5

for i in range(T):
    n=int(input())
    liist.append(n)
for j in range(6,10001):
    dp[j]=dp[j-1]+dp[j-2]-dp[j-3]
    if j%3==0:
        dp[j]+=1
for n in liist:
    print(dp[n])
'''
T=int(input())

for i in range(T):
    n=int(input())
    n2=n//2
    n3=n//3
    n4=0
    
    if n3>1:
        if n-n3*3==2:
            if n3==1:
                n4=(n-3*1)//2
                print(n2+n3+n4+2)
            elif n3>1:
                for j in range(1,n3):
                    if n-j*3>1:
                        n4+=(n-j*3)//2
                        #print(n4)
                print(n2+n3+n4+2)
            else:
                print(n2+n3+2)
        else:
            if n3==1:
                n4=(n-3*1)//2
                print(n2+n3+n4+1)
            elif n3>1:
                for j in range(1,n3):
                    if n-j*3>1:
                        n4+=(n-j*3)//2
                        #print(n4)
                print(n2+n3+n4+1)
            else:
                print(n2+n3+1)
    else:
        print(n2+n3+1)'''
