#143400KB /	4736ms
import sys
input = sys.stdin.readline

'''
4 7
20 15 10 17

Test case : M이 나오지 않는 경우 
7 8 
9 9 9 9 9 9 9
7
'''

N, M =map(int, input().split())  # N : 나무의 수 , M : 상근이가 필요한 나무 m
tree = list(map(int,input().split()))



if len(tree)==1:
    print(tree[0]-M)
else:
    tree.sort()
    start = 0
    end = tree[-1]
    max_height = 0 
    while (start <= end):
        current_sum  = 0 
        mid = (start+end)//2  # 버림 사용 

        for i in tree:
            if i > mid :
                current_sum += i - mid
        if current_sum > M :    # 더 많이 남음
            start = mid +1  # 오른쪽으로 이동
        elif current_sum < M :
            end = mid -1 # 왼쪽으로 이동
        else:
            max_height = mid
            break
    else:   #  current_sum이 M 이랑 같은 수가 나오지 못 한 경우 
        max_height = end    # M 이상 중 가장 작은 값일 때의 절단기 높이

    print(max_height)
            

            



