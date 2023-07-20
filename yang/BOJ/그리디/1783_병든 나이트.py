# 31388KB / 44ms
n, m = map(int, input().split())
if n==1 or m==1:
    print(1)
elif n == 2:
    if m==2: print(1)
    elif m==3 or m==4: print(2)
    elif m==5 or m==6: print(3)
    else: print(4)
else:
    if m==2: print(2)
    elif m==3: print(3)
    elif 4<=m<=6: print(4)
    else: print(m-2)