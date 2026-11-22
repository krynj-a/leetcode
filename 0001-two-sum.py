# 1. Two Sum
# https://leetcode.com/problems/two-sum/
#
# Idea: Вариант 1 - простой перебор по факту до первого нахождения, худшее время O(n^2) - из-за вложенного фор. 
# Вариант 2 - поиск по ключам - мы проходим массив лишь один раз -> O(n) - хитрость в том, что идет проверка словаря, который мы дополняем по мере проходки по циклу. 
# Если пара уже входила в словарь - выводим по её ключу индекс, но так трейдим память  ведь придется сохранять словарь - то есть память может достигать O(n), в отличие от O(1) первого случая
# Time: O(?)   Space: O(?)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       
        for i in range(len(nums)-1):
            pair = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == pair:
                    idx = [i, j]
                    return idx
#Variant 2
    def twoSumDic(self, nums: list[int], target: int) -> list[int]:
        d = {}   
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in d:
                return [d[pair], i]
            else: d[nums[i]] = i


print(Solution().twoSum([2, 7, 11, 15], 9))  # expected [0, 1]
print(Solution().twoSum([3, 2, 4], 6))       # expected [1, 2]
print(Solution().twoSum([3, 3], 6))          # expected [0, 1]

print("----------------------------------------")
print(Solution().twoSumDic([2, 7, 11, 15], 9))  # expected [0, 1]
print(Solution().twoSumDic([3, 2, 4], 6))       # expected [1, 2]
print(Solution().twoSumDic([3, 3], 6))          # expected [0, 1]