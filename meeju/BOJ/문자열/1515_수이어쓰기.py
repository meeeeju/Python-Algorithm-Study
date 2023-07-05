# 블로그 참고 - 재귀를 써야하나..? 이해가 잘 안 되뮤ㅠ
# import sys
# input = sys.stdin.readline

'''
234092'''


# lines =list(map(int,input().rstrip()))
# print(lines)
# # current = [0,0,0,0] # 3000

# current = lines[0]

# for i in range(1,len(lines)):

#     current_last = current % 10

#     if current_last  > lines[i]:  # 자신보다 큰 수를 만날경우
#         current = (current //10) *10 + lines[i]
#     elif current_last < lines[i]:
#         temp = current + 10
#         temp = (temp//10) *10 + lines[i]

#         if i+len(str(current))<len(lines):
#             if  current < lines[i:i+len(str(current))] :
#                 current = lines[i:i+len(str(current))]
        
#         current = min(current,temp)


import sys
S = sys.stdin.readline().strip()
n = 0
while len(S):
    n += 1 # 1칸씩 찾기
    num = str(n)
    while len(num) and len(S): #둘 다 아직 숫자가 있고
        if num[0] == S[0]: #만약 n의 앞자리가 S의 앞자리랑 같으면
            S = S[1:] # 앞자리 잘라내
        num = num[1:] # 앞자리 이동
print(n)
        