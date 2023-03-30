#시간 출력 방식 찾아봄
#메모리 :31256 시간 :60ms
import sys
input=sys.stdin.readline

N=int(input())
count1=0
count2=0
k_mm,k_ss=0,0
team1,team2=0,0
win=0
alltime=48*60

for i in range(N):
    team,time=input().split()
    mm,ss=map(int,time.split(':'))
    if N==1:
        if team=='1':
            team1=alltime-(60*mm+ss)
            
        else:
            team2=alltime-(60*mm+ss)
            
    else:
        if team=='1':
            count1+=1
        else:
            count2+=1

        if count1>count2:
            if win==0:
                k_mm,k_ss=mm,ss
            win=1
        elif count1<count2:
            if win==0:
                k_mm,k_ss=mm,ss
            win=2
        else:
            if win==1:
                team1+=(mm*60+ss)-(k_mm*60+k_ss) 
            elif win==2:
                team2+=(mm*60+ss)-(k_mm*60+k_ss)  
            win=0
if win==1:
    team1+=alltime-(k_mm*60+k_ss)
elif win==2:
    team2+=alltime-(k_mm*60+k_ss)
print('{:0>2}:{:0>2}'.format((team1)//60, (team1)%60))
print('{:0>2}:{:0>2}'.format((team2)//60, (team2)%60))              
