class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right - left))
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max_area

        # Brute Force
        # max_area = -1
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         if height[j] <= height[i]:
        #             max_area = max(height[j]*(j-i), max_area)
        #         else:
        #             max_area = max(height[i]*(j-i), max_area)
        # return max_area