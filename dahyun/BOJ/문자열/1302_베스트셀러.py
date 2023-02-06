import sys
input = sys.stdin.readline
dic = dict()  # 해쉬 사용

for _ in range(int(input())):  # 입력받은 책의 개수만큼 반복문
    text = input().strip()
    if text in dic : dic[text]+=1   # 입력받은 책 제목이 사전에 존재하면 +1
    else : dic[text]=1       # 존재하지 않으면 사전에 해당 책 제목 추가하기

# 해당 사전의 items의 values를 기준으로 내림차순 , keys를 기준으로 오름차순 정렬 후, 첫 번째 값 출력
print(sorted(dic.items(),key=lambda item : (-item[1],item[0]))[0][0])력
