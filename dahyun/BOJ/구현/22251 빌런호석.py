# 31256 KB / 884 ms
def check():
    for i in range(10):
        for j in range(i+1,10):
            count=0
            for k in range(7): # 7개를 모두 확인하며 숫자가 다른 것의 개수 구하기 => 반전시켜야할 개수
                if LED[i][k]!=LED[j][k]: count+=1
            dif[i][j]=count;dif[j][i]=count;
def dfs(index,num,count): # index : 변경될 숫자의 인덱스 값 , num : 이때까지 변경된 수 (문자열) , count : 반전된 개수
    global result
    for j in range(10):  # 0~9까지 수
        temp = int(num[:index]+str(j)+num[index+1:])
        # 마지막 인덱스가 아니고, 바뀐 개수가 P를 넘지 않을 때  ,, 바뀐 개수 = 이전에 바뀐 숫자(count)와 이번에 바꿀 숫자 개수(dif[int(num[index])][j])의 합
        if index+1<K and count+dif[int(num[index])][j]<=P: dfs(index+1,num[:index]+str(j)+num[index+1:],count+dif[int(num[index])][j])
        # 마지막 인덱스이고, 바뀐 개수가 1~P 사이 값이고, 바뀌어진 수가 0~N일 때 결과로 추가
        elif index+1>=K and 0<count+dif[int(num[index])][j]<=P and 0<temp<=N: result+=1;

# 0~9 LED 표시
LED=[[1,1,1,0,1,1,1],[0,0,1,0,0,1,0],[1,0,1,1,1,0,1],[1,0,1,1,0,1,1],[0,1,1,1,0,1,0],[1,1,0,1,0,1,1],[1,1,0,1,1,1,1],[1,0,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]
# 숫자가 바뀌기 위해 반전시켜야할 LED 수
dif=[[0 for _ in range(10)] for _ in range(10)]
check()

result=0
N,K,P,X = map(int,input().split())
display = '' 
# K개수에 맞게 재조정 
for i in range(K-len(str(X))): display+='0'  
display+=str(X)

dfs(0,display,0)
print(result)

