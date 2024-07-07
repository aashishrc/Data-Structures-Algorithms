class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] in numbers[:i] or target - numbers[i] in numbers[i+1:]:
                print(numbers[i+1:].index(target- numbers[i]))
                return [i + 1, numbers[i+1:].index(target- numbers[i]) + i + 2]