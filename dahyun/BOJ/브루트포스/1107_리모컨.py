#BaekJoon 1107 리모컨
#게시판 반례 모두 돌아가는데 계속 틀리거나 시간초과나서 ... 블로그 참고
# 31256 KB / 780 ms
import sys
def find():
        total=N
        for i in range(1000000): # i : 이동하는 숫자
            if i>(abs(100-N)): return (abs(100-N)) # 임의의 수에서 N 만큼 이동하는 수(i) 보다 100에서 N만큼 이동하는 수가 더 작으면 리턴
            a=list(str(total+i)) 
            b=list(str(total-i))
            a_num,b_num=0,0
            if 0<=total+i and 0<=total-i:  # 임의의 수에서 N 만큼 이동하는 수를 구함 (1) N+i  (2) N-i
                for j in range(max(len(a),len(b))):
                    if a_num>0 and b_num>0 : break
                    if len(a)>j and int(a[j]) in breakdown: a_num+=1  # N+i 인덱스에 고장난 번호가 포함되어 있으면 a_num 증가
                    if len(b)>j and int(b[j]) in breakdown: b_num+=1  # N-i 인덱스에 고장난 번호가 포함되어 있으면 b_num 증가
            elif 0<=total+i : # (1) N+i
                b_num+=1
                for j in str(total+i):
                    if int(j) in breakdown: 
                        a_num+=1
                        break
            elif 0<=total-i: # (2) N-i
                a_num+=1
                for j in str(total-i):
                    if int(j) in breakdown:
                        b_num+=1
                        break
            if a_num==0 and b_num==0 : return min(abs(100-N),i+len(b),i+len(a))
            elif a_num==0 : return min(abs(100-N),i+len(a))
            elif b_num==0 : return min(abs(100-N),i+len(b))
            
        
N=int(sys.stdin.readline())  #이동하려는 채널
M=int(sys.stdin.readline())  #고장난 버튼 수
breakdown=list(map(int,sys.stdin.readline().split())) # 고장난 버튼 리스트
if N==100: print(0)
else : print(find())
