# 32276 KB / 180 ms
import sys
sys.setrecursionlimit(10000000)
def dfs(index,numbers):  # index : 부등호 인덱스 , numbers : 구한 문자열
    if index>=K: result.append(numbers);return  # 부등호 인덱스가 부등호 개수와 같거나 크면, 값 저장 후, return
    for i in range(10):
        if not str(i) in numbers:
            if (klist[index]=='>' and int(numbers[-1])>i) or (klist[index]=='<' and int(numbers[-1])<i): # 문제에서 제시한 조건에 성립하면
                dfs(index+1,numbers+str(i))
    return
K=int(input())
klist=input().strip()
klist = klist.split()  # 부등호 공백 제거
result=[]  # 모든 결과 값 담을 list
for i in range(10):  # 0~9 시작 값
    dfs(0,str(i))
result.sort()  # 정렬
print(result[-1])  # 최댓값
print(result[0])   # 최솟값


    
