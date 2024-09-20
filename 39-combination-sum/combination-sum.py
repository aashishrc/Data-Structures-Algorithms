class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        ans = []
        n = len(candidates)
        
        def comboSum(start, target, sol, ans):
            # print("step 1: ", sol, ans)
            if start == n:
                if target != 0:
                    return
            if target == 0:
                ans.append(sol.copy())
                # print("sol added: ", ans)
                return
            
            if candidates[start] <= target:
                sol.append(candidates[start])
                # print("after addition: ", sol)
                comboSum(start, target - candidates[start], sol, ans)
                sol.pop()
                comboSum(start+1, target, sol, ans)
            else:
                comboSum(start+1, target, sol, ans)
        
        comboSum(0, target, sol, ans)
        return ans
