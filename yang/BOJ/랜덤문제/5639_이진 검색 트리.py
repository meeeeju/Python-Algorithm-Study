# 346292KB / 1128ms (PyPy3)

import sys
sys.setrecursionlimit(10 ** 4 + 1)
input = sys.stdin.readline

### 노드 자료구조
class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

### 이진 검색 트리에서 삽입하기
def binary_insert(root: Node, value: int):
    if root.value > value:
        if root.left != None:
            binary_insert(root.left, value)
        else:
            root.left = Node(value)
    elif root.value < value:
        if root.right != None:
            binary_insert(root.right, value)
        else:
            root.right = Node(value)

### 후위 순회하기
def postorder(node: Node):
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    print(node.value)

### solution
root = None
while True:
    try:
        value = int(input())
        if root != None:
            binary_insert(root, value)
        else:
            root = Node(value)
    except:
        break
postorder(root)


### solution
# root = None
# preorder = []
# while True:
#     try:
#         value = int(input())
#         preorder.append(value)
#     except:
#         break

# root = Node(preorder[0])
# for i in range(1, len(preorder)):
#     binary_insert(root, preorder[i])
# postorder(root)