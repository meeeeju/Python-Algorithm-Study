# 블로그 참고
# 근데 내가 스스로 풀었는데 왜 답이 안 나오는지,,?
import math
def solution(numbers):
    
    def make_binary(n):
        answer =[]
        while n:
            m = n % 2
            n = n //2
            answer.append(m)
        answer.reverse()
        return answer
         
    # 판별하기 (부모가 0 이면 안 됨)
    def check(num_bin, prev_parent):
        # 중앙값(자손) 기준으로 재귀적으로 확인
        mid = len(num_bin) // 2
        if num_bin: son = (num_bin[mid] == '1')
        else: return True

        # 내가 존재하면 부모가 존재해야함.
        if son and not prev_parent:
            return False
        else:
            return check(num_bin[mid + 1:], son) and check(num_bin[:mid], son)
        
    
    result = []
    for n in numbers:
        
        if n == 1 or n ==2 :
            result.append(1)
            continue
            
        # 이진수로 바꾸기  (bin(numbers[i])[2:], format(numbers[i],'b'))    
        num = make_binary(n)
        
        
        # 포화 이진트리로 변경하기
        depth = int(math.log(len(num))) +1
        tree_n = (2**depth)-1
        spare = tree_n- len(num)
        print("필요한 0의 갯수",depth,tree_n,spare)
        full_binary = [0 for _ in range(spare)] + num
    
        print("포화 이진트리",full_binary)
        
        # 부모 체크하기
        if full_binary[len(full_binary) // 2] == '1'and check(full_binary, True):
            result.append(1)
        else:
            result.append(0)
    return result
            
        

