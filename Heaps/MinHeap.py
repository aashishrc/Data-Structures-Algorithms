# link : https://www.naukri.com/code360/problems/min-heap_4691801?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
from sys import *
from collections import *
from math import *
import heapq

def minHeap(N: int, Q: [[]]) -> []:
    arr = []
    ans= []
    for i in range(N):
        if Q[i][0] == 0:
            arr.append(Q[i][1])
            heapq.heapify(arr)
        else:
            ans.append(arr[0])
            arr.pop(0)
            heapq.heapify(arr)
    return ans
    pass

