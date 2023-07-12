import sys
input = sys.stdin.readline

'''
쉬프트 , & 개념

'''

n = int(input())
result = []
while n :
    if n&1 :    # 0번째 비트가 1일경우, N 은 홀수이므로 2를 곱해 0번째 비트를 1로 바꿔준다.
        result.append('[/]')
        n*=2
    elif n&2 :    # 0번째 비트가 0이고 1번째 비트가 1인경우, 2을 빼줘서 1번재 비트를 0으로 만들기.
        result.append('[+]')
        n-=2
    else: # 0번재 1번째 비트가 모드 0인경우:
        result.append('[*]')
        n//=2
print(len(result))
print(' '.join(result[::-1]))
    
