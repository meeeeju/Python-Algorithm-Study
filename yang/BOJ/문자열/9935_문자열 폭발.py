# 블로그 참고
# 42436KB / 540ms

string = input()
bomb = input()
newString = []

for i in range(len(string)):
    newString.append(string[i])
    if string[i]==bomb[-1] and ''.join(newString[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            newString.pop()
if newString:
    print(''.join(newString))
else:
    print('FRULA')

# string = input()
# bomb = input()
# newString = []
# isBomb = [False]*len(string)
# s = 0
# while s <= len(string)-len(bomb):
#     if isBomb[s]:
#         s+=1
#         continue
#     p = 0; count = 0
#     while count < len(bomb) and s+p<len(string): # s를 시작점으로 폭발 문자열 여부 검사
#         if isBomb[s+p]: p+=1
#         else:
#             if string[s+p]!=bomb[count]:
#                 break
#             p+=1; count +=1
#     if count==len(bomb): # 문자열 폭발
#         for i in range(s, s+p):
#             if i < len(string):
#                 isBomb[i] = True
#         for p in range(len(bomb)-1):
#             if s > 0:
#                 s -= 1
#             if len(newString) > 0:
#                 newString.pop()
#         continue
#     newString.append(string[s])
#     s += 1
# for i in range(s, len(string)):
#     if not isBomb[i]: newString.append(string[i])
# if len(newString)==0:
#     print("FRULA")
# else:
#     print(''.join(newString))