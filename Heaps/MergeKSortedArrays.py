#link : https://www.naukri.com/code360/problems/merge-k-sorted-arrays_975379

from sys import *
from collections import *
from math import *

def mergeKSortedArrays(kArrays, k:int):
	# Write your code here.
	# kArrays is a list of 'k' lists.
	# Return a list.
	temp = kArrays[0][:]
	for i in range(k):
		if i + 1 < k:
			for j in kArrays[i+1]:
				temp.append(j)
	temp.sort()
	# print(type(temp))
	return temp
	pass