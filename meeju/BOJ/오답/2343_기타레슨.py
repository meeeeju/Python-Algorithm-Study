import sys

# 이진 탐색 문제

'''
input : N 강의의 수 M 블루레이의 갯수
9 3
1 2 3 4 5 6 7 8 9

output : 가능한 블루레이의 최소 크기
17
'''

N, M = map(int,input().split())
course = list(map(int,input().split()))

min_size = max(course)
max_size = sum(course)

while max_size >= min_size:

    size = (min_size + max_size )//2

    temp = 0
    m = 1
    for i in range(N):
        temp += course[i]
        if temp > size:
            m +=1
            temp = course[i]
    if m > M :
        min_size = size + 1
    else:
        max_size = size -1
 
print(min_size)
    
        




