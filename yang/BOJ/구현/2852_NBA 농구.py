# 31256KB / 40ms
import sys
input = sys.stdin.readline
N = int(input())        

team1_score, team2_score = 0, 0
team1_time, team2_time = 0, 0
before = 0 # 이전에 이기고 있던 사람 : 0이면 무승부, 1이면 team1, 2이면 team2
last_time = 0 # 마지막에 승부가 결정된 시간

for _ in range(N):
    team, time = input().rstrip().split()
    minute, second = map(int, time.split(":"))
    time = minute*60 + second
    if team == "1": team1_score += 1
    else: team2_score += 1
    
    if team1_score > team2_score:
        if before == 0: # 무승부였다가 team1이 이김
            last_time = time
        elif before == 2: # team2가 이기다가 team1이 이김
            team2_time += time - last_time
            last_time = time
        before = 1
    elif team1_score < team2_score :
        if before == 0: # 무승부였다가 team2가 이김
            last_time = time
        elif before == 1: # team1이 이기다가 team2가 이김
            team1_time += time - last_time
            last_time = time
        before = 2
    else: # 무승부일때
        if before == 1:
            team1_time += time - last_time
            
        elif before == 2:
            team2_time += time - last_time
        before = 0

if before == 1:
    team1_time += 48*60 - last_time
elif before == 2:
    team2_time += 48*60 - last_time

print(f"{team1_time//60:02}:{team1_time%60:02}")
print(f"{team2_time//60:02}:{team2_time%60:02}")