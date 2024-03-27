from os import *
from sys import *
from collections import *
from math import *

'''
	 
	 Following is the Binary Tree node structure:
	 
	 class TreeNode:
	     def __init__(self, data=0, left=None, right=None):
	         self.data = data
	         self.left = left
	         self.right = right
'''

def getPreOrderTraversal(root):
    # Write your code here.
	preOrder = []
	cur = root
	while cur != None:
		if cur.left == None:
			preOrder.append(cur.data)
			cur = cur.right
		else:
			prev = cur.left
			while(prev.right and prev.right != cur):
				prev = prev.right
			if prev.right == None:
				prev.right = cur
				preOrder.append(cur.data)
				cur = cur.left
			else:
				prev.right = None
				cur = cur.right
	return preOrder
