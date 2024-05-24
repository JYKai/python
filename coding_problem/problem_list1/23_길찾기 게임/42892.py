import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insert_node(root, node_data):
    curr = root
    while True:
        if curr.data[1] > node_data[1]:
            if curr.left is None:
                curr.left = Node(node_data)
                break
            else:
                curr = curr.left
        else:
            if curr.right is None:
                curr.right = Node(node_data)
                break
            else:
                curr = curr.right

def preorder(tree, pre):
    if not tree:
        return
    pre.append(tree.data[0])
    preorder(tree.left, pre)
    preorder(tree.right, pre)
    return pre

def postorder(tree, post):
    if not tree:
        return
    postorder(tree.left, post)
    postorder(tree.right, post)
    post.append(tree.data[0])
    return post

def solution(nodeinfo):
    answer = []
    new_nodeinfo = []
    for i, node in enumerate(nodeinfo, start=1):
        new_nodeinfo.append([i] + node)
    new_nodeinfo.sort(key=lambda x: (x[2], -x[1]), reverse=True)
    
    root = Node(new_nodeinfo[0])
    for node in new_nodeinfo[1:]:
        insert_node(root, node)
    
    answer.append(preorder(root, []))
    answer.append(postorder(root, []))
    
    return answer
