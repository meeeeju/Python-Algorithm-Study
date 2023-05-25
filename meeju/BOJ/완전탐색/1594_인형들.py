# 블로그 참고 
# 문제 이해 잘 못 함 ;; 완전 탐색 해주면 끝나는 일, 너무 어렵게 생각함;;

'''
5 3 N  
1 2 3 4 5'''  

import sys
import math
input = sys.stdin.readline

n, K = map(int,input().split()) #  n : 인형의 종류 K : 연속된 minimum 
preference = list(map(int,input().split() )) # 인형이 일렬로 나열된 순서대로 인형을 선호하는 사람의 수


def distribute(m, list):
    result = 0
    for i in list:
        result += (i-m)**2
    return result/len(list)

resultCandidate = list()
for i in range(0,n-K+1): # 0  부터 n-k 까지
    for j in range(n-K-i+2):    # 범위 설정 잘 모르겠음 
        tmp = preference[i:i + K + j]
        m = sum(tmp) / len(tmp)
        dis = distribute(m, tmp)
        resultCandidate.append(dis)
result = min(resultCandidate)
print(math.sqrt(result))