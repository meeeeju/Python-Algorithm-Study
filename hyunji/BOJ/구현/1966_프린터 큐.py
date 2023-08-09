#메모리 :31256 시간 :92
import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    liist=list(map(int,input().split()))
    printer=[]
    if n==1:
        print(1)
    else:
        for i in range(n):
            printer.append([i,liist[i]])
        count=0
        while True:
            maxx=0
            for i in range(len(printer)):
                if printer[i][1]>maxx:
                    maxx=printer[i][1]
            
            if printer[0][1]==maxx:
                count+=1
                #print(printer)
                if printer[0][0]==m:
                    print(count)
                    break
                else:
                    del printer[0]   
            else:
                printer.append(printer[0])
                del printer[0]


            
