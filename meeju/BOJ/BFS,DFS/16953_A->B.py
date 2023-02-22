# 31256KB /	40ms
import sys
input = sys.stdin.readline

''''
2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
'''

A,B = map(int,input().split())
count = 0

while(B >= A):
    if B == A :
        break

    if (str(B)[-1:] == "1") :   # 끝 자리수가 1인 경우
        B = int(str(B)[:-1])
        count += 1
    else:                       
        if not (B % 2):     # 짝수로 나누어떨어지는 경우
            B = B//2
            count +=1
        else:
            break
# 결과 출력
if  (A==B): 
    print(count +1)
else:
    print(-1)

