# 블로그 참고 / 질문 게시판 참고
# 34400kb /	68ms

import sys
import math
input = sys.stdin.readline

'''
4 (지역)
120 110 140 150 (지역별 예산 요청)
485(한도)'''

def main():

    state_number= int(input())  # 지역 수 

    budget_request = list(map(int,input().split()))     # 각 지역별 예산 요청 금액
    budget = int(input())   # 예산

    
    if sum(budget_request) <= budget:  # 예산 요청 금액의 총 합이 예산 보다 작은 경우 
        print(max(budget_request))
        return

    # 예산보다 예산 요청 금액의 총 합이 큰 경우
    budget_request.sort()

    start = 0
    end = max(budget_request)
    result = 0
    while (start <= end):

        mid = (start + end )//2     # mid 가 상한액
        temporary_budget =0

        for i in range(state_number):   # 임시 예산의 총 합 구하기 (요청 금액이 mid 보다 크면 mid로 요청 금액 계산하기)
            temporary_budget += min(mid,budget_request[i])
        
        if budget >= temporary_budget:  # 예산이 임시 예산 총 합이 예산보다 크거나 같으면
            result = mid
            start = mid +1
        else:
            end = mid -1
    print(result)



main()