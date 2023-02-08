# =============================================================================
# #하다가 포기한 코드
# 
# S=input()
# alpha=list(S)
# liist=[]
# liist2=[]
# liist3=[]
# 
# for i in range(len(S)):
#     liist.append(alpha[i])
# 
# liist.sort()
# 
# for i in range(len(liist)):
#     for j in range(len(alpha)):
#         if liist[i]==alpha[j]:
#             liist2.append(S[j:])
#             
# liist2.sort()            
# print(liist2)
# =============================================================================
#블로그 참고
S=input()
liist=[]

for i in range(len(S)):
    liist.append(S[i:])
    
liist.sort()

for i in range(len(liist)):
    print(liist[i])