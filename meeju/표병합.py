import sys
sys.setrecursionlimit(10**6)
# 초기화
N = 51
parent =[[(i,j) for j in range(N)]for i in range(N)]
values =[['' for _ in range(N)]for _ in range(N)]


def find(i,j): # find(parent,2,3)
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[i][j] != (i,j):
        return find(parent[i][j][0],parent[i][j][1])
    return (i,j)

def solution(commands):

    answer = []
    # 명령어 하나씩 돌기
    for c in commands:
        word = c.split()
        order = word[0]

        if order=='UPDATE':
            if len(word)==4:
                r = int(word[1])
                c = int(word[2])
                value = word[3]
                x = find(r,c)
                values[x[0]][x[1]]=value
            else: #  value1인 것들은 value2로 다 바꾸기
                value1 = word[1]
                value2 = word[2]
                for i in range(1,N):
                    for j in range(1,N):
                        if parent[i][j] == (i,j): # root 인 것들
                            if values[i][j]== value1:
                                values[i][j] = value2
        elif order =='MERGE':
            r1,c1,r2,c2 = map(int,word[1:])

            x = find(r1,c1)
            y = find(r2,c2)
            if x == y:
                continue
            if not values[x[0]][x[1]] and values[y[0]][y[1]]: # 첫번째 위치의 값이 있다면
                parent[x[0]][x[1]] = y
            else:
                parent[y[0]][y[1]] = x 

        elif order =='UNMERGE':
            r,c = map(int,word[1:])
            x = find(r,c)
            value = values[x[0]][x[1]]
            temp =[]
            for k in range(1,N):
                for l in range(1,N):
                    if find(k,l) == x:
                        values[k][l]= ''
                        temp.append((k,l))
            values[r][c]=value
            for v,w in temp:
                parent[v][w]=(v,w)
            
            
        else:
            r,c = map(int,word[1:])
            x= find(r,c)
            if not values[x[0]][x[1]]:
                answer.append('EMPTY')
            else: answer.append(values[x[0]][x[1]])
            # print(parent[x[0]][x[1]][1])
    
    return answer

#print(solution(["UPDATE 1 1 a"]))

print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
#print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))

#print(solution(["MERGE 1 1 2 2", "MERGE 1 1 3 3", "UPDATE 3 3 A", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3"]))
#print(solution(["UPDATE 1 1 apple", "MERGE 1 1 2 2", "MERGE 2 2 3 3", "UNMERGE 1 1", "UNMERGE 2 2", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3"]))