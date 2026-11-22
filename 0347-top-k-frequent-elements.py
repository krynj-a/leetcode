# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
#
# Idea: Изначально план был просто отсортировать массив в порядке спадання и вывести первые k уникальных чисел, но тогда бы complexity было - O(nlogn), поэтому я решил прибегнуть к уже любимому
# методу - словарю. вначале мы делаем n проходов - считая кол-во вхождений уникальных чисел, а после сортируем эти числа по частотам - тут в худшем случае n проходок, если все числа уникальны
# а потом идем от макс фриквенси к минимальной - от n к одному - то есть n-1 проходок в худшем случае, после мы заглядываем в словарь и там проходим ещё один фор, чтобы сформировать наш топ - что
# ещё k  проходок, а так как k может быть равна n - выйдет общая O(?) = n+n+(n-1)+n=4n-1, константы может отбросить ->  O(n), а места займет O(3n) = O(n) - из-за словарей и резалт массива
# Time: O(n)   Space: O(n)


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_freq = {}
        freq_num = {}
        for num in nums:
            if  num not in num_freq:
                num_freq[num] = 0
            num_freq[num] += 1
       
        for key, value in num_freq.items():
            if  value not in freq_num:
                freq_num[value] = []
            freq_num[value].append(key)
        result = []
        frequency = len(nums)
        while frequency >= 1:
            if frequency in freq_num:
                for num in freq_num[frequency]:
                    if len(result) < k:
                        result.append(num)
                    else: 
                        return result
                if len(result) == k:
                    return result
            frequency -= 1

print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))  # expected [1, 2] (any order)
print(Solution().topKFrequent([1], 1))                 # expected [1]
print(Solution().topKFrequent([4, 4, 5, 5, 5, 6], 1))  # expected [5]
