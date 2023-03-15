import sys
input = sys.stdin.readline

N,M = map(int,input().split()) # N : 달걀 수 M : 고객
price = [0 for _ in range(M)]
profit= 0

for i in range(M):
    price[i]=int(input())
price.sort(reverse=True)


for i in range(M):
    limit_price = price[i]
    temp =0
    for j in range(M):
        if j >= N:   # 준비한 달걀을 모두 소진한 경우 (M >= N)
            break
        if price[j] >=limit_price:
            temp += limit_price
    if temp > profit :
        profit = temp   # 수익 
        max_price = limit_price # 책정 가격
    
            
print(max_price,profit)