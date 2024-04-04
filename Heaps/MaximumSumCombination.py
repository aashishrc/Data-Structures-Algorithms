#link : https://www.interviewbit.com/problems/maximum-sum-combinations/

import heapq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    
    def solve(self, A, B, C):
        A.sort(reverse=True)
        B.sort(reverse=True)
        max_heap = []
        visited = set()
        result = []
        
        # Initialize the heap with the maximum sum from both arrays
        heapq.heappush(max_heap, (-1 * (A[0] + B[0]), 0, 0))
        visited.add((0, 0))
        
        # Continue popping elements from the heap until we find C valid combinations
        while len(result) < C:
            current_sum, i, j = heapq.heappop(max_heap)
            result.append(-1 * current_sum)
            
            # Explore the next possible combinations and add them to the heap if not visited
            if i + 1 < len(A) and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-1 * (A[i + 1] + B[j]), i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(B) and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-1 * (A[i] + B[j + 1]), i, j + 1))
                visited.add((i, j + 1))
        
        return result