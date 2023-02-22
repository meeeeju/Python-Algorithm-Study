#블로그 참조
#메모리:110564 시간 :896ms
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

N=int(input())
color=[0]+list(map(int,input().split()))
array=[[] for i in range(N+1)]

def checkColor(curr,curr_color,parent,child,color):
    count=0
    if color[curr]!=curr_color:
        count+=1
        curr_color=color[curr]
        
    if not len(child[curr]):
        return count
    
    for curr_child in child[curr]:
        if curr_child==parent:
            continue
        count+=checkColor(curr_child,curr_color,curr,child,color)
    return count

def main():
    
    for i in range(N-1):
        a,b=map(int,input().split())
        array[a]+=[b]
        array[b]+=[a]

    count=checkColor(1,0,-1,array,color)
    print(count)

main()
