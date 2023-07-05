# 블로그 참고
import sys
input = sys.stdin.readline



'''mirkovC4nizCC44
C4
'''


# words = list(input().rstrip())
# boom_word = input().rstrip()
# boom_len = len(boom_word)

# while True:
#     j=0

#     for i in range(j,len(words)-boom_len+1):

#         if ''.join(words[i:i+boom_len]) ==boom_word:
#             words = words[:i]+words[i+boom_len:]
#             break
#         j=i
#     else:
#         break
# if not words:
#     print("FRULA")
# else:
#     print("".join(words))



"""
    1. 입력문자열을 앞에서부터 차례차례 한 글자씩 스택에 push 합니다.
    2. 현재 글자가 폭발 문자열의 마지막 글자와 일치하면 
스택의 top부터 폭발문자열의 길이까지 확인하여 폭발문자열이 만들어지는지 확인합니다.
    3. 폭발문자열이 만들어진다면 만들어지는 폭발문자열을 스택에서 pop합니다.
    4. 1~3을 반복합니다.
    5. 문자열 순회를 마치고 스택이 비어있으면, FRULA를 출력, 비어있지 않다면 스택 속 문자열을 차례로 출력합니다.
"""
 
def main():
 
    string = input()    # 전체 문자열
    bomb = input()      # 폭발 문자열
 
    lastChar = bomb[-1] # 폭발 문자열의 마지막 글자
    stack = []
    length = len(bomb)  # 폭발 문자열의 길이
 
    for char in string:
        stack.append(char)
        if char == lastChar and ''.join(stack[-length:]) == bomb:
            del stack[-length:]
 
    answer = ''.join(stack)
 
    if answer == '':
        print("FRULA")
    else:
        print(answer)
 
 
if __name__ == '__main__':
    main()