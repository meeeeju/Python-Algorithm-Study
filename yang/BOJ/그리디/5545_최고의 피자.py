# 31256KB / 40ms
import sys
input = sys.stdin.readline
N = int(input()) # 토핑종류의 수
A, B = map(int, input().split()) # 도우의 가격, 토핑의 가격
C = int(input()) # 도우의 열량
D_list = [] # 각 토핑의 열량
for _ in range(N):
    D_list.append(int(input()))
D_list.sort(reverse=True)
best_pizza = C//A
calory_sum = C
for i in range(N):
    calory_sum += D_list[i]
    pizza = calory_sum//(A+B*(i+1))
    if best_pizza <= pizza:
        best_pizza = pizza
    else:
        break
print(best_pizza)