# 	31256kb/	44ms
import sys
input = sys.stdin.readline
'''
3 # 토핑 종류의 수 
12 2 # 도우의 가격  # 토핑의 가격 
200   # 도우의 열량
50   # 토핑1
300  # 토핑2
100  # 토핑 3'''


topping_num= int(input())

dough_price,topping_price = map(int,input().split())    
dough_cal = int(input())
topping_cal=[0 for _ in range(topping_num)]

max_pizza_cal_per = dough_cal//dough_price
pizza_cal = dough_cal


for i in range(topping_num):
    topping_cal[i]= int(input())

topping_cal.sort(reverse=True)   # 열량 높은 순으로 정렬

topping_cal= list(zip(topping_cal,[0 for _ in range(topping_num)]))

cnt =0

for i in range(topping_num):
    # if topping_cal[i][1]==1:
    #     continue

    # topping_cal[i][1]=1    # 사용 갯수 체크
    pizza_cal += topping_cal[i][0] 
    cnt +=1
    pizza_cal_per = pizza_cal // (dough_price + topping_price*cnt)

    max_pizza_cal_per  = max(max_pizza_cal_per,pizza_cal_per)


print(max_pizza_cal_per)
