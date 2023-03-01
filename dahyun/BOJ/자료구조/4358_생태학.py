#BackJoon 4358 생태학
# 31256 KB / 536 ms
import sys
tree_type={}
total=0 # 나무의 전체 개수
while True:
    tree=''
    tree=sys.stdin.readline().strip()
    if tree=='': break
    if tree in tree_type: tree_type[tree]+=1  # tree_type에 존재하면 개수 +1
    else : tree_type[tree]=1  # tree_type에 존재하지 않으면 1로 초기화
    total+=1산
for t in sorted(tree_type.items(), key=lambda x : x[0]):  # tree 이름을 사전 순으로 정렬 후 계
    print(t[0],format((t[1]/total)*100,".4f"))
