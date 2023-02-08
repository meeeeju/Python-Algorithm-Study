#블로그 참조
S=input()
T=input()
count=0

array=[[0]*(len(T)+1) for _ in range(len(S)+1)]

for i in range(1,len(S)+1):
    for j in range(1, len(T)+1):
        if S[i-1]==T[j-1]:
            array[i][j]=array[i-1][j-1]+1
            count=max(array[i][j],count)
print(count)