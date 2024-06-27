from typing import List
def subsetXORSum( nums: List[int]) -> int:
    res, sol = [], []
    n = len(nums);
    xor = 0
    final_result = 0

    def subset(i: int):
        if (i == n):
            res.append(sol[:])
            return;
        subset(i + 1);
        sol.append(nums[i])
        subset(i + 1)
        sol.pop()


    subset(0)

    for val in res:
        for itr in val:
            xor ^= itr
        final_result += xor
    return final_result

res = subsetXORSum([1,2,3])
print(res)