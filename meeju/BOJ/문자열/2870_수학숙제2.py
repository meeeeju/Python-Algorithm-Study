# 31256	44
import sys
input = sys.stdin.readline



'''바부,,,,,int() 는 자동으로 문자열 앞에 오는 0을 무시하고 변환함;;'''
'''
2
lo3za4
01'''

N = int(input())    # 줄의 갯수
number_list=['0','1','2','3','4','5','6','7','8','9']
result = []

for _ in range(N):
    paper = input().rstrip()

    # 초기화
    start = 0
    end = 0

    # for i in range(len(paper)):
    size = len(paper)
    i = 0
    while(i<size):

        if paper[i] in number_list :
            for j in range(i+1,len(paper)):
                if paper[j] not in number_list:
                    break
            else:
                result.append(int(paper[i:])) # for - else 조건문에 걸리면  aa1233
                break 
            result.append(int(paper[i:j]))
            i= j
        else:
            i +=1

result.sort()
for i in result:
    print(i)

                    
            

        
