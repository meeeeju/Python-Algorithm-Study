#블로그 코드
import sys
input=sys.stdin.readline

for _ in range(int(input())):
    K=int(input())
    file_size=list(map(int,input().split()))
    d=[[0 for _  in range(K+1)] for _ in range(K+1)]
    
    for i in range(K-1):
        d[i][i+1]=file_size[i]+file_size[i+1]
        for j in range(i+2,K):
            d[i][j]=d[i][j-1]+file_size[j]
    
    for v in range(2,K):
        for i in range(K-v):
            j=i+v
            d[i][j] += min([d[i][k] + d[k+1][j] for k in range(i,j)])
    
    print(d[0][K-1])
    
'''
d[start][end] : start ~ end 까지의 최소합
'''
