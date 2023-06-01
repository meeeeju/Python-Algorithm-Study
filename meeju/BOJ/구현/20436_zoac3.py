# 31256	44
import sys
input = sys.stdin.readline

'''
z o
zoac'''

# 초기화
left_dict = {'q':(0,0),'w':(0,1),'e':(0,2),'r':(0,3),'t':(0,4),'a':(1,0),'s':(1,1),'d':(1,2),'f':(1,3),'g':(1,4),'z':(2,0),'x':(2,1),'c':(2,2),'v':(2,3)}
right_dict = {'y':(0,5),'u':(0,6),'i':(0,7),'o':(0,8),'p':(0,9),'h':(1,5),'j':(1,6),'k':(1,7),'l':(1,8),'b':(2,4),'n':(2,5),'m':(2,6)}

sl ,sr = input().split()    #  sL, sR은 각각 왼손 검지손가락, 오른손 검지손가락의 처음 위치
words = input().rstrip()    #  문자열
left = left_dict[sl]
right = right_dict[sr]
time = 0

for w in words:
    if w in left_dict.keys():   # 왼쪽 자판의 것이라면 
        cost = abs(left[0]-left_dict[w][0])+abs(left[1]-left_dict[w][1])
        left = left_dict[w]
    else:                       # 오른쪽 자판의 것이라면 
        cost = abs(right[0]-right_dict[w][0])+abs(right[1]-right_dict[w][1])
        right= right_dict[w]
    time += cost    # 이동 비용
    time += 1       # 클릭 비용

print(time)