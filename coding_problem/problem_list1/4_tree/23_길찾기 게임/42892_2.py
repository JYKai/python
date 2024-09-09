import sys
sys.setrecursionlimit(10**4)

class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

def preorder(tree, pre):
    if tree is None:
        return
    pre.append(tree.info[0])
    preorder(tree.left, pre) # pre가 공유되는건가?
    preorder(tree.right, pre)
    return pre

def postorder(tree, post):
    if tree is None:
        return
    postorder(tree.left, post)
    postorder(tree.right, post)
    post.append(tree.info[0])
    return post

def insert_node(root, info):
    current = root
    while True:
        if current.info[1] > info[1]:
            if current.left is None:
                current.left = Node(info)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = Node(info)
                break
            current = current.right
            
def solution(nodeinfo):
    nodeinfo = [[idx + 1] + node for idx, node in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: (-x[2], x[1]))

    root = Node(nodeinfo[0])
    for info in nodeinfo[1:]:
        insert_node(root, info)
    
    return [preorder(root, []), postorder(root, [])]
