# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
#
# Idea: каждое число имеет до и после, которые можно вычислить за два прохода массива с разных концов - произведение суффикса и префикса - как раз и будет искомое значение
# Time: O(n)   Space: O(n)


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        suffix = prefix = 1
        d = []

        d.append(prefix)
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            d.append(prefix)

        for i in range(len(nums)-2, -1,-1):
            suffix *= nums[i+1]
            d[i] *= suffix
        
        return d


print(Solution().productExceptSelf([1, 2, 3, 4]))       # expected [24, 12, 8, 6]
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))  # expected [0, 0, 9, 0, 0]
print(Solution().productExceptSelf([2, 3]))             # expected [3, 2]
