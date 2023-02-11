import sys
import math
input = sys.stdin.readline

# 3
# 6
# 20
# 100

def find_primeNumber(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i==0: # 소수가 아님
            return find_primeNumber(num+1)
    return num

testcase = int(input())
input_list = [0 for _ in range(testcase)]

for i in range(testcase):
    input_list[i] = int(input())
    if input_list[i]==0 or input_list[i]==1:
        input_list[i]=2

for number in input_list:
    print(find_primeNumber(number))

