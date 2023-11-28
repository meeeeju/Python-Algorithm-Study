def solution(survey, choices):
    
    mbti = ['R','C','J','A']
    score_board = {1:3,2:2,3:1} # 번호별 획득 점수
    personality = [0,0,0,0,0,0,0,0] # R,T,C,F,J,M,A,N
    person_alpha=['T','F','M','N']
    
    for i  in range(len(survey)):
        q = survey[i]
        choice = choices[i]
        score = 0
        
        if choice == 4:
            continue
            
        if q =='RT':
            if choice > 4:
                personality[1] += score_board[8-choice]
            else:
                personality[0] += score_board[choice]
        if q =='TR':
            if choice > 4:
                personality[0] += score_board[8-choice]
            else:
                personality[1] += score_board[choice]

        if q =='FC':
            if choice > 4:
                personality[2] += score_board[8-choice]
            else:
                personality[3] += score_board[choice]
        if q =='CF':
            if choice > 4:
                personality[3] += score_board[8-choice]
            else:
                personality[2] += score_board[choice]
        if q =='MJ': # j가 4
            if choice > 4:
                personality[4] += score_board[8-choice]
            else:
                personality[5] += score_board[choice]
            
        if q =='JM':
            if choice > 4:
                personality[5] += score_board[8-choice]
            else:
                personality[4] += score_board[choice]
                
        if q =='AN':
            if choice > 4:
                personality[7] += score_board[8-choice]
            else:
                personality[6] += score_board[choice]
            
        if q =='NA':
            if choice > 4:
                personality[6] += score_board[8-choice]
            else:
                personality[7] += score_board[choice]
                
#     personality = [0,0,0,0,0,0,0,0] # R,T,C,F,J,M,A,N
    
    cnt =0
    for i in range(0,8,2):
        if personality[i] < personality[i+1]:
            mbti[cnt] = person_alpha[cnt]
        cnt+=1
    
    answer = ''.join(mbti)
    # print(answer)
    
    
    

    return answer