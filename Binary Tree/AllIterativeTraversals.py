from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    def inOrder(root):
        ans = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur =cur.left
            cur = stack.pop()
            ans.append(cur.data)
            cur = cur.right
        return ans 

    def preOrder(root):
        ans = []
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.data)
                stack.append(cur.right)
                stack.append(cur.left)
        return ans

    def postOrder(root):
        ans = []
        stack1 = []
        stack2 = []
        stack1.append(root)
        while stack1:
            cur = stack1.pop()
            if cur:
                stack2.append(cur.data)
                stack1.append(cur.left)
                stack1.append(cur.right)
        # print("stack2: ", stack2)
        stack2.reverse()
        # print("ans: ", stack2)
        return stack2

    inorder = inOrder(root)
    preorder = preOrder(root)
    postorder = postOrder(root)

    # print(inorder)
    # print(preorder)
    # print(postorder)

    return [inorder, preorder, postorder]

    pass