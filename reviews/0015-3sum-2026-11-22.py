# 15. 3Sum — re-solve from scratch (review 2026-11-22)
# https://leetcode.com/problems/3sum/
# Rule: no peeking at ../0015-3sum.py, no hints at first.
#
# Idea: мы используем поинтеры, как в 2sum, чтобы найти пару соответствующей -nums[i], которую записываем в сет, чтобы избежать дубликатов и не делать лишних проверок.
# если сумма найменьшего и найбольщего - больше таргета - нужно уменьшнить найбольшее, ведь в противном случае - все последующее суммы будут больше, при условии, что массив сортирован
# в ином случае двигаем найменьшее, чтобы увеличить значение
# Time: O(n^2)   Space: O(n)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s = set()
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            target = 0 - nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            elif nums[i] > 0:
                break
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                    continue
                if nums[left] + nums[right] == target:
                    triple =[nums[left], nums[right], nums[i]]
                    s.add(tuple(triple))
                left += 1
        return [list(item) for item in s]


s = Solution()
print(s.threeSum([-100,-70,-60,110,120,130,160]))  # expected [[-100,-60,160],[-70,-60,130]]
print(s.threeSum([0, 1, 1]))              # expected []
print(s.threeSum([0, 0, 0]))              # expected [[0, 0, 0]]
print(s.threeSum([-2, 0, 0, 2, 2]))       # expected [[-2, 0, 2]]  (duplicates!)
