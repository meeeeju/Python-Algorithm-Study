import sys
input = sys.stdin.readline

N = int(input()) # ㅜ
a_list = list(map(int,input().split()))
M = int(input())
b_list = list(map(int,input().split()))
A=1
B=1

for  a in a_list:
    A = a* A
for b in b_list:
    B = b * B

r = 1
if A > B:
    while(r):
        r = A % B
        A = B
        B = r
    gcd = A

else:
    while(r):
        r = B % A
        B = A
        A = r
    gcd = B


if (len(str(gcd))>9):  # 9자리 넘는지 체크
    answer = ""
    for i in range(9):
        answer += str(gcd % (10**1)) 
        gcd = gcd // (10**1)
    print(answer[::-1])
else:
    print(gcd)




