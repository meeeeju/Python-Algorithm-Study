# 실패잼
import sys
input = sys.stdin.readline


'''
N K P X
N : 층수
K : 자리수
P : 반전시킬 수 있는 최대 갯수
x : 현재 층수
9 1 2 5
'''

display_info = {0:set([1,2,3,4,5,6]),1:set([4,5]),2:set([2,3,5,6,7]),
                3:set([3,4,5,6,7]),4:set([1,4,5,7]),
                5:set([1,3,4,6,7]),6:set([1,2,3,4,6,7]),
                7:set([4,5,6]),8:set([1,2,3,4,5,6,7]),9:set([1,3,4,5,6,7])}

# a= set([1,2,5,7,4])
# b = set([2,3])
# print(a|b-a&b)

N, K,P,X = map(int,input().split())
X =str(X)
result =[]
result_count =[]

for digit in X:
    
    candidate =[]
    count = 0 
    for i in range(10):
        temp = display_info[i]
        current = display_info[int(digit)]
        p = len(temp-current)+ len(current-temp)
        if 1 <= p <= P :
            candidate.append(i)
            count +=1
    result.append(candidate)
    result_count.append(count)


print(result,result_count )