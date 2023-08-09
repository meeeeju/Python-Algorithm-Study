#메모리 :129512 시간 :808
from itertools import combinations
k=int(input())

def choco():
    for i in range(100):
        if 2**i>=k:
            break
    return i

number=choco()
chocolate=2**choco()

def cut():
    global number
    global chocolate
    count=[]
    liist=[]
    minn=1e8
    mini=1e8
    answer=0
    for i in range(number+1):
        liist.append(2**i)
    
    if k==chocolate:
        return 0
    else:
        for i in range(number+1):
            count=list(combinations(liist,i))
            for j in range(len(count)):
                if sum(count[j])==k:
                    if len(count[j])<minn:
                        minn=len(count[j])
                        mini=min(count[j])
                        
        for i in range(number+1):
            if mini==2**i:
                answer=number-i
        
        return answer
print(chocolate,cut())
