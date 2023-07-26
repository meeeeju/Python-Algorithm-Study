# 시간 초과,,
import sys
'''
강의의 갯수 N
강의 번호, 강의 시작 시간, 강의 종료

8
6 15 21
7 20 25
1 3 8
3 2 14
8 6 27
2 7 13
4 12 18
5 6 20'''

# 15486 퇴사2, 1931 회의실 배정

N = int(input())
course = []
is_value = [ False for _ in range(N+1)]
min_place =1

for i in range(N):
    num, start, end = map(int,input().split())
    course.append((num,start,end))

course.sort(key=lambda x: x[1])
course.sort(key=lambda x: x[2])


for i in range(N):
    if not is_value[course[i][0]]: # 아직 방문 안했다면
        end = course[i][2]
        is_value[course[i][0]]=True
        min_place +=1
    
        for j in range(1,len(course)):
            if course[j][1] < end:
                continue
            if not is_value[course[j][0]]:
                end= course[j][2]
                is_value[course[j][0]] = True
    


print(min_place-1)