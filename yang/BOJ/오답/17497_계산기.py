# 블로그 코드
n =  int(input())
ans = []
while n: # n을 0으로 만들기. 즉 모든 비트를 0으로 만들자.
    if n&1 : # 01, 11 -> 10 (홀수면 나누기 연산으로 없앰)
        ans.append('[/]')
        n *= 2
    elif n&2 : # 10 -> 00
        ans.append('[+]')
        n -= 2
    else : # 00 -> 없앰
        ans.append('[*]')
        n //= 2
print(len(ans))
print(' '.join(ans[::-1]))