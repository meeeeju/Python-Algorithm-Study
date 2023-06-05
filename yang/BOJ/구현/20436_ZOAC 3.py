# 31256KB / 40ms
leftKeys = {'q':(0,0), 'w':(0,1),'e':(0,2),'r':(0,3),'t':(0,4),
            'a':(1,0),'s':(1,1),'d':(1,2),'f':(1,3),'g':(1,4),
            'z':(2,0),'x':(2,1),'c':(2,2),'v':(2,3)}
rightKeys = {'y':(0,5), 'u':(0,6),'i':(0,7),'o':(0,8),'p':(0,9),
            'h':(1,5),'j':(1,6),'k':(1,7),'l':(1,8),
            'b':(2,4),'n':(2,5),'m':(2,6)}
L, R = input().split()
goalString = input()
time = 0
for i in goalString:
    time += 1
    if i in leftKeys:
        time += abs(leftKeys[L][0]-leftKeys[i][0])+abs(leftKeys[L][1]-leftKeys[i][1])
        L = i
    else:
        time += abs(rightKeys[R][0]-rightKeys[i][0])+abs(rightKeys[R][1]-rightKeys[i][1])
        R = i
print(time)