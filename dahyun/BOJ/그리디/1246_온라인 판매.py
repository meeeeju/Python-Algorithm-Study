# 31256 KB / 40 ms
import sys
input=sys.stdin.readline
N,M = map(int,input().split())
customer_list=[int(input()) for i in range(M)]
customer_list.sort(reverse=True) # 고객 리스트 내림차 순으로 정렬
max_money=0  # 가장 큰 수익
pay=0  # 판매 가격
for i in range(M): # 고객 수만큼 반복문 돌리기 : 고객 리스트 값 하나씩 보기 위해서 
    if i+1>N: break  # 판매할 수 있는 달걀 수를 초과하면 종료
    if max_money<((i+1)*customer_list[i]) : # 고객 리스트 값 * 판매 가능한 달걀 수
        max_money=(i+1)*customer_list[i]
        pay=customer_list[i]
print(pay,max_money)

