# 31256	176
import sys
input = sys.stdin.readline
# 블로그 참고
# 문자열 배열했을 때 정렬의 특성을 잘 활용하자
'''
https://storing.tistory.com/49'''

'''
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346'''

T = int(input())
for _ in range(T):
    n = int(input())
    numbers = []
    answer = 'YES'
    for i in range(n):
        phone_number = input().rstrip()
        numbers.append(phone_number)
    
    numbers.sort()
    for i in range(n-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            answer ='NO'
            break
    print(answer)
    # print(numbers)
