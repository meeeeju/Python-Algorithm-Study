import sys
S = sys.stdin.readline().strip() # 문자열 입력받기
text=[]
for i in range(len(S)): # 문자열 접미사 text 리스트에 추가
    text.append(S[i:])
text.sort()  # 모든 접미사 사전형(오름차순)으로 정렬
for t in text:   # 출력
    print(t)
