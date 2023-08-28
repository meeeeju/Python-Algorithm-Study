# 31256	48
import sys
input = sys.stdin.readline

'''
15
AFC
AAFC
AAAFFCC
AAFCC
BAFC
QWEDFGHJMNB
DFAFCB
ABCDEFC
DADC
SDFGHJKLQWERTYU
AAAAAAAAAAAAABBBBBBBBBBBBBBCCCCCCCCCCCCCCCCCCDDDDDDDDDDDEEEEEEEEEEEEEEEFFFFFFFFC
AAAFFFFFBBBBCCCAAAFFFF
ABCDEFAAAFFFCCCABCDEF
AFCP
AAFFCPP'''

def IsPattern(s):
    
    j = 0

    if s[0] not in rule1 :
        return False
    elif s[0] == rule2[j]:
        j +=1
        
    for i in range(1,len(s)):

        if s[i] == rule2[j]:
            j +=1
            if j == 3 :
                break
        elif  s[i] == rule2[j-1]:
            continue
        else:
            return False
        
    if i+1 == len(s) or (s[i+1] in rule1 and i+2 == len(s) ):    # 조건 :  그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.
        return True
    else:
        return False
    

rule1 = [ 'A', 'B', 'C', 'D', 'E', 'F' ]
rule2= ['A','F','C']

T = int(input())
for _ in range(T):
    s = input().rstrip()
    if IsPattern(s):
        print("Infected!")
    else:
        print("Good")
   

        
