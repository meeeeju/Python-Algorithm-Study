# 블로그 참고 ㅡㅡ


'''3
1 3
2 5
3 3'''
import math
import sys
input = sys.stdin.readline

N = int(input())

village_info = [0 for _ in range(N)]
all_people = 0
for i in range(N):
    village_info[i] = list(map(int,input().split()))
    all_people +=village_info[i][1]

village_info.sort()
count = 0

for i in range(N):
    count +=village_info[i][1]
    if count >= (math.ceil(all_people/2)): 
        print(village_info[i][0])
        break




