# 블로그 참고
# https://school.programmers.co.kr/questions/51024 <= 이 글이 이해가 제일 잘됐음
# https://wondev.tistory.com/154 <= 코드는 여기서 봄
import math

def solution(edges, target):    
    graph = {i: [] for i in range(1, len(target)+1)}
    for edge in edges:
        v1, v2 = edge
        graph[v1].append(v2)

    # 리프 노드에 숫자가 떨어진 횟수 저장.
    leaf_cnt = {}
    # graph 내부 간선 정리, 리프 노드의 target 저장.
    for i in graph:
        if len(graph[i]) == 0: # 리프노드면          
            leaf_cnt[i] = 0 # 초기화    
            continue
        graph[i] = sorted(graph[i]) # 숫자가 적은 순대로 미리 정렬

    # cursor -> 가리키는 child node의 index
    cursor = {i: -1 for i in range(1, len(target)+1)}
    for i in graph:        
        if len(graph[i]): # 리프 노드가 아니면
            cursor[i] = 0   

    # 리프 노드에 숫자가 떨어지는 순서.    
    leaf = []     

    # while문 flag값.    
    isFin = False  
    
    while not isFin:        
        # root node에서 시작       
        a = 1        
        # 리프 노드에 도달할 때 까지 반복        
        while cursor[a] != -1:           
            temp = a  
            a = graph[a][cursor[a]]
            # 지나간 후 커서를 새로 설정
            cursor[temp] = (cursor[temp] + 1) % len(graph[temp])

        # 떨어뜨린 리프 노드의 순서 저장
        leaf.append(a)        
        # 리프 노드의 떨어뜨려진 횟수 추가        
        leaf_cnt[a] += 1
    
        # 만족하는 지 검증 (이 부분을 Brute-Force로 처리해도 되는 지 고민했으나, 최대 횟수가 100x100회를 넘지 않기 때문에, 전체 탐색으로 구현함.)        
        isFin = True        
        for i in leaf_cnt:            
            if leaf_cnt[i] < int(math.ceil(target[i-1]/3)):                
                isFin = False
                break            
            elif leaf_cnt[i] > target[i-1]:                
                # 허용 범위를 넘어가면.. -1 출력 후 종료                
                return [-1] 
    # 1 먼저 채워 넣기    
    result = [1 for _ in range(len(leaf))]    
    for i in leaf:
        target[i-1] -= 1
        
    # 뒤에서부터 되는 대로 숫자 추가하기 (0, 1, 2 중..)    
    for i in range(len(leaf)-1, -1, -1):        
        if target[leaf[i]-1] >= 2: # 3 떨어트림
            result[i] += 2
            target[leaf[i]-1] -= 2 
        elif target[leaf[i]-1] == 1: # 2 떨어트림
            result[i] += 1
            target[leaf[i]-1] -= 1
        else:            
            continue                
    return result