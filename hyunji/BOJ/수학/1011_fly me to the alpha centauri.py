#문제 이해를 잘못함 ㅠ
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if y-x==1:
        print(1)
        
    elif y-x==2:
        print(2)
        
    else:
        y=y-x-1
        x=1
        jump=1
        count=0
        i=1
        
        while jump<=y:
            if jump+i+1>y:
                break
            i+=1
            jump+=i
            
        #print(i)
        if jump==y:
            print(i+1)
        else:
            print(i+2)

