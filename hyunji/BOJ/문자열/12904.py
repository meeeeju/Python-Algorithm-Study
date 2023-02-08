S=list(input().rstrip())
T=list(input().rstrip())


# =============================================================================
# liist=[]
#for _ in range(len(T)):
#     S=S+"A"
#     liist.append(S)
#     S=S[::-1]+"B"
#     liist.append(S)
# 
# if T not in liist:
#     print(0)
# else:
#     print(1)
# =============================================================================
for _ in range(len(T)-len(S)):
    if T[-1]=="A":
        T.pop()
    elif T[-1]=="B":
        T.pop()
        T.reverse()

if S==T:
    print(1)
else:
    print(0)