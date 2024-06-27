class Solution:
    def permute( nums: list[int]) -> list[list[int]]:
        res, sol = [] , []
        n = len(nums)
        def backtracking():
            if(len(sol) == n):
                res.append(sol[:])
                return
            for i in nums:
                if(i not in sol):
                    sol.append(i)
                    backtracking()
                    sol.pop()

        backtracking()
        return res

    list = permute([1,2,3])
    print(list)


