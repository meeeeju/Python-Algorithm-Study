import sys

vowel=['a','e','i','o','u']  #모음 모음집

while True:
    text=sys.stdin.readline().strip()  # 입력받는 text 값
    if text=='end': break  # 입력받은 값이 end면 종료
    
    v=0   # 모음 개수
    c=0   # 자음 개수
    Perfect=False  # 비밀번호가 완벽한지 구분하는 변수
    
    for i in range(len(text)):    # 입력받은 text 값을 하나씩 확인
        
        if text[i] in vowel :   # 모음 포함 시,
            v+=1                # 모음 개수 증가
            c=0                 # 자음 개수 초기화
            Perfect=True        # 자음이 하나 이상이므로 Perfect 변수 True
        else :                 # 자음 포함 시,
            c+=1                # 자음 개수 증가
            v=0                 # 모음 개수 초기화
            
        # (자음 또는 모음 개수가 3개 연속으로 나올시) or (e와 o를 제외한 같은 글자가 연속 두 번 나올시)
        if v>2 or c>2 or (text[i]!='e' and text[i]!='o' and (i!=len(text)-1 and text[i]==text[i+1])): 
            Perfect=False      #완벽하지 않으므로 False
            break
        
    if Perfect==False : print(f'<{text}> is not acceptable.')
    else : print(f'<{text}> is acceptable.')
        
    
