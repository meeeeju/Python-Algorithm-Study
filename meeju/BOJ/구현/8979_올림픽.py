# 31256	40
import sys
input = sys.stdin.readline

'''
4 3
1 1 2 0
2 0 1 0
3 0 1 0
4 0 0 1'''

n,k = map(int,input().split())  # n : 국가의 수, k : 등수를 알고 싶은 나라의 번호

prize_info= [0 for _ in range(n)] 


for i in range(n):

    country, gold,silver,dong = map(int,input().split())
    prize_info[i]=(gold,silver,dong,country)

# print(prize_info)
prize_info.sort(key=lambda x:(-x[0],-x[1],-x[2]))
# print(prize_info)


def find_rank(k):
    
    rank =1
    same_size = 1
    for i in range(n):

        if prize_info[i][0] > prize_info[i+1][0]:   # 금메달 비교
            rank +=same_size   
            same_size = 0
        elif prize_info[i][1] > prize_info[i+1][2]: # 은메달 비교
            rank +=same_size
            same_size = 0
        elif prize_info[i][1] > prize_info[i+1][2]: # 동메달 비교
            rank+=same_size
            same_size = 0
        else:
            same_size +=1
        
        if prize_info[i][3] == k:
            return rank
    
    
print(find_rank(k))
