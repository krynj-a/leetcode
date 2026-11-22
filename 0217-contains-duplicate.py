# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
#
# Idea: Мы закидываем уникальные числа полученного массива в сет. Логика такая: если число уже существует в сет - значит мы нашли повтор. 
# Time: O(n)   Space: O(n) - в худшем случае(все разные) - мы записыаем n элементов в сет


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False


print(Solution().containsDuplicate([1, 2, 3, 1]))  # expected True
print(Solution().containsDuplicate([1, 2, 3, 4]))  # expected False
print(Solution().containsDuplicate([]))            # expected False


# Variant-2
# class Solution:
#   def containsDuplicate(self, nums: List[int]) -> bool:
#      return len(set(nums)) < len(nums)