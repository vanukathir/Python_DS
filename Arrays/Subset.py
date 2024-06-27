from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res , sol = [] , []
        n = len(nums)

        def subsetGenerative(i):
            if(i == n):
                res.append(sol[:])
                return
            subsetGenerative(i+1)
            sol.append(nums[i])
            subsetGenerative(i+1)
            sol.pop()

        subsetGenerative(0)
        return res

s = Solution()
result = s.subsets([1,2,3])
print(result)

