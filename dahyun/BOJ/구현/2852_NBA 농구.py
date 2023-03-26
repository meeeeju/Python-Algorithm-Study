# 31256 KB / 40 ms
import sys
N=int(sys.stdin.readline()) 
score1,score2=0,0  # 점수
beforeTime =0 # 이전 시간
totaltime1, totaltime2 = 0,0 # 이긴 시간
lock1,lock2=0,0 # 어디 팀이 이기고 있는지 판별하기 위해
for i in range(N):
    winner , t = map(str,sys.stdin.readline().split())
    temp_time=t.split(":")
    time=int(temp_time[0])*60+int(temp_time[1]) # 초로 계산
    if winner=='1':   # 1팀이 이겼을 때
        if lock2==0 and lock1==0: # 이전에 이기고 있던 팀이 없다면,
            lock1=1    # lock1을 1 : 1팀이 이기고 있다고 표현
            beforeTime=time  # 이때 이기기 시작하였을 때 시간을 beforeTime에 저장해놓음
        score1+=1
    else : 
        if lock1==0 and lock2==0: 
            lock2=1
            beforeTime=time
        score2+=1
    if score1==score2:   # 1팀과 2팀의 점수가 동일할 때,
        if lock1==1 : totaltime1+=(time-beforeTime)  # 이전에 1팀이 이기고 있었다면 1팀 승리시간 증가 (현재 시간 - 이기기 시작한 시간)
        else : totaltime2+=(time-beforeTime)
        lock1,lock2=0,0  # 동점이 되었으므로, 이기고 있는 팀이 없다는 것을 나타내기 위해 lock1과 lock2 0으로 초기화
    elif i==N-1 :  # 동일하지 않고, 종료 직전일 경우, 남은 시간은 모두 현재 이기고 있던 팀이 계속 이기는 것이므로
        if lock1==1 : totaltime1+=(48*60)-beforeTime  # 총 경기 시간 (40분) - 이기기 시작한 시간
        else : totaltime2+=(48*60)-beforeTime
    
# print(str(totaltime1//60).zfill(2),":",str(totaltime1%60).zfill(2))
# print(str(totaltime2//60).zfill(2),":",str(totaltime2%60).zfill(2))

print(f"{totaltime1//60:02}:{totaltime1%60:02}")
print(f"{totaltime2//60:02}:{totaltime2%60:02}")
