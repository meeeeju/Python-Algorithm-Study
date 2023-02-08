import sys

N = int(input())
sales_books={}

for _ in range(N):
    book=input().rstrip()
    if book in sales_books:
        sales_books[book]+=1
    else:
        sales_books[book]=1

listed = sorted(sales_books.items(), key = lambda x : (-x[1], x[0])) 

print(listed[0][0])


'''
풀이
딕셔너리를 활용할 수 있는 것이 핵심이다.


input 
5
top
top
top
top
kimtop

output 
9
table
chair
table
table
lamp
door
lamp
table
chair
'''


