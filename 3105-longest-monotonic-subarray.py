# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
#
# Idea: Мы проходим массив - постоянно сравнивая пары вхождений, если второе число больше - увеличивается соответственный каунтер, меньше - противоположный. Важно следить за сбросами каунтеров
# чтобы прогресс предыдущего увеличения/уменьшения - не перенесся дальше и не повлиял на результат
# Time: O(n) - бежим по массиву и за раз смотрим увеличение и падение   Space: O(1) - по факту только переменные  inc_count, dec_count, best


class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inc_count = 1
        dec_count = 1
        best = 1
        for i in range(len(nums)-1):
            
            if nums[i] < nums[i+1]:
                inc_count += 1
                dec_count = 1
                if best < inc_count:
                    best = inc_count
                continue
            elif nums[i] > nums[i+1]:
                dec_count += 1
                inc_count = 1
                if best < dec_count:
                    best = dec_count
                continue
            inc_count = 1
            dec_count = 1
        return best

print(Solution().longestMonotonicSubarray([3, 2, 1]))        # expected 3
print(Solution().longestMonotonicSubarray([1, 4, 3, 3, 2]))  # expected 2
print(Solution().longestMonotonicSubarray([3, 3, 3, 3]))     # expected 1
