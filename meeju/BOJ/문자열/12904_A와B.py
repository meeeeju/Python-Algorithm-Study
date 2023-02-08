import sys
input= sys.stdin.readline
'''
#input
B
ABBA
#output
'''

S=list(input().rstrip())
T=list(input().rstrip())

check= False
while(len(T)):  #len T 랑 T 랑 같음
    if T[-1]=='A':
        T.pop()
    else:
        T.pop()
        T.reverse()
    if T==S:
        check=True
        break


if check:
    print(1)
else:
    print(0)
    


