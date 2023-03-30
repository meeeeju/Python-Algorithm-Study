# 틀린 코드
import sys
input = sys.stdin.readline

'''
3 ( 총 득점 갯수)
1 01:10
2 21:10
2 31:30'''

def calculate(time):    # 초, 시간 계산해주는 함수

    start_time =time[1]
    end_time=time[2]
    second = 0
    minute= 0

    if end_time[1]<start_time[1]:
        second = end_time[1]+60 - start_time[1]
        end_time[0]-=1
    else:
        second = end_time[1]-start_time[1]
    
    minute=end_time[0] - start_time[0]
    return (minute,second)

all = int(input())  # 골이 들어간 횟수
goal_info = [0 for _ in range(all)]  # 득점 정보
goal_time=[]    # 득점 시간

for i in range(all):
    team, time = input().rstrip().split()
    time = time.split(":")
    time = list(map(int,time))
    goal_info[i]= (team,time)

team_one = 0    # 팀 1의 현재 score
team_two = 0    # 팀 2의 현재 score
two_flag = 0
one_flag = 0

for i in range(all):
    if goal_info[i][0] == '1' :   # 1번팀이 이긴 경우
        team_one +=1
        if team_one > team_two and not(one_flag):
            one_start_time = goal_info[i][1]
            one_flag = 1
            if i == all-1:
                goal_time.append(('1',one_start_time,[48,0]))
        if team_one == team_two:
            two_end_time = goal_info[i][1]
            goal_time.append(('2',two_start_time,two_end_time))
            two_flag = 0
    else:                        # 2번 팀이 이긴 경우
        team_two +=1
        if team_two > team_one and (not two_flag) :
            two_start_time = goal_info[i][1]
            two_flag =1
            if i == all-1:
                goal_time.append(('2',two_start_time,[48,0]))
        if team_one == team_two :
            one_end_time = goal_info[i][1]
            goal_time.append(('1',one_start_time,one_end_time))
            one_flag = 0

one_minute=0
one_second=0
two_minute = 0
two_second = 0

for i in goal_time:
    if i[0]=='1':
        one = calculate(i)
        one_minute += one[0]
        one_second += one[1]
    else:
        two = calculate(i)
        two_minute += two[0]
        two_second += two[1]


print("{0:02d}:{1:02d}".format(one_minute,one_second))
print("{0:02d}:{1:02d}".format(two_minute,two_second))
