#메모리 :31256 시간 :48
n,m=map(int,input().split())
count=1

def night(n,m):
    if n==1:
        return 1
    elif n==2:
        if m>=7:
            return 4
        else:
            return (1+(m-1)//2)
    else:
        if m>=7:
            return (5+(m-7))
        elif 5<=m<=6:
            return 4
        else:
            return m

print(night(n,m))
